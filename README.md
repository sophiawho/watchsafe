# WATCHSAFE

## Hack The Valley II

*watchsafe* uses **computer vision** to scan video clips for nsfw content by flagging the start and end of the nsfw content, and displaying the type of nsfw content (drugs/nudity/gore)


### technology:
1. clarifai/microsoft custom vision
2. python (flask)
3. node.js backend

### challenges:
1. rate-limiting api
2. getting clarifai to return second of video

### applications:
1. nanny cam
2. teachers, parents showing movies
3. crime scenes

### primary goals:
1. be able to mark certain kinds of nsfw content
2. mark the start/end of nsfw content
3. deploy onto web app

### secondary goals:
1. chrome extension
2. live black-out
