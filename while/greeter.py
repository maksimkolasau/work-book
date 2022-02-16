name1 = input("Please, enter your name: ")
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your last name? "

name = input(prompt)
print(f"Hello, {name1.title()} {name.title()}!")
