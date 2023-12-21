def main():
	i = read_input('input1.txt')
	[time, distance] = format_input(i)

	print(f'{time} | {distance}')
	ways_to_win = find_ways_to_win(time, distance)

	return len(ways_to_win)

def find_ways_to_win(time, dist):
	wins = []
	for t in range(time):
		if t % 1000000 == 0:
			print(t)
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
	ts = [str(t) for t in times.split(':')[1].split(' ') if t != '']
	ds = [str(d) for d in dists.split(':')[1].split(' ') if d != '']
	
	return [int(''.join(ts)), int(''.join(ds))]

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()