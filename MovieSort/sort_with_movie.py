#!/usr/bin/env python
import os
import shutil
from imdbmovie import *
import sys

class sorting:
	def __init__(self,direct):
		self.path_name=direct

	def rename(self,oldname,newname):
		try:
			shutil.move(oldname,'Movies/%s'%newname)
		except:
			print "Problem with moving%s.Make sure you specify the correct directory"%oldname

	def newname(self,name):
		movie=movie_rating(name)
		rating = movie.getrating()
		if rating  == 'null':
			print "The %s can't be found.Make sure the movie name is correct"%name
			return name
		elif rating == 'error':
			print "error"
			return name
		else:
			new_name=str(rating)+'\n'+name
			return new_name
	




