import requests
import json
import sys
import urllib.request
import os, os.path
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
For this script to run, the following must be specified, and the user must create an "imagePath" folder for the photos to be saved to.
'''

facebook_token = ''	# Refer to README.md for how to get token
facebook_id = ''	# Refer to README.md for how to get facebook ID
imagePath = ''		# Name of folder images save to 


def waitABit(minTime, maxTime):
	wait = random.uniform(minTime, maxTime)
	print("WAIT: " + str(wait) + "\n")
	time.sleep(wait)


def tinderAPI_get_xAuthToken(facebook_token, facebook_id):

	loginCredentials = {'facebook_token': facebook_token, 'facebook_id': facebook_id}
	headers = {'Content-Type': 'application/json', 'User-Agent': 'Tinder Android Version 3.2.0'}

	r = requests.post('https://api.gotinder.com/auth', data=json.dumps(loginCredentials), headers=headers)
	x_auth_token = r.json()['token']

	return x_auth_token


def tinderAPI_getSubjectList(x_auth_token):

	# Get a list of subjects
	headers2 = {'User-Agent': 'Tinder Android Version 3.2.0', 'Content-Type': 'application/json', 'X-Auth-Token': x_auth_token}
	r2 = requests.get('https://api.gotinder.com/user/recs', headers=headers2)
	subjects = r2.json()['results']

	# Return list of subjects
	return subjects


def tinderAPI_passSubject(subject, x_auth_token):
	_id = subject['_id']
	headers3 = {'X-Auth-Token': x_auth_token, 'User-Agent': 'Tinder Android Version 3.2.0'}
	r3 = requests.get('https://api.gotinder.com/pass/' + _id, headers=headers3)


def getPics(x_auth_token):

	# Get list of subjects
	subjects = tinderAPI_getSubjectList(x_auth_token)

	# Get the number of photos in directory
	processed_numPhotos = len([f for f in os.listdir(imagePath) if os.path.isfile(os.path.join(imagePath, f))])

	# Iterate through list of subjects
	for subject in subjects:
		
		# Get the subject ID
		sid = subject['_id']
		
		# Gets a list of pictures of the subject
		pictures = subject['photos']

		# Iterate through and save the pictures of the subject
		for picIndex in range(len(pictures)):

			# Get the URL for the largest cropped photo
			processed_picURL = str(pictures[picIndex]['processedFiles'][0]['url'])

			# Get the photo and save
			urllib.request.urlretrieve(processed_picURL, imagePath + '/' + sid + '_' + str(processed_numPhotos) + '.jpg')
			processed_numPhotos += 1

		# Wait some random amount of time and then pass the subject
		waitABit(0.5, 2.0)
		
		# Pass the subject
		tinderAPI_passSubject(subject, x_auth_token)


if __name__ == '__main__':

	# Log into Tinder
	x_auth_token = tinderAPI_get_xAuthToken(facebook_token, facebook_id)

	# Get pics
	for i in range(10000):

		# Print current iteration to terminal
		print("Potential Match Batch: ",str(i + 1))

		# Get one collection of subjects and their pictures
		getPics(x_auth_token)

		# Wait a bit
		waitABit(0.25 * 60, 0.5 * 60)









	

