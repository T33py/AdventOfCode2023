def main():
	i = read_input('input2.txt')
	games = format_input(i)

	powers_of_games = []
	for game in games:
		min_r = 0
		min_g = 0
		min_b = 0
		for draw in game:
			if draw[0] > min_r:
				min_r = draw[0]
			if draw[1] > min_g:
				min_g = draw[1]
			if draw[2] > min_b:
				min_b = draw[2]
		powers_of_games.append(min_r * min_g * min_b)
	print(powers_of_games)
	return sum(powers_of_games)

def format_input(i:str):
	games = {}
	for game in i.split('\n'):
		[_id, _ds] = game.split(': ')
		id = int(_id.split(' ')[1])
		# print(id)
		_draws = _ds.split('; ')
		draws = []
		for draw in _draws:
			red = 0
			green = 0
			blue = 0
			cubes = draw.split(', ')
			# print(cubes)
			for color in cubes:
				if 'red' in color:
					red = int(color.split(' ')[0])
				elif 'green' in color:
					green = int(color.split(' ')[0])
				elif 'blue' in color:
					blue = int(color.split(' ')[0])
			draws.append([red, green, blue])

		games[id] = draws

	return games

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()