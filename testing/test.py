# from clarifai.rest import ClarifaiApp
# from clarifai.rest import Image as ClImage
# import json

# app = ClarifaiApp(api_key='f3fa183a15bc4dfba346f09f93b7784c')
# model = app.models.get("moderation")

# #predict 
# #print model.predict("girl.jpeg")
# image = ClImage(file_obj=open('gorey.jpg', 'rb'))
# print(model.predict([image]))

from sightengine.client import SightengineClient

client = SightengineClient('258566145', 'nGGUMmk7CsQ6463MHQjY')
output = client.check('nudity', 'wad').video('https://d3m9459r9kwism.cloudfront.net/stream/examples/funfair.mp4', 'http://localhost:5000/callback/')
# output = client.check('nudity').set_url('https://d3m9459r9kwism.cloudfront.net/img/examples/example-fac-1000.jpg')
print(output)