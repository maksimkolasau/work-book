requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinishing making pizza!")
else:
	print("Are you sure you want plain pizza?")