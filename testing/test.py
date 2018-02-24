from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json

app = ClarifaiApp(api_key='f3fa183a15bc4dfba346f09f93b7784c')
model = app.models.get("moderation")

#predict 
#print model.predict("girl.jpeg")
image = ClImage(file_obj=open('girl.jpeg', 'rb'))
print(model.predict([image]))