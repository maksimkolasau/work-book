def make_album(musician_name, musician_album, number_of_tracks= ''):
	album_info = {'musician': musician_name, 'album': musician_album}
	if number_of_tracks:
		album_info['number_of_tracks'] = number_of_tracks
	return album_info

album = make_album('john', '1987')
album2 = make_album('max', '123123')
album3 = make_album('wef', 'qwdq ewef wef')
album4 = make_album('asd', 'asafdadfawd', '12')
print(album)
print(album2)
print(album3)
print(album4)
