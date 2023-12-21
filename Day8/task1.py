def main():
	i = read_input('input1.txt')
	(steps, nodes) = format_input(i)
	print(steps)
	print(nodes)

	steps_taken = 0
	step_idx = 0
	current_node = 'AAA'
	while current_node != 'ZZZ':
		if steps[step_idx] == 'L':
			current_node = nodes[current_node][0]
		else:
			current_node = nodes[current_node][1]
		steps_taken += 1
		step_idx = (step_idx+1) % len(steps)
	print(current_node)
	return steps_taken

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