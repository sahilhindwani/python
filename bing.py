#to do:
#check description not coming
#make a keyword for all the queries
#make atleast 5 queries
#make code more readable 

import urllib
import requests
from requests.auth import HTTPBasicAuth
from urllib import quote
import json
import webbrowser
import sys
API_KEY = "PYVolCI7EsUa7HwJRTlGUIfTg3nsS4nA3hO1TKpEUgI"

def bing_api(query,t):
	url = "https://api.datamarket.azure.com/Bing/Search/v1/Web"
	url += "?$format=json&$top="+str(t)+"&Query=%27{}%27".format(quote(query))
	r = requests.get(url, auth=("",API_KEY))
	resp = json.loads(r.text)
	return resp

while True:	
	try:
		q,i=raw_input(">>>").split()
		if q == 'open':
			new=2
			n=int(i)
			try:
				url=resp['d']['results'][n-1]['Url']
				webbrowser.open(url,new=new)
			except ValueError:
				print 'integer out of bound'
		elif q == 'desc':
			 n=int(i)
			 desc=resp['d']['results'][n-1]['Description']
			 print str(desc)
		elif q == 'exit':
			sys.exit();
		elif q == 'help':
			print "'open value':to open a link in a webbrowser"
			print "'desc value':to give a description of the given link"
			print "'exit --':to exit the program"
			print "'increase display_result':to increase the results of search"
			print "'query query_name':to search again the given query"

		elif q == 'increase':
			t=int(i)
			resp=bing_api(query,t)
			for i in range(t):
			        print str(i+1)+":-"+resp['d']['results'][i]['Url']
		elif q == 'query':
			query=raw_input("query>>>")
			resp=bing_api(query,20)
			for i in range(20):
				 print str(i+1)+":-"+resp['d']['results'][i]['Url']
		else:
			print 'invalid command for help type "help --"'

	except ValueError:
		print 'type help followed by integer for help'
