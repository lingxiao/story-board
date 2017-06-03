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

from app import *
from utilities import *
from experiments.face import *

############################################################
'''
	init app
'''
try: app
except: app = App()

# application paths
work_dir    = app.module('experiments/face', ['templates', 'script', 'shells'])
face_dir    = app.fetch('face/dlib-resnet_model_v1')
no_face_dir = app.fetch('face/no-face-dlib-resnet_model_v1')


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
'''








