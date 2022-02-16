age = int(input("\nPlease enter your age: "))

if age < 3:
	print("Free entry for babies <3")
elif age >= 3 and age <= 12:
	print("Price for ticket is $10")
elif age > 12:
	print("Price for ticket is $15")


