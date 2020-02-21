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

class scrobble:
	#Member Variables
	_artist = ''
	_album = ''
	_song = ''
	_datetime = ''

	def __init__(self, artist, album, song, datetime):
		self._artist = artist 
		self._album = album
		self._song = song
		self._datetime = datetime
	
	#Setters
		#NONE - scrobbles should not be changed after intialisation

	#Getters
	def get_artist(self):
		return self._artist

	def get_album(self):
		return self._album

	def get_song(self):
		return self._song

	def get_datetime(self):
		return self._datetime

		# String output for class item
	def __str__(self):
		return '"{0}","{1}","{2}","{3}"'.format(
			self._artist,self._album,self._song,self._datetime)