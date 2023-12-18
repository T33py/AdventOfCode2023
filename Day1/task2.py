spelled_out_digits = { 'one': 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9 }
valid_substrings = []

def main():
	build_valid_substrings()
	i = read_input('input2.txt')
	# print(i)
	lines = format_input(i)

	calibration_values = []
	for line in lines:
		calibration_values.append(find_calibration_value(line))

	print(calibration_values)

	return sum(calibration_values)

def find_calibration_value(line:str):
	_line = line
	letters = ''
	first_val = -1
	last_val = -1
	# find and replace spelled out digits
	for char in _line:
		letters += char
		if letters in valid_substrings:
			if letters in spelled_out_digits.keys():
				line = line.replace(letters, str(spelled_out_digits[letters]))
				letters = ''
		else:
			letters = char


	print(line)
	# solve for calibration value
	for char in line:
		if char.isdigit():
			if first_val == -1:
				first_val = char
			last_val = char
	return int(first_val + last_val)

def build_valid_substrings():
	for digit in spelled_out_digits.keys():
		substring = ''
		for letter in digit:
			substring += letter
			valid_substrings.append(substring)


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