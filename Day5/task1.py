def main():
	i = read_input('input1.txt')
	almanac = format_input(i)

	locations = []
	for seed in almanac['seeds']:
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
			# destination has the same offset from its base value as the source
			destination = dest + (source - src)
	return destination

def format_input(i:str):
	parts = i.split('\n\n')
	# print(parts)
	seeds = [int(num) for num in parts[0].split(': ')[1].split(' ') if num != '']
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