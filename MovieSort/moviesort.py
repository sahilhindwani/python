#!/usr/bin/env python

import os
import sys
from sort_with_movie import *
from imdbmovie import *
#import movieratings


if len(sys.argv) < 2:
	print 'Usage:./sort_with_movie Directory_path'
	sys.exit()

if not os.path.exists('Movies'):
	os.mkdir('Movies')

os.chdir(sys.argv[1])
li=os.listdir(sys.argv[1])
#f=open('extensionlist.txt')
extensions=['.3gp','.avi','.mkv','.mp4','.flv','.mp4','.mpeg','.mpg']#f.read.split(',')
x=sorting(sys.argv[1])
for file in li:
		nname = x.newname(file)
		if nname != file:
			x.rename(file,nname)

