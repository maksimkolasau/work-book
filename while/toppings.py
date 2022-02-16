cl_topping = "\n( введите 'жирнюка' чтобы закончить оформление заказа)"
cl_topping += "\nДобавьте топпинг к пицце: "

ctl = []

while True:
	message = input(cl_topping)

	if message == 'жирнюка':
		print("Добавленные топпинги: ")
		for t in ctl:
			print(f"\t{t.title()}")
		break

	else:
		ctl.append(message)
		for t2 in ctl:
			print(f"Вы добавили: {t2.title()}")
print("Ваша пицца никогда не будет готова... лоооооооол")
