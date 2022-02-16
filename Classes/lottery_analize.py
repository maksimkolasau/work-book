from random import choice

lottery_numbers = (7, 'a', 8, 't', '3', 12, 1, 'e', 4)
my_ticket = ['a', 'e', 1, 4]
count = 0

while True:
	winner = []
	winner.append(choice(lottery_numbers))
	winner.append(choice(lottery_numbers))
	winner.append(choice(lottery_numbers))
	winner.append(choice(lottery_numbers))

	if winner == my_ticket:
		print(f"Your ticket number {my_ticket} = lottery number {winner}! You won!")
		break
	else:
		count += 1
		print(f"You had {count} tries! It's {winner}, not your ticket!")
