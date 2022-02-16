file = 'learning_python.txt'
with open(file) as learning:
	contents = learning.read()

contents = contents.replace('Python', 'Food')

print(contents)
print(contents)
print(contents)