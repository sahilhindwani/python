#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import sys

class movie_rating:

	def __init__(self,name):
		self.movie_name=name

	def getrating(self):
		try:
			x=urllib2.urlopen('http://www.imdb.com/find?ref_=nv_sr_fn&q=%s&s=tt'%self.movie_name)
			html=x.read()
			soup=BeautifulSoup(html,'html.parser')
			count = 0
			z1=soup.find_all('td',class_='result_text')
			for z in z1:
				count=count+1
				new_url='http://www.imdb.com/%s'%z.a['href']
				y=urllib2.urlopen(new_url)
				#print "Server taking too much time..."
				html=y.read()
				soup=BeautifulSoup(html,'html.parser')
				movie_name=soup.find('div',class_='title_wrapper').h1.text
				z=soup.find('div',class_='ratingValue').strong.span.text
				return z
				if count == 5:
					break
			return 'null'
		except:
			return 'error'