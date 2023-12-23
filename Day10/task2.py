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
	i = read_input('ex5.txt')
	grid = format_input(i)

	connections = {}
	(sx, sy) = find_s(grid)
	s_choord_str = str_choords((sx, sy))
	print(f'S: {s_choord_str}')
	
	# walk around the loop in one direction to get a map of all the choordinates
	current_connected = get_s_connected(grid, (sx, sy))
	connections[s_choord_str] = current_connected
	# print(current_connected)

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
	
	# do task2 
	# we gradually expand areas outside the circle untill only the areas inside remain
	#  0 not inside circle
	#  1 inside circle
	#  2 circle
	print('setup encircled')
	encircled = grid.copy()
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			# assume encircled until proven outside the circle
			encircled[x][y] = 1

	print('mark 100%')
	# mark everything we know 100%
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			choords = (x, y)
			c_str = str_choords(choords)
			# all pipes in the circle count as outside the circle
			if c_str in connections:
				encircled[x][y] = 2
			# all pipes at the edges are by default either cirlcle or outside
			if x == 0 or x == len(grid)-1:
				encircled[x][y] = 0
			elif y == 0 or y == len(grid[x])-1:
				encircled[x][y] = 0

	print('do expansion')
	lst_inside = 1
	inside = 0
	# since all things outside the circle must be next to something else outside the circle 
	#  we keep expanding untill nothing new is marked as outside the circle
	while lst_inside != inside:
		lst_inside = inside
		inside = 0
		for x in range(len(encircled)):
			for y in range(len(encircled[x])):
				# if we know its not encircled -> skip
				if encircled[x][y] == 0:
					continue
				(neighbours, n_coordinates) = get_neighbours(encircled, (x, y))
				# if a neighbour is outside this cant be inside
				if 0 in neighbours and encircled[x][y] != 2: 
					encircled[x][y] = 0
				# if this might allow squeezing
				# if 2 in neighbours:
				# 	allows_squeezing_to((x, y), encircled, connections, neighbours, n_coordinates)
				if encircled[x][y] == 1:
					inside += 1
	
	print('print encircled')
	for y in range(len(grid[x])-1, -1, -1):
		row = ''
		for x in range(len(grid)):
			row = row + ' ' + str(encircled[x][y])
		print(row)

	return inside

def allows_squeezing_to(spot, grid, connections, neighbours, n_coordinates):
	(x, y) = spot
	check_squeeze = []
	for n in range(len(neighbours)):
		if neighbours[n] == 2:
			check_squeeze.append(n_coordinates[n])

	


	return

def get_neighbours(grid, spot):
	(x, y) = spot
	neighbours = []
	coordinates = []
	if y > 0:
		neighbours.append(grid[x][y-1])
		coordinates.append((x,y-1))
		if x > 0:
			neighbours.append(grid[x-1][y-1])
			coordinates.append((x-1,y-1))
		if x < len(grid)-1:
			neighbours.append(grid[x+1][y-1])
			coordinates.append((x+1,y-1))
	
	if x > 0:
		neighbours.append(grid[x-1][y])
		coordinates.append((x-1,y))
	if x < len(grid)-1:
		neighbours.append(grid[x+1][y])
		coordinates.append((x+1,y))
	
	if y < len(grid[x])-1:
		neighbours.append(grid[x][y+1])
		coordinates.append((x,y+1))
		if x > 0:
			neighbours.append(grid[x-1][y+1])
			coordinates.append((x-1,y+1))
		if x < len(grid)-1:
			neighbours.append(grid[x+1][y+1])
			coordinates.append((x+1,y+1))

	return (neighbours, coordinates)

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