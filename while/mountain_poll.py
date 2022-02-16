
responses = {}

# установка флага продолжения опроса
polling_active = True

while polling_active:
	# запрос имени и ответа пользователя
	name = input("\nWhat is your name? ")
	response = input("Which mountain you would like to climb someday? ")

	# ответ сохраняется в словаре
	responses[name] = response

	# проверка продолжения опроса
	repeat = input("Would you like to let another person respond? ( yes/no ) ")
	if repeat == 'no':
		polling_active = False

# опрос завершен, вывести результаты.
print("\n--- Poll Results---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}")