############################################################
# Module  : obj-recog/top.py
# Date    : May 26th 2017
# Author  : Xiao Ling
############################################################

import os

from clarifai import rest
from clarifai.rest import Image
from clarifai.rest import ClarifaiApp

from app import *


############################################################
'''
	make current directory
'''
paths = app.module('obj-recog')
