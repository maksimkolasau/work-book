guests_list = ['Natali', 'Helen', 'Uri', 'Luba', 'Ksenia', 'Ann']

guests_list[0] = 'Alexander'
guests_list.insert(0, 'Vasya')
guests_list.insert(4, 'Peter')
guests_list.append('Ivan')

print("I'm sorry but I can invite only 2 guests on my b-day!\n")
print(guests_list)

for guest in guests_list[-7:]:
	print(f"I'm so sorry, {guest}, for cancellation!")
	guests_list.pop()

for guest in guests_list:
	print(f"You are invited {guest}! :D")




