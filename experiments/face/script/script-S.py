############################################################
# Module  : face/top
# Date    : 05/28/2017
# Author  : Xiao Ling
############################################################


import os
import pickle
import numpy as np
from PIL import Image as Im

from app import *

############################################################
'''
	init app
'''
try: app
except: app = App()

model_root  = app.fetch('assets/dlib')
shard_root  = app.fetch('female-shards')
shards      = [ os.path.join(shard_root, p) for p in os.listdir(shard_root) ]
out_root    = app.fetch('data/results/face/dlib-resnet_model_v1')
# os.path.join(work_dir['results'], 'dlib-resnet_model_v1')

############################################################

letter = 'S'

shard = [s for s in shards if letter == s.split('/')[-1].split('.')[0]]

if shard:
	with open(shard[0], 'rb') as h:
		usr_paths = pickle.load(h)
		usr_paths = [v for _,v in usr_paths.iteritems()]
		parse_all_users(usr_paths, out_root, model_root, debug = False)

