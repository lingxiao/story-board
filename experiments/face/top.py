############################################################
# Module  : face/top
# Date    : 05/28/2017
# Author  : Xiao Ling

# sources : http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html


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

############################################################
'''
	@Use: make one script for each shard 
'''	
def make_scripts(shards):

	for shard in shards:

		letter = shard.split('/')[-1].split('.')[0]

		print('\n\t>> auto generating script and shell for letter ' + letter)

		src_path = os.path.join(work_dir['templates'], 'script-A.py')
		tgt_path = os.path.join(work_dir['script'], 'script-' + letter + '.py')
		src_strs = "{LETTER}"
		tgt_strs = letter

		auto_gen(src_path, tgt_path, [src_strs], [tgt_strs])

		src_shell = os.path.join(work_dir['templates'], 'shell-A.sh')
		tgt_shell = os.path.join(work_dir['shells'], 'shell-' + letter + '.sh')
		src_xs    = 'script-A'
		tgt_xs    = 'script-' + letter
		auto_gen(src_shell, tgt_shell, [src_xs], [tgt_xs])

	print('\n\t>> finished!')


if False:
	app.shard_data()
	shard_root  = app.fetch('female-shards')
	shards      = [ os.path.join(shard_root, p) for p in os.listdir(shard_root) ]
	make_scripts(shards)













