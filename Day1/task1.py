def main():
	i = read_input('input1.txt')
	# print(i)
	lines = format_input(i)

	calibration_values = []
	for line in lines:
		calibration_values.append(find_calibration_value(line))

	print(calibration_values)

	return sum(calibration_values)

def find_calibration_value(line:str):
	first_val = -1
	last_val = -1
	for char in line:
		if char.isdigit():
			if first_val == -1:
				first_val = char
			last_val = char
	return int(first_val + last_val)

def format_input(i:str):
	f = i.split('\n')
	return f

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()