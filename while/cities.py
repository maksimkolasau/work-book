pro = "\nPlease enter the name of city you have visited (enter 'quit' when you are finished.): "

while True:
	city = input(pro)

	if city == 'quit':
		break
	else:
		print(f"You would love to go to {city.title()}!")