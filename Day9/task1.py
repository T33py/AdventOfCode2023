def main():
	i = read_input('input1.txt')
	sequences = format_input(i)

	derivatives = {}
	for seq in range(len(sequences)):
		derivatives[seq] = []

	# generate the derived sequences for each sequence
	for seq in range(len(sequences)):
		first_derivative = generate_derived_sequence(sequences[seq])
		derivatives[seq].append(first_derivative)
		current_derivative = first_derivative
		# while the current derivative isn't all zeroes we do a new derivative
		while not all_zeroes(current_derivative):
			new_derivative = generate_derived_sequence(current_derivative)
			derivatives[seq].append(new_derivative)
			current_derivative = new_derivative
		
	# for seq in derivatives:
	# 	print(f'{sequences[seq]}: {derivatives[seq]}')
	
	# extrapolate next number
	nexts = []
	for seq in range(len(sequences)):
		nxt = 0
		ds: list = derivatives[seq].copy()
		ds.reverse()
		for derivative in ds:
			nxt += derivative[len(derivative)-1]
		nxt += sequences[seq][len(sequences[seq])-1]
		nexts.append(nxt)
	
	print(nexts)
	

	return sum(nexts)

def generate_derived_sequence(sequence):
	derived = []
	last = sequence[0]
	for number in sequence[1:]:
		derived.append(number - last)
		last = number
	return derived

def all_zeroes(ls):
	for i in ls:
		if i != 0:
			return False
	return True

def format_input(i:str):
	seqs = i.split('\n')
	sequences = []
	for seq in seqs:
		sequence = [int(s) for s in seq.split(' ') if s != '']
		sequences.append(sequence)
	return sequences

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()