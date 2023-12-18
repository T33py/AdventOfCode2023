def main():
	i = read_input('input1.txt')
	schematic = format_input(i)

	gear_ratios = []
	for row in range(len(schematic)):
		for point in range(len(schematic[row])):
			if schematic[row][point] == '*':
				ratio = calculate_gear_ratio(schematic, point, row)
				if ratio > -1:
					gear_ratios.append(ratio)
						
	# print(gear_ratios)
	return sum(gear_ratios)

def calculate_gear_ratio(schematic, x, y):
	width = len(schematic[0])
	height = len(schematic)

	print(f'looking at {x},{y}')

# figure out where there are digits
	found_digits = []
	for _y in range(-1, 2):
		for _x in range(-1, 2):
			if y+_y >= 0 and y+_y<height:
				if x+_x >= 0 and x+_x < width:
					# print(f'check: {x},{y} = {schematic[row+y][point+x]}')
					if schematic[y+_y][x+_x].isdigit():
						found_digits.append([x+_x, y+_y])

	print(found_digits)
	# 2 digits on different rows will never be adjacent => first and last number will be from different rows
	# 2 digits on the same row will either be the same number => one will be at a different row
	# 	or they will be the only 2 digits => we want the first and last number
	# if the first and last digits both come from the same number, we can see that the first digit in the number will have identical coordinates for both
	num1 = ''
	num1_x = found_digits[0][0]
	num1_y = found_digits[0][1]
	num2 = ''
	num2_x = found_digits[len(found_digits)-1][0]
	num2_y = found_digits[len(found_digits)-1][1]

	# go left to the beginning of each number
	while schematic[num1_y][num1_x].isdigit():
		num1_x -= 1
		if num1_x < 0:
			break
	while schematic[num2_y][num2_x].isdigit():
		num2_x -= 1
		if num2_x < 0:
			break
		
	num1_x += 1
	num2_x += 1

	# we now know whether its the same number
	# we can return -1 as the problem space only contains positive numbers
	if num1_x == num2_x and num1_y == num2_y:
		return -1

	
	# go right to the end of each number
	while schematic[num1_y][num1_x].isdigit():
		num1 = num1 + schematic[num1_y][num1_x]
		num1_x += 1
		if num1_x == width:
			break
	while schematic[num2_y][num2_x].isdigit():
		num2 = num2 + schematic[num2_y][num2_x]
		num2_x += 1
		if num2_x == width:
			break

	# print(f'{num1}, {num2}')

	return int(num1) * int(num2)



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