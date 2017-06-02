############################################################
# Module  : face/top
# Date    : 05/28/2017
# Author  : Xiao Ling

# sources : http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
# conclusion: installing openCV is too time consuming for now
############################################################

import os
import cv2
import pickle
import numpy as np
from PIL import Image as Im

from app import *

############################################################
'''
	make current directory
'''
app    = App()
paths  = app.module('face')
im_dir = app.fetch ('Abby-1')


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
	face extraction			
'''
disp_image = False

# load image
im_path = im_paths[2]
img     = cv2.imread(im_path)

# display image if needed
if disp_image:
	print('\n\t>> displaying image for ' + meta['name'])
	pic     = Im.fromarray(img,'RGB')
	pic.show()

# load open cv classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier('haarcascade_eye.xml')

gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)










