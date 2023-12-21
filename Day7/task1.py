def main():
	i = read_input('ex1.txt')
	formatted_input = format_input(i)

	return 0

def format_input(i:str):
	f = []
	return f

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()