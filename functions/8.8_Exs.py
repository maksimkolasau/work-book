def make_album(musician_name, musician_album):
	album_info = {'musician': musician_name, 'album': musician_album}
	return album_info

while True:
	print('\nPlease tell me the info about musician and album: ')
	m_info = input("Musician: ")
	alb_info = input("Album: ")

	fmalbum = make_album(m_info, alb_info)
	print(f"You added: {fmalbum}")
	break