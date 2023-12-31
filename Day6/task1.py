def main():
	i = read_input('input1.txt')
	[times, distances] = format_input(i)

	possible_wins = []
	for race in range(len(times)):
		ways_to_win = find_ways_to_win(times[race], distances[race])
		possible_wins.append(len(ways_to_win))
		print(f'race {race} has wins: {ways_to_win}')

	return product(possible_wins)

def find_ways_to_win(time, dist):
	wins = []
	for t in range(time):
		my_dist = t * (time - t)
		if (my_dist > dist):
			wins.append(my_dist)
	return wins

def product(ls:list):
	prod = 1
	for n in ls:
		prod *= n
	return prod

def format_input(i:str):
	[times, dists] = i.split('\n')
	ts = [int(t) for t in times.split(':')[1].split(' ') if t != '']
	ds = [int(d) for d in dists.split(':')[1].split(' ') if d != '']
	return [ts, ds]

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()