############################################################
# Module  : face/run_openface
# Date    : 05/28/2017
# Author  : Xiao Ling
# Module  : run open face's face detector and represenation
############################################################

import os
import time

import cv2
import dlib
import pickle
import argparse
import itertools
import numpy as np

import openface
from skimage import io
from PIL import ImageFile

from app import *

ImageFile.LOAD_TRUNCATED_IMAGES = True
np.set_printoptions(precision=2)

############################################################

try: app
except: app = App()

align = openface.AlignDlib(args.dlibFacePredictor)
net   = openface.TorchNeuralNet(args.networkModel, args.imgDim, cuda=args.cuda)


