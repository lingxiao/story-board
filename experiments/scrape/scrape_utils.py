
############################################################
# Module  : scrape/scrape_utils
# Date    : 05/28/2017
# Author  : Xiao Ling
############################################################

import os
import shutil
import pickle
import string
from app import *
from experiments.scrape import *


'''
	@Use: make copy of tinder-_ directory with 
		  meta file only

		  this is useful when running on remote since 
		  remote server has disk quota
'''
def make_meta_only(image_path):

	print('\n>> making meta only... ')
	out_path   = image_path + '-meta-only'

	if not os.path.exists(out_path):
		print('\n>> making directory at ' + out_path)
		os.mkdir(out_path)

	in_dirs = [ p for p in os.listdir(image_path) if '-' in p ]

	for dir_name in in_dirs:
		in_dir  = os.path.join(image_path, dir_name)
		out_dir = os.path.join(out_path  , dir_name)

		if os.path.exists(out_dir):
			print('\n\t>> already copied over user ' + dir_name)
		else:
			os.mkdir(out)
			paths = [p for p in os.listdir(in_dir) if 'meta' in p]
			if paths:
				path = os.path.join(in_dir, paths[0])
				with open(path,'rb') as h:
					m = pickle.load(h)

				print('\n\t>> copying meta for user: ' + m['name'])	

				out = os.path.join(out_path, dir_name) 


				with open(out + '/meta.pkl', 'wb') as h:
					pickle.dump(m,h)

	print('\n\t>> DONE! ')		


'''
	@Use: remove directories that have meta file only
		  this is useful when transferring files from remote 
		  that have directories with meta only
'''
def remove_meta_only(image_path):

	in_dirs = [ os.path.join(image_path, p) for p in os.listdir(image_path) ]

	for in_dir in in_dirs:
		paths = os.listdir(in_dir)

		if len(paths) == 1 and 'meta' in paths[0]:
			print('\n\t>> removing directory ' + in_dir)
			shutil.rmtree(in_dir)

	print('\n\t>> Done!')		


'''
	@Use: merge remote directories with local
		  if names overlap, rename remote 
'''
def merge_remote_with_local(remote_root, local_root):

	if not os.exists(remote_root) or not os.exists(local_root):
		raise NameError('Failed, cannot find remote or local root')


	remote_dirs = [os.path.join(remote_root, p) for p in os.listdir(remote_root)]

	for src in remote_dirs:

		name = src.split('/')[-1]
		tgt  = os.path.join(local_root, name)

		if os.path.exists(tgt):
			print('\n\t>> found existing file for ' + tgt 
				 + '\n\t\t>> incrementing counter to prevent name collison')

			new_path = tgt.split('-')
			new_tgt  = '-'.join(new_path[0:-1])
			idx      = int(new_path[-1]) + 1
			new_tgt  = new_tgt + '-' + str(idx)

			shutil.move(src, new_tgt)

		else:
			print('\n\t>> moving directory to ' + tgt)
			shutil.move(src, tgt)




if False:
	print('\n\t>> making meta only ...')
	app = App()
	make_meta_only(app.fetch('data/female'))

if False:
	print('\n\t>> removing meta only ...')
	app = App()
	image_path = app.fetch('data/remote-meta-pics')
	remove_meta_only(image_path)

if False:
	print('\n\t>> merging all pictures from remote to local ...')
	app = App()
	remote_root = app.fetch('data/remote-meta-pics')
	local_root  = app.fetch('data/female'   )
	merge_remote_with_local(remote_root, local_root)

