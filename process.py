## 
'''
---------------------------
Name:		Thomas Higgins
e-mail:		thomas.higgins.2@gmail.com
---------------------------
Created:	2020-02-18
Edited:		2020-02-21
---------------------------
'''

from scrobble import scrobble

#	Local Variables
filepath = '2020-02.csv'

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
	corrected = 0
	for line in data:
		artist = line.split(',')[0]
		#Correct frequently misnamed artists
		result = artist_check(artist)
		artist = result[0]
		count = result[1]
		corrected = corrected + count
		album = line.split(',')[1]
		song = line.split(',')[2]
		datetime = line.split(',')[3]
		listen = scrobble(artist, album, song, datetime)
		scrobbles.append(listen)
		linecount+=1
	print("Processing completed:\n - {0} lines processed\n - {1} artist entries corrected".format(linecount,corrected))
	return scrobbles

def the_artists(data):
	#checks for artists beginning with "the"
	the_artists = {}
	for item in data:
		artist = item.get_artist()
		#print(artist)
		if artist.startswith('The') or artist.startswith('the'):
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

def full_export_csv(data):
	csv_file = open('all_the_artists.csv', 'w')
	csv_file.write('Artist,Album,Song,Datetime\n')
	for it in data:
		csv_file.write(str(it)+"\n")
	csv_file.close()
	print("Full export complete")

def count_by_artist(data):
	count = {}
	#TODO
	for item in data:
		artist = item.get_artist()
		if artist in count:
			count[artist] += 1
		else:
			count[artist] = 1
	return count
	
def artist_check(artist):
	# Rename commonly misnamed bands for a more acurate count
	count = 0
	if artist == 'The Arcade Fire':
		artist = 'Arcade Fire'
		count = 1
	elif artist == 'Flaming Lips':
		artist = 'The Flaming Lips'
		count = 1
	elif artist == 'At The Drive In':
		artist = 'At the Drive-In'
		count = 1

	#return artist at the end
	return artist,count

###############################################

def main():
	data = read_in(filepath)
	scrobbles = process(data)
	full_export_csv(scrobbles)
	#the_artists_csv(the_artists(scrobbles))



main()