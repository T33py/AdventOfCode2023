from functools import cmp_to_key

card_strengths = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
hand_strengths = ['5ok', '4ok', 'fh', '3ok', '2p', '1p', 'hc']
# reverse to get indexes to match gt/lt comparisons with hand/cardstrengths
card_strengths.reverse()
hand_strengths.reverse()


def main():
	i = read_input('input1.txt')
	formatted_hands = format_input(i)
	bids = {}
	hands = []
	for hand in formatted_hands:
		bids[hand[0]] = int(hand[1])
		hands.append(hand[0])

	# print(hands)
	# print(bids)

	sorted_hands = sort_hands(hands)
	# print(sorted_hands)
	winnings = []
	for i in range(len(sorted_hands)):
		winnings.append((i+1) * bids[sorted_hands[i]])
	# print(winnings)

	for hand in sorted_hands:
		print(f'{hand}: {hand_strength(hand)}')

	return sum(winnings)

def sort_hands(hands): # sort hands by ascending strength
	hands_by_str = {}
	for strength in hand_strengths:
		hands_by_str[strength] = []
	# print(hands_by_str)
	
	for hand in hands:
		# print(f'h: {hand}')
		hands_by_str[hand_strength(hand)].append(hand)

	print(hands_by_str)
	sorted_hands = []
	for hand_str in hands_by_str:
		hands_of_str:list = hands_by_str[hand_str]
		# print(f'{hand_str}: {hands_of_str}')
		if len(hands_of_str) > 1:
			hands_of_str = sorted(hands_of_str,key=cmp_to_key(by_best_card))
		sorted_hands.extend(hands_of_str)
			

	return sorted_hands

def by_best_card(hand1:str, hand2:str):
	# if hand1 is None or hand2 is None:
	# 	return 0
	for card in range(5):
		c1 = hand1[card]
		c2 = hand2[card]
		# print (f'cmp: {c1} and {c2}')
		if card_strengths.index(c1) < card_strengths.index(c2):
			return -1
		elif card_strengths.index(c1) > card_strengths.index(c2):
			return 1
	return 0

def hand_strength(cards):
	card_counts = {}
	J_count = 0
	max_count = 0 
	for card in cards:
		if not card in card_counts:
			card_counts[card] = 0
		card_counts[card] += 1
		if card_counts[card] > max_count and card != 'J':
			max_count = card_counts[card]
		if card == 'J':
			J_count += 1
	
	# print(f'max_count: {max_count}, j_count: {J_count}')
	max_count += J_count
	strength = ''
	if max_count == 1:
		strength = 'hc'
	elif max_count == 2: # pair => check whether 1 or 2 pair
		strength = '1p'
		ps = 0
		for card in card_counts:
			if card_counts[card] == 2:
				ps += 1
		if ps == 2: # 2 pairs
			strength = '2p'
	elif max_count == 3: # 3 of a kind is either 3ok or full house
		strength = '3ok'
		# possible patterns for fh
		#    22233
		#    22J33
		#    2JJ33
		# bad patterns for fh
		#    2J344
		if len(card_counts) == 2: # is 100% fh
			strength = 'fh'
		elif len(card_counts) == 3 and 'J' in card_counts: # Must be house since only 2 kinds thats not J exists
			strength = 'fh'
			
	elif max_count == 4:
		strength = '4ok'
	elif max_count == 5:
		strength = '5ok'
	
	return strength

def format_input(i:str):
	ls = i.split('\n')
	hands = []
	for h in ls:
		hands.append(h.split(' '))

	return hands

def read_input(file: str):
	i = ''
	with open(file, 'r') as f:
		i = f.read()
	return i

if __name__ == '__main__':
	main()