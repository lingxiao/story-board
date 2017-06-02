############################################################
# Module  : face/top
# Date    : 05/28/2017
# Author  : Xiao Ling
# source  : installing dlib w/o conda:
#                http://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/
#           installing using conda:
# 				 conda install -c conda-forge dlib=19.4
############################################################


import os

import sys
import dlib
from skimage import io
import numpy as np
import pickle
from PIL import Image as Im

from app import *

############################################################
'''
	make current directory
'''
app    = App()
paths  = app.module('face')
im_dir = app.fetch ('tinder-female/Abby-1')

############################################################
'''
	get assets
'''
data_paths = [ os.path.join(im_dir, p) for p in os.listdir(im_dir) ]
meta_path  = [ p for p in data_paths if 'meta' in p ]
im_paths   = [ p for p in data_paths if '.jp' in p  ]

if meta_path:
	with open(meta_path[0], 'rb') as h:
		meta = pickle.load(h)

print('\n>> opening face for user: ' + meta['name'])

############################################################
'''
	get all models we need:
		- detector to find faces
		- shape predictor to find face landmarks
		- face regoncition model
'''
model_root            = app.fetch('assets/dlib')
predictor_path        = os.path.join( model_root, 'shape_predictor_68_face_landmarks.dat' )
face_recog_model_path = os.path.join( model_root, 'face_recognition_resnet_model_v1.dat'  )

try:
	detector
except:	
	print('\n\t>> loading pre-trained image models')
	if os.path.exists(predictor_path) \
	   and  os.path.exists(face_recog_model_path):
			detector   = dlib.get_frontal_face_detector()
			shape_pred = dlib.shape_predictor(predictor_path)   
			face_recog = dlib.face_recognition_model_v1(face_recog_model_path)
	else:
		raise NameError('Cannot find path:\n\t>> '  \
			           + predictor_path + '\n\t>> ' \
			           + face_recog_model_path      )	


faces = dict()

for im_path in im_paths:

	img = io.imread(im_path)

	print('\n\t>> recognizing image ...')
	dets = detector(img, 1)

	print("\n\t>> Number of faces detected: {}".format(len(dets)))

	for k,d in enumerate(dets):

		print("\n\t>> Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
	            k, d.left(), d.top(), d.right(), d.bottom()))

		lft  = max(d.left()  , 0)
		rt   = max(d.right() , 0)
		tp   = max(d.top()   , 0)
		bot  = max(d.bottom(), 0)

		shape = shape_pred(img,d)

		print('\n\t>> selecting sub part of image with face')
		face = img[lft:rt, tp:bot]

		pic      = Im.fromarray(img , 'RGB')
		pic_crop = Im.fromarray(face, 'RGB')
		pic.show()
		pic_crop.show()

		print('\n\t>> computing face representation')
		phi_face = face_recog.compute_face_descriptor(img, shape)

