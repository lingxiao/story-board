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

work_dir = app.module('experiments/face', ['templates', 'script', 'shells'])






