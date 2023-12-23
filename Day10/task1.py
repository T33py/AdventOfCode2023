# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes.
big_int = 9999999999999999

def main():
	i = read_input('input1.txt')
	grid = format_input(i)

	connections = {}
	(sx, sy) = find_s(grid)
	s_choord_str = str_choords((sx, sy))
	print(f'S: {s_choord_str}')
	
	# walk around the loop in one direction to get a map of all the choordinates
	current_connected = get_s_connected(grid, (sx, sy))
	connections[s_choord_str] = current_connected
	print(current_connected)

	lst = s_choord_str
	nxt = current_connected[0]
	nxt_choord_str = str_choords(nxt)
	while nxt_choord_str != s_choord_str:
		current_coordinates = nxt
		current_connected = get_connecting_pipes(grid, current_coordinates)
		current_coordinates_str = str_choords(current_coordinates)
		connections[current_coordinates_str] = current_connected
		if str_choords(current_connected[0]) == lst:
			nxt = current_connected[1]
		else:
			nxt = current_connected[0]
		nxt_choord_str = str_choords(nxt)
		lst = current_coordinates_str
	
	# for c in connections:
	# 	print(f'{c}: {connections[c]}')

	# do task 1
	dists = {}
	for spot in connections:
		dists[spot] = big_int
	dists[s_choord_str] = 0

	# follow the loop
	for spot in connections:
		update_dists(dists, connections, spot)

	# go back along the loop to get the other direction
	for spot in connections.keys().__reversed__():
		update_dists(dists, connections, spot)
	
	print(dists)
			

	return max(dists.values())

def update_dists(dists, conns, spot):
	n1 = str_choords(conns[spot][0])
	n2 = str_choords(conns[spot][1])
	
	if dists[spot] < dists[n1]:
		dists[n1] = dists[spot] + 1
	if dists[spot] < dists[n2]:
		dists[n2] = dists[spot] + 1
	return

def get_s_connected(grid, choordinates):
	(x, y) = choordinates
	connected = []
	print(grid[x+1][y])
	if grid[x-1][y] in ['-', 'F', 'L']:
		connected.append((x-1, y))
	if grid[x+1][y] in ['-', '7', 'J']:
		connected.append((x+1, y))
	
	if grid[x][y-1] in ['|', 'J', 'L']:
		connected.append((x, y-1))
	if grid[x][y+1] in ['|', 'F', '7']:
		connected.append((x, y+1))
	return connected

def get_connecting_pipes(grid, choordinates):
	(x, y) = choordinates
	pipe = grid[x][y]
	connected = []
	if pipe == '|':
		connected = [(x, y+1), (x, y-1)]
	elif pipe == '-':
		connected = [(x+1, y), (x-1, y)]
	elif pipe == 'L':
		connected = [(x+1, y), (x, y+1)]
	elif pipe == 'J':
		connected = [(x-1, y), (x, y+1)]
	elif pipe == '7':
		connected = [(x-1, y), (x, y-1)]
	elif pipe == 'F':
		connected = [(x+1, y), (x, y-1)]

	return connected

def str_choords(choords):
	(x, y) = choords
	return f'({x}, {y})'

def find_s(grid):
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] == 'S':
				return (x, y)
	return None

def format_input(i:str):
	rows = i.split('\n')
	rows.reverse()
	grid = [[] for c in range(len(rows[0]))]
	for row in rows:
		for col in range(len(grid)):
			grid[col].append(row[col])
	return grid

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()