## 
'''
---------------------------
Name:		Thomas Higgins
e-mail:		thomas.higgins.2@gmail.com
---------------------------
Created:	2020-02-18
Edited:		2020-02-18
---------------------------
'''

from scrobble import scrobble

#	Local Variables
filepath = '2020-01-27-lastfm_thedeclineirl.csv'

def read_in(filename):
	#	open file, read in data
	file = open(filename, encoding="utf8")
	data = [line.strip() for line in file]
	#print(data)
	return data	

def process(data):
	scrobbles = []
	linecount = 0
	for line in data:
		artist = line.split(',')[0]
		if artist == 'The Arcade Fire':
			artist = 'Arcade Fire'

		album = line.split(',')[1]
		song = line.split(',')[2]
		datetime = line.split(',')[3]
		listen = scrobble(artist, album, song, datetime)
		scrobbles.append(listen)
		linecount+=1
	print("{0} lines processed".format(linecount))
	return scrobbles

def clean(data):
	return False

data = read_in(filepath)
scrobbles = process(data)

