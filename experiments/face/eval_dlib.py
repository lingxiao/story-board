############################################################
# Module  : face/eval_dlib
# Date    : 05/28/2017
# Author  : Xiao Ling
# Module  : evaluate dlib for false positive and false negative
#           id of faces
############################################################

import os
import pickle
import numpy as np
from PIL import Image as Im
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from app import *
from utilities import *
from experiments.face import *

############################################################
'''
	init app
'''
try: app
except: app = App()

# asset paths
work_dir    = app.module('experiments/face', ['templates', 'script', 'shells'])
face_dir    = app.fetch ('face/dlib-resnet_model_v1')
no_face_dir = app.fetch ('face/no-face-dlib-resnet_model_v1')
image_root  = app.fetch ('data/female')

############################################################
'''
	evaluate set of pictures with no faces
'''
with open( os.path.join(no_face_dir, 'no-faces.pkl'), 'rb') as h:
	no_face = pickle.load(h)

no_face = no_face['phis']
false_pos_no_face = [ d for d,v in no_face.iteritems() \
                      if 'error' not in v \
                    ]

no_face_false_positive =  len(false_pos_no_face)/float(len(no_face)) * 100

print('\n\t>> false positive face detection: ' + str(no_face_false_positive) + '%')


############################################################
'''
	evaluate set of pictures with faces
		- existence of faces
		- cosine distance of same user faces
		   versus different user faces

	conclusion:	dlib's frontal face api is poorly suited for 
	            tinder/instagram photos   
'''
usr_files = [os.path.join(face_dir,p) for p in os.listdir(face_dir)]

for usr_file in usr_files[530:540]:

	usr_name = usr_file.split('/')[-1].replace('.pkl','')
	usr_dir  = os.path.join(image_root, usr_name)

	with open(usr_file, 'rb') as h:
		usr = pickle.load(h)

	for im_name, im_phi in usr['phis'].iteritems():

	 	box     = im_phi['box']
		im_path = os.path.join(usr_dir, im_name)

		if os.path.exists(im_path):
			img  = io.imread(im_path)
			face = img[box['left']:box['right'], box['top']:box['bottom']]
			pic = Im.fromarray(face, 'RGB')
			pic.show()














































