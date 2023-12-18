def main():
	i = read_input('input1.txt')
	almanac = format_input(i)
	location = 9999999999999999999999999999999999
	
	print(len(almanac['seeds']))
	seedmap = almanac['seeds']

	seed = -1
	location_ranges = get_destination_ranges_from_map(almanac['humidity_to_location'])
	humidity_ranges = translate_ranges_back(almanac['humidity_to_location'], location_ranges)
	temperature_ranges = translate_ranges_back(almanac['temperature_to_humidity'], humidity_ranges)
	light_ranges = translate_ranges_back(almanac['light_to_temperature'], temperature_ranges)
	water_ranges = translate_ranges_back(almanac['water_to_light'], light_ranges)
	fertilizer_ranges = translate_ranges_back(almanac['fertilizer_to_water'], water_ranges)
	soil_ranges = translate_ranges_back(almanac['soil_to_fertilizer'], fertilizer_ranges)
	seed_ranges = translate_ranges_back(almanac['seed_to_soil'], soil_ranges)
	# print(seed_ranges)


	locations = []
	# since the order of numbering is preserved across maps the lowest seed number in a range must have the lowest location number
	# further only seed ranges that fall in the ranges of seeds available should be considered
	for seed in [r[0] for r in seed_ranges]:
		for rang in seedmap:
			if seed >= rang[0] and seed <= rang[1]:
				soil = lookup(almanac['seed_to_soil'], seed)
				fertilizer = lookup(almanac['soil_to_fertilizer'], soil)
				water = lookup(almanac['fertilizer_to_water'], fertilizer)
				light = lookup(almanac['water_to_light'], water)
				temperature = lookup(almanac['light_to_temperature'], light)
				humidity = lookup(almanac['temperature_to_humidity'], temperature)
				location = lookup(almanac['humidity_to_location'], humidity)
				# print(f'seed: {seed} => soil: {location}')
				locations.append(location)
			

	
	return min(locations)

def lookup(mapping, source):
	destination = source
	for [dest, src, rang] in mapping:
		if source in range(src, src+rang):
			destination = dest + (source - src)
	return destination

# map ranges of destinations to ranges of sources
def translate_ranges_back(mappings, destination_ranges):
	# each range is checked and partitioned into segments that fit with ranges in the map
	# leftover ranges will translate directly
	source_ranges = []
	leftovers = []
	unchecked = []
	for range in destination_ranges:
		found_overlap = False
		for mapping in mappings:
			mapping_source_range = [mapping[1], mapping[1] + mapping[2]-1]
			mapping_destination_range = [mapping[0], mapping[0] + mapping[2]-1]
			# if there is a start overlap (range starts between the ends of the destination range)
			if mapping_destination_range[0] <= range[0] and mapping_destination_range[1] >= range[0]:
				found_overlap = True
				# if the range is entirely in the destination range
				if mapping_destination_range[1] >= range[1]:
					translated_start = mapping[1] + (range[0] - mapping[0])
					translated_end = mapping[1] + (range[1] - mapping[0])
					source_ranges.append([translated_start, translated_end])
				else: # otherwise it ends outside the range and we split it into a source range and an unchecked range
					translated_start = mapping[1] + (range[0] - mapping[0])
					translated_end = mapping_source_range[1]
					range[0] = mapping_destination_range[1] + 1
					unchecked.append(range)
					source_ranges.append([translated_start, translated_end])
			# if there is an end overlap (range ends between the ends of the destination range), we split it into a source range and an unchecked range
			# we caught full overlap in the previous if
			elif mapping_destination_range[0] <= range[1] and mapping_destination_range[1] >= range[1]:
				found_overlap = True
				translated_start = mapping_source_range[0]
				translated_end = mapping[1] + (range[1] - mapping[0])
				range[1] = mapping_destination_range[0] - 1
				unchecked.append(range)
				source_ranges.append([translated_start, translated_end])
				
		# if neither the start or end overlaps any mapping then the range just translates directly
		if not found_overlap:
			leftovers.append(range)
	
	# handle the unchecked ranges
	if len(unchecked) > 0:
		source_ranges.extend(translate_ranges_back(mappings, unchecked))
	source_ranges.extend(leftovers)
	source_ranges.sort(key=lambda x: x[0])
	# print(f'source ranges: {source_ranges}')

	return source_ranges


def get_destination_ranges_from_map(locationmap):
	ranges = []
	for mapping in locationmap:
		ranges.append([mapping[0], mapping[0] + mapping[2]-1])

	ranges.sort(key=lambda x: x[0])
	# print(ranges)

	# we need to fill out the ranges between those specified as they are valid solutions
	untranslated_ranges = []
	prev_range = None
	for range in ranges:
		if prev_range is None:
			prev_range = range
		else:
			if range[0] - prev_range[1] > 1:
				untranslated_ranges.append([prev_range[1]+1, range[0]-1])
		prev_range = range
	# print(untranslated_ranges)
	ranges.extend(untranslated_ranges)
	ranges.sort(key=lambda x: x[0])

	return ranges

def format_input(i:str):
	parts = i.split('\n\n')
	
	_seeds = [int(num) for num in parts[0].split(': ')[1].split(' ') if num != '']
	seeds = []
	i = 0
	while i < len(_seeds):
		seeds.append([_seeds[i], _seeds[i] + _seeds[i+1]])
		i += 2
	

	seed_to_soil = format_parts(parts[1])
	# print(seed_to_soil)
	soil_to_fertilizer = format_parts(parts[2])
	fertilizer_to_water = format_parts(parts[3])
	water_to_light = format_parts(parts[4])
	light_to_temperature = format_parts(parts[5])
	temperature_to_humidity = format_parts(parts[6])
	humidity_to_location = format_parts(parts[7])

	almanac = {
		'seeds': seeds
		, 'seed_to_soil': seed_to_soil
		, 'soil_to_fertilizer': soil_to_fertilizer
		, 'fertilizer_to_water': fertilizer_to_water
		, 'water_to_light': water_to_light
		, 'light_to_temperature': light_to_temperature
		, 'temperature_to_humidity': temperature_to_humidity
		, 'humidity_to_location': humidity_to_location

	}

	return almanac

def format_parts(part):
	split = part.split('\n')
	mapping = []
	for i in range(1, len(split)):
		part = [int(num) for num in split[i].split(' ') if num != '']
		mapping.append(part)

	return mapping


def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()