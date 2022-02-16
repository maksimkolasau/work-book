from random import choice

lottery_numbers = (2, 5, 10, 3, 7, 8, 9, 6, 11, 1, 'b', 'c', 'a', 'd')
winner = []
winner.append(choice(lottery_numbers))
winner.append(choice(lottery_numbers))
winner.append(choice(lottery_numbers))
winner.append(choice(lottery_numbers))

print(f"This number {winner} is a winner in annual lottery game! Congratulations!")