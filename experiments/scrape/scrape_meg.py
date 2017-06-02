############################################################
# Module  : scrape/top
# Date    : 05/28/2017
# Author  : Xiao Ling
############################################################

from app import *
from experiments.scrape import *


app = App()

'''
	scrape for male faces
'''
facebook_token = app.fetch('facebook/meg/token')
facebook_id    = str(app.fetch('facebook/meg/id'))
image_path     = app.fetch('data/tinder-male')

print('\n>> lauching crawler for facebook user: ' + facebook_id)
exec_tinder(facebook_token, facebook_id, image_path)



