############################################################
# Module  : scrape/top
# Date    : 05/28/2017
# source  : https://github.com/scoliann/TinderFaceScraper
############################################################

import json
import sys
import urllib
import pickle
import requests
from urllib2 import urlopen

import os, os.path
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from app import *

def waitABit(minTime, maxTime):
	wait = random.uniform(minTime, maxTime)
	print("WAIT: " + str(wait) + "\n")
	time.sleep(wait)

def tinderAPI_get_xAuthToken(facebook_token, facebook_id):

	loginCredentials = {'facebook_token': facebook_token, 'facebook_id': facebook_id}
	headers = {'Content-Type': 'application/json', 'User-Agent': 'Tinder Android Version 3.2.0'}

	r = requests.post('https://api.gotinder.com/auth', data=json.dumps(loginCredentials), headers=headers)
	r = r.json()

	if 'token' in r:
		x_auth_token = r['token']
		return x_auth_token
	else:
		raise NameError("Error: " + r['error'])

def tinderAPI_getSubjectList(x_auth_token):

	# Get a list of subjects
	headers2 = {'User-Agent': 'Tinder Android Version 3.2.0', 'Content-Type': 'application/json', 'X-Auth-Token': x_auth_token}
	r2       = requests.get('https://api.gotinder.com/user/recs', headers=headers2)
	r2       = r2.json()

	if 'results' in r2:
		subjects = r2['results']
		return subjects
	else:
		raise NameError("Error: " + str(r2))

def tinderAPI_passSubject(subject, x_auth_token):
	_id      = subject['_id']
	headers3 = {'X-Auth-Token': x_auth_token, 'User-Agent': 'Tinder Android Version 3.2.0'}
	r3       = requests.get('https://api.gotinder.com/pass/' + _id, headers=headers3)


'''
	@Use: load all pictures and save meta data
'''
def scrape_person(out_root, person):

	out_dir = ping_dir( os.path.join(out_root, person['name']), person['_id'], 1 )

	if out_dir:

		os.mkdir(out_dir)

		im_id = 1

		print('\n\t>> loading data for ' + person['name'])

		for m in person['photos']:
			url = m['url']
			out_path = os.path.join(out_dir, 'photo-' + str(im_id) + '.jpg')
			urllib.urlretrieve( url, out_path )
			im_id += 1 

		out = { k : v for k,v in person.iteritems() \
		        if k not in ['photos']              }

		out_path = os.path.join(out_dir, 'meta.pkl')

		with open(out_path, 'wb') as h:
			pickle.dump(out,h)
	else:
		print('\n\t>> already found user: ' + person['name'])


'''
	@Use: ping directory to see if path exists, if yes
	      increment up
'''
def ping_dir(stem, pid, incr):

	out_dir = stem + '-' + str(incr)

	if os.path.exists(out_dir):
		'''
			check if we already found this person
		'''
		meta_path = os.path.join(out_dir, 'meta.pkl')

		# person has meta-file, check this person
		if os.path.exists(meta_path):
			with open(meta_path, 'rb') as h:
				meta = pickle.load(h)

			# already found person, skip
			if meta['_id'] == pid:
				return ''

			# new person with same name, recurse
			else:
				return ping_dir(stem, pid, incr + 1)

		# person has no meta-file, assume we have a new person
		else:
			return ping_dir(stem, pid, incr + 1)
	else:
		return out_dir


def getPics(x_auth_token, imagePath):

	# Get list of subjects
	subjects = tinderAPI_getSubjectList(x_auth_token)

	# Iterate through list of subjects
	for subject in subjects:

		scrape_person(imagePath, subject)
		
		# Wait some random amount of time and then pass the subject
		waitABit(0.5, 2.0)
		
		# Pass the subject
		tinderAPI_passSubject(subject, x_auth_token)


def exec_tinder(facebook_token, facebook_id, imagePath):

	# Log into Tinder
	x_auth_token = tinderAPI_get_xAuthToken(facebook_token, facebook_id)

	# Get pics
	for i in range(10000):

		# Print current iteration to terminal
		print("\n\t>> Potential Match Batch: " + str(i + 1))

		# Get one collection of subjects and their pictures
		getPics(x_auth_token, imagePath)

		# Wait a bit
		waitABit(0.25 * 60, 0.5 * 60)






