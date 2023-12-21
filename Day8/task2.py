from math import lcm
def main():
	i = read_input('input1.txt')
	(steps, nodes) = format_input(i)
	# print(steps)
	# print(nodes)

	steps_taken = 0
	step_idx = 0
	starting_nodes = find_a_nodes(nodes)
	current_nodes = starting_nodes.copy()
	cycle_lens = [0 for n in starting_nodes]
	cycles_found = [False for n in starting_nodes]
	print(current_nodes)

	# find the length of each cycle
	while not all_found(cycles_found):
		for node_idx in range(len(current_nodes)):
			node = current_nodes[node_idx]
			if steps[step_idx] == 'L':
				node = nodes[node][0]
			else:
				node = nodes[node][1]
			current_nodes[node_idx] = node
			if not cycles_found[node_idx]:
				if node[2] == 'Z':
					cycle_lens[node_idx] = steps_taken + 1
					cycles_found[node_idx] = True
		steps_taken += 1
		step_idx = (step_idx+1) % len(steps)
		
	print(cycle_lens)

	# walk(steps, nodes, 17141*16579)
	lowest_common_multiple = 1
	for i in range(len(cycle_lens)):
		lowest_common_multiple = lcm(lowest_common_multiple, cycle_lens[i])
	return lowest_common_multiple

def find_a_nodes(nodes):
	a_nodes = []
	for node in nodes:
		if 'A' == node[2]:
			a_nodes.append(node)
	return a_nodes

def all_found(found):
	for b in found:
		if not b:
			return False
	return True

def format_input(i:str):
	s_input = i.split('\n')
	steps = s_input[0]
	node_strs = s_input[2:]
	_nodes = [node.split(',') for node in node_strs]
	nodes = {}
	for node in _nodes:
		nodes[node[0]] = node[1:]
	return (steps, nodes)

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
		i = i.replace('(', '').replace(')', '').replace('=', ',').replace(' ', '')
	return i

if __name__ == '__main__':
	main()