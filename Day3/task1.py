def main():
	i = read_input('input1.txt')
	schematic = format_input(i)
	width = len(schematic[0])
	height = len(schematic)

	part_numbers = []
	for row in range(len(schematic)):
		current_number = ''
		is_adjacent = False
		for point in range(len(schematic[row])):
			# handle this being a number
			if schematic[row][point].isdigit():
				if current_number == '':
					is_adjacent = False
				current_number = current_number + schematic[row][point]
			else: # if the number ended
				if is_adjacent and not current_number == '':
					part_numbers.append(int(current_number))
				current_number = ''
			
			# check whether the number is adjecent to a symbol
			for y in range(-1, 2):
				for x in range(-1, 2):
					if row+y >= 0 and row+y<height:
						if point+x >= 0 and point+x < width:
							# print(f'check: {x},{y} = {schematic[row+y][point+x]}')
							if is_symbol(schematic[row+y][point+x]):
								is_adjacent = True

			# print(f'{schematic[row][point]}| current_number: {current_number}, is_adjacent: {is_adjacent}, part_numbers: {part_numbers}')
			# input()
		if not current_number == '' and is_adjacent:
			part_numbers.append(int(current_number))
						
	print(part_numbers)



	return sum(part_numbers)

def is_symbol(thing):
	if (not thing.isdigit()) and (not thing == '.'):
		return True
	return False

def format_input(i:str):
	schema = i.split('\n')
	return schema

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()