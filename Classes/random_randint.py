from random import randint, choice

print(randint(1, 6))

players = ['vasya', 'maks', 'fillip', 'yan', 'kostya', 'pasha']

who_will_win_the_random_game = choice(players)
print(who_will_win_the_random_game)