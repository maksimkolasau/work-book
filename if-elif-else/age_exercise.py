age = int(input())

if age < 2:
	print("Small Baby")
elif age >= 2 and age < 4:
	print("Baby")
elif age >= 4 and age < 13:
	print("Child")
elif age >= 13 and age < 20:
	print("Teenager")
elif age >= 20 and age < 65:
	print("Adult")
elif age >= 65:
	print("Old")