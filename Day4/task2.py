def main():
	i = read_input('input1.txt')
	card_table = format_input(i)

	cards = []

	for id in card_table:
		if len(cards) < id:
			cards.append(0)
		# index of the current card
		idx = id-1
		# we have at least 1
		cards[idx] += 1
		card = card_table[id]
		score = calculate_matches(card)
		# we want to increment the counters "score" with the number of the current card
		for i in range(score):
			more_cards_idx = idx + i + 1
			while len(cards) < more_cards_idx +1:
				cards.append(0)
			cards[more_cards_idx] += cards[idx]

	print(cards)
	return sum(cards)

def calculate_matches(card):
	count = 0
	winning_numbers = card['winning_numbers']
	my_numbers = card['my_numbers']

	for number in winning_numbers:
		if number in my_numbers:
			count += 1

	return count

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

	return cards

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()