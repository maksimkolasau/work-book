def sandwich_comps(sandwich_name, *components):
	print(f"Making a {sandwich_name} with the following toppings:")
	for component in components:
		print(component)

sandwich_comps('cheese', 'pepr', 'wregerg')
sandwich_comps('KRISPY', 'ice', 'gsefs')