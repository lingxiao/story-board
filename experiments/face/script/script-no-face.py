
############################################################
# Module  : face/top
# Date    : 05/28/2017
# Author  : Xiao Ling
############################################################


import os
import pickle
import numpy as np

from skimage import io
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from app import *
from utilities import *
from experiments.face import *

############################################################
'''
	init app
'''
try: app
except: app = App()

dir_name    = 'no-faces'

model_root  = app.fetch('assets/dlib')

out_root    = app.fetch('data/results/face/no-face-dlib-resnet_model_v1')

usr_root    = app.fetch(dir_name)

usr_paths   = [ os.path.join(usr_root, p) for p in os.listdir(usr_root) \
                if '.DS_Store' not in p ]

############################################################

if True:
	parse_all_users( [usr_root]
		           , out_root
		           , model_root
		           , debug = False
		           )
