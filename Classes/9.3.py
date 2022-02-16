class User():
	def __init__(self, first_name, last_name, nickname, age):
		self.first_name = first_name
		self.last_name = last_name
		self.nickname = nickname
		self.age = age
		self.login_attempts = 0
		self.full_name = f"{self.first_name} {self.last_name}"

	def describe_user(self):
		print(f"{self.full_name} with nick name {self.nickname} is {self.age} years old!")


	def greet_user(self):
		print(f"Hello, {self.full_name}! Glad to see you!")


	def increment_login_attempts(self):
		self.login_attempts += 1


	def read_attempts(self):
		print(f"User {self.nickname} loged in {self.login_attempts} times.")


	def reset_login_attempts(self):
		self.login_attempts = 0

maksim = User('Maksim', 'Kolasau', 'kolasau88', 31)
luba = User('Liubou', 'Dzemskaya', 'applewithlove', 26)

maksim.describe_user()
maksim.greet_user()
luba.describe_user()
luba.greet_user()

user1 = User('user1', 'userski', 'user123', 20)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.read_attempts()
user1.reset_login_attempts()
user1.read_attempts()