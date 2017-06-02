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
try   : app
except: app = App()

############################################################
'''
	get assets
'''
paths   = app.module('face')
im_path = app.fetch('dev')
pics    = [ p for p in os.listdir(im_path) if 'face.jpg' in p ]

if pics:
	print('\n>> opening face from dev ')
	face_path = os.path.join(im_path, pics[0])


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


img = io.imread(face_path)

print('\n\t>> recognizing image ...')
dets    = detector(img, 1)

for k,d in enumerate(dets):
	print (k, d.left(), d.top(), d.right(), d.bottom())
	shape = shape_pred(img,d)


print('\n\t>> selecting sub part of image with face')
m = img[d.left():d.right(), d.top():d.bottom()]

# Note: frontal face detection works for frontal faces, but not otherwise
pic = Im.fromarray(m,'RGB')
pic.show()


































