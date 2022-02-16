	my_foods = ['pizza', 'falafel', 'carrot cake']
	friend_foods = my_foods[:]
	my_foods.append('cannoli')
	friend_foods.append('ice cream')

	print("My favorite foods are:")
	print(my_foods)

	print("\nMy friend's favorite foods are:")
	print(friend_foods)

	print("\nThe first three items in the list are:")
	print(my_foods[:3])

	print("\nTwo items from the middle of the list are:")
	print(my_foods[1:3])

	print("\nThe last three items in the list are:")
	print(my_foods[-3:])

	for my_food in my_foods:
		print(my_food.title())
	print('\n')
	for friend_food in friend_foods:
		print(friend_food.title())