############################################################
# Module  : obj-recog/clar_tut.py
# Date    : May 26th 2017
# Author  : Xiao Ling
############################################################

import os

from clarifai import rest
from clarifai.rest import Image
from clarifai.rest import ClarifaiApp

from app import *

############################################################
'''
	Clarifai tutorial
'''
clar  = ClarifaiApp( app.get('APP-ID'), app.get('APP-SECRET'))
model = clar.models.get("general-v1.3")

# call by url
# m = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

# call by path
dev_root  = app.get('dev')
dev_paths = [ os.path.join(dev_root, p) for p in os.listdir(dev_root) if 'jpg' in p ]
dev_ims   = [ Image(file_obj = open(p, 'rb')) for p in dev_paths ]
preds     = [ model.predict([im]) for im in dev_ims ]

# get bag of words representation 
bag_of_words = []

for pred in preds:
	concepts = pred['outputs'][0]['data']['concepts']
	bow      = [c['name'] for c in concepts]
	bag_of_words.append(bow)



