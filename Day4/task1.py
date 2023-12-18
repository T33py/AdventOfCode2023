def main():
	i = read_input('input1.txt')
	cards = format_input(i)

	total_points = 0

	for id in cards:
		card = cards[id]
		score = calculate_points(card)
		total_points += score
		print(f'{id} = {score}')

	return total_points

def calculate_points(card):
	score = 0
	winning_numbers = card['winning_numbers']
	my_numbers = card['my_numbers']

	for number in winning_numbers:
		if number in my_numbers:
			if score == 0:
				score = 1
			else:
				score *= 2

	return score

def format_input(i:str):
	cards = {}
	
	for card in i.split('\n'):
		[_id, _numbers] = card.split(': ')
		id_lst = _id.split(' ')
		id = int(id_lst[len(id_lst)-1])
		numbers = _numbers.split(' | ')
		winning_numbers = [int(num) for num in numbers[0].split(' ') if num != '']
		my_numbers = [int(num) for num in numbers[1].split(' ') if num != '']
		cards[id] = { 'winning_numbers': winning_numbers, 'my_numbers': my_numbers}
		print(cards[id])

	return cards

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()