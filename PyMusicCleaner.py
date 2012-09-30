#!/usr/bin/python
# -*- coding: utf-8 -*

""" PyMusicCleaner takes info from last.fm,
	edits music tags and renames files and directories. """

import sys, os
import eyed3
import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm
API_KEY = "api_key"
API_SECRET = "api_secret"

username = "name"
password_hash = pylast.md5("password")

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
    API_SECRET, username = username, password_hash = password_hash)

def lister(root):
	"""Выводит список файлов в дереве каталогов с помощью os.walk"""
	for (thisdir, subshere, fileshere) in os.walk(root):
		print('[' + thisdir + ']')
		for fname in fileshere:
			if fname.endswith('.mp3'):
				path = os.path.join(thisdir, fname)
				# print(path)

				audiofile = eyed3.load(path)
				# print(audiofile.tag.artist)

				artist = network.get_artist(audiofile.tag.artist)

				print(artist.get_name())

if __name__ == '__main__':
	lister(sys.argv[1])