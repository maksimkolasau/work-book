alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25

alien_0['color'] = 'red'  # izmenyaem znachenie v slovare
# print(alien_0['color'])
# print(alien_0['points'])

print(alien_0)
# alien_01_________________________________________________________________________________________________
alien_01 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_01['x_position']}")
alien_01['speed'] = 'fast'
# prishelec peremeshaetsya v pravo
# vychislyaem velichiny smesheniya na osnovanii tekyshei skorosti
if alien_01['speed'] == 'slow':
	x_increment = 1
elif alien_01['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3  # prishelec dvigaetsya bystro
# novaya poziciya ravna symme staroi pozicii i prirasheniya
alien_01['x_position'] = alien_01['x_position'] + x_increment
print(f"New position: {alien_01['x_position']}")

del alien_01['y_position']

print(alien_01)