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

class Admin(User):

	def __init__(self, first_name, last_name, nickname, age):
		super().__init__(first_name, last_name, nickname, age)
		self.privileges = Privileges(privs=['allowed add messages', 'allowed delete users', 'allowed ban users'])


class Privileges():

	def __init__(self, privs):
		self.privs = privs


	def show_privileges(self):
		print(f"Admins have the following privileges:")
		for privilege in self.privs:
			print(privilege)



