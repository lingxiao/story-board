############################################################
# Module  : scrape/top
# Date    : 05/28/2017
# Author  : Xiao Ling
# source  : https://github.com/scoliann/TinderFaceScraper
############################################################

from app import *
from experiments.scrape import *


app = App()

'''
	scrape for female faces
'''
facebook_token = app.fetch('facebook/xiao/token')
facebook_id    = str(app.fetch('facebook/xiao/id'))
image_path     = app.fetch('data/tinder-female')

print('\n>> lauching crawler for facebook user: ' + facebook_id)
exec_tinder(facebook_token, facebook_id, image_path)








