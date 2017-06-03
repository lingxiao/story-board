############################################################
# Module  : face/run_dlib
# Date    : 05/28/2017
# Author  : Xiao Ling
# Module  : function run dlib face detection and representation
# source  : installing dlib w/o conda:
#                http://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/
#           installing using conda:
# 				 conda install -c conda-forge dlib=19.4
############################################################

import os
import dlib
import numpy as np
import pickle
from skimage import io
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


from app import *

'''
	@Use: open all users and find face representation
	      save to out_dir

	@Input:  in_dir : list of absolute paths to input user directories
		                containing their pictures

		     out_root: absolute path to output directory

		     model_root: absolute path to model with these two models:
							shape_predictor_68_face_landmarks.dat		     
							shape_predictor_68_face_landmarks.dat

			debug: if True then only run on first five paths				

'''
def parse_all_users(in_dirs, out_root, model_root, debug = False):

	suffix = '[ debug ]' if debug else '[ production ]'
	print('\n>> running parse_all_users in ' + suffix + ' mode ...')

	if not os.path.exists(out_root):
		os.mkdir(out_root)

	predictor_path        = os.path.join( model_root, 'shape_predictor_68_face_landmarks.dat' )
	face_recog_model_path = os.path.join( model_root, 'face_recognition_resnet_model_v1.dat'  )

	if os.path.exists(predictor_path) and os.path.exists(face_recog_model_path):
			print('\n\t>> loading pre-trained image models')
			detector   = dlib.get_frontal_face_detector()
			shape_pred = dlib.shape_predictor(predictor_path)   
			face_phi   = dlib.face_recognition_model_v1(face_recog_model_path)
	else:
		raise NameError('Cannot find path:\n\t>> '  \
			           + predictor_path + '\n\t>> ' \
			           + face_recog_model_path      )	

	if debug:
		in_dirs = in_dirs[0:5]

	for in_dir in in_dirs:
		out_path = os.path.join(out_root, in_dir.split('/')[-1]) + '.pkl'
		parse_user(in_dir, out_path, detector, shape_pred, face_phi)

	print('\n>> DONE!')

############################################################
'''
	@Use: open all pictures at in_dir,
	      find 126 dimension feature representation
	      of all pictures of each user
	      save to out_root/name
'''		
def parse_user(in_dir, out_path, detector, shape_pred, face_phi):

	name = in_dir.split('/')[-1]

	if os.path.exists(out_path):
		print('\n\t>> user ' + name + ' already exists, skipping')
	else:

		print('\n\t>> parsing user ' + name)

		data_paths = [ os.path.join(in_dir, p) for p in os.listdir(in_dir) ]
		im_paths   = [ p for p in data_paths if '.jp' in p  ]
		pkl_path   = [ p for p in data_paths if '.pkl' in p ]


		if pkl_path:
			with open(pkl_path[0], 'rb') as h:
				meta = pickle.load(h)
		else:
				meta = {'error': 'meta file found'}

		if im_paths:

			phis = parse_faces(im_paths, detector, shape_pred, face_phi)

			out = {'phis': phis, 'meta': meta}

			with open(out_path, 'wb') as h:
				pickle.dump(out, h)


'''
	@Use: find 126 dimension feature representation
	      of all pictures of each user
'''		
def parse_faces(im_paths, detector, shape_pred, face_phi):

	faces = dict()

	ImageFile.LOAD_TRUNCATED_IMAGES = True

	for im_path in im_paths:

		im_name = im_path.split('/')[-1]
		img     = io.imread(im_path)
		dets    = list(enumerate(detector(img, 1)))


		if len(dets) == 1:

			k,d = dets[0]

			lft  = max(d.left()  , 0)
			rt   = max(d.right() , 0)
			tp   = max(d.top()   , 0)
			bot  = max(d.bottom(), 0)

			face  = img[lft:rt, tp:bot]
			shape = shape_pred(img,d)

			phi_face = face_phi.compute_face_descriptor(img, shape)


			faces[im_name] = { 'phi': phi_face
			                 , 'box': {'left'  : lft
			                          ,'right' : rt
			                          ,'top'   : tp
			                          ,'bottom': bot
			                          }
			                 }       

		elif len(dets) == 0:
			faces[im_name] = {'error': 'no faces found'}
		else:
			faces[im_name] = {'error': 'found ' + str(len(dets)) + ' faces'}


	return faces		                 



