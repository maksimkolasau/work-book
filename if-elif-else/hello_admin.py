users = []
# ['maks', 'admin', 'jaden', 'igor']
for user in users:
		if user == 'admin':
			print(f"Hello, {user.title()}, would you like to see a status report?")
		else:
			print(f"Hello, {user.title()}.")

if users:
	print("We have users!")
else:
	print("We need to invite some users!")

# 2____________________________________________________________________________________________________

current_users = ['maks', 'admin', 'jaden', 'igor', 'petya']
new_users = ['vasya', 'luba', 'Jaden', 'kostya', 'helen']

for user1 in new_users:
	if user1.lower() in current_users:
		print(f"{user1} is not available! Try to create something else")
	else:
		print(f"You can try {user1}")