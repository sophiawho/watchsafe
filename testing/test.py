from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='f3fa183a15bc4dfba346f09f93b7784c')
model = app.models.get("moderation")

#predict 
print model.predict_by_url(url="https://samples.clarifai.com/moderation.jpg")

