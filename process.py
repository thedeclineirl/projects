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
filepath = 'source.csv'

def read_in(filename):
	#	open file, read in data
	#file = open(filename, encoding = "utf8")
	file = open(filename, 'r')
	data = [line.strip() for line in file]
	#print(data)
	return data	

def process(data):
	scrobbles = []
	linecount = 0
	for line in data:
		artist = line.split(',')[0]
		#if artist == 'The Arcade Fire':
		#	artist = 'Arcade Fire'

		album = line.split(',')[1]
		song = line.split(',')[2]
		datetime = line.split(',')[3]
		listen = scrobble(artist, album, song, datetime)
		scrobbles.append(listen)
		linecount+=1
	print("{0} lines processed".format(linecount))
	return scrobbles

def clean_artists(data):
	the_artists = {}
	for item in data:
		artist = item.get_artist()
		#print(artist)
		if artist.startswith('The'):
			if artist in the_artists:
				the_artists[artist] += 1
			else:
				the_artists[artist] = 1
	print("{0} artists starting with The".format(len(the_artists)))
	return the_artists

def the_artists_csv(dict):    
	csv_file = open('the_artists.csv', 'w')
	csv_file.write('Artist,Play Count\n')
	#dict = dict.sort()
	for key in dict:
		x = "{0},{1}\n".format(key,dict[key])
		csv_file.write(x)
	csv_file.close()

def count_by_artist(data):
	count = {}
	#TODO
	for item in data:
	artist = item.get_artist()
	if artist in the_artists:
		count[artist] += 1
	else:
		count[artist] = 1
	return count
	
def main():
	data = read_in(filepath)
	scrobbles = process(data)
	the_artists_csv(clean_artists(scrobbles))

main()