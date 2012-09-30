#!/usr/bin/python
# -*- coding: utf-8 -*

"""PyMusicCleaner"""

import sys, os
import eyed3

def lister(root):
	"""Выводит список файлов в дереве каталогов с помощью os.walk"""
	for (thisdir, subshere, fileshere) in os.walk(root):
		print('[' + thisdir + ']')
		for fname in fileshere:
			if fname.endswith('.mp3'):
				path = os.path.join(thisdir, fname)
				# print(path)

				audiofile = eyed3.load(path)
				print(audiofile.tag.artist)

if __name__ == '__main__':
	lister(sys.argv[1])