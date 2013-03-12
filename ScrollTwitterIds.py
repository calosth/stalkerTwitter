#!/usr/bin/env python
import urllib2
import simplejson as json

for user in range(100):
	print "User Number: %s"  %user
	try: 
		URL = "http://api.twitter.com/1/users/show.json?user_id=%s&include_entities=true" %user
		f = urllib2.urlopen(URL)
		list_fancy = json.loads( f.read() )

		print list_fancy['error']

		print "Name:       %s" %list_fancy['name']
		print "User:       @%s" %list_fancy['screen_name']
		print "Created at: %s" %list_fancy['created_at']
		f.close
	except:
		print "I don't know what do"
	print "====================================================="
