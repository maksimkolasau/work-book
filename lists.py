bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[2].title()}."
print(message)

names = ['pasha', 'vasya', 'ivan', 'petya', 'denis',]
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(f"Hello, {names[0].title()}!")
print(f"Hello, {names[1].title()}!")
print(f"Hello, {names[2].title()}!")
print(f"Hello, {names[3].title()}!")
print(f"Hello, {names[4].title()}!")

print('\n')

cars = ['honda', 'mercedes', 'bmw', 'opel', 'gmc', 'porshe']
cars[5] = 'ferrari'
print(f'I would like to buy a {cars[5].title()} car!')

print('\n')

motorcycles = []
motorcycles.append('honda')
print(motorcycles[0].title())
# na kakoe mesto   v
motorcycles.insert(1, 'ducati')
print(motorcycles)

# how to delete element from list
del motorcycles[0]
print(motorcycles)

print('\n')

# pop() ydalyaet posledni element iz spiska
popped_moto = motorcycles.pop()
print(motorcycles)
print(popped_moto)

print('\n')
# pop(2) ydalyaet konkretnyi element iz spiska
motorcycles.append('honda')
motorcycles.append('ducati')
motorcycles.append('bmw')

first_owned = motorcycles.pop(0)
print(f'The first owned moto was a {first_owned.title()}.')

print('\n')

# remove() metod
list2_moto = ['honda', 'ducati', 'yamaha', 'suzuki']
print(list2_moto)
too_exp = 'yamaha'
list2_moto.remove(too_exp)
print(list2_moto)
print(f"\n{too_exp.title()} is too expensive for me! :(")

