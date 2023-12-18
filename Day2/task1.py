reds = 12
greens = 13
blues = 14


def main():
	i = read_input('input1.txt')
	games = format_input(i)

	possible_games = []
	for game in games.keys():
		possible = True
		for draw in games[game]:
			possible = possible and reds >= draw[0] and greens >= draw[1] and blues >= draw[2]
		if possible:
			possible_games.append(game)

	print(possible_games)
	return sum(possible_games)

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