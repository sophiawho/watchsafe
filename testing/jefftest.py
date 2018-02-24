# if you haven't already, install the SDK with "pip install sightengine"
from sightengine.client import SightengineClient
client = SightengineClient('1051134213', 'NHSHEEAmrEdxkapSmt8F')
# output = client.check('nudity','wad').video('https://video.twimg.com/tweet_video/DWlS4OxVMAAlCsh.mp4', 'http://localhost:5000/callback')
output = client.check('nudity','wad').video('https://video.twimg.com/tweet_video/DWlS4OxVMAAlCsh.mp4', 'http://watchsafehtv.us-east-1.elasticbeanstalk.com/callback')
# output = client.check('nudity','wad').video('https://video.twimg.com/tweet_video/DWlS4OxVMAAlCsh.mp4', 'http://requestb.in/1nm1vw11')
# output = client.check('nudity','wad','offensive').set_url('https://previews.123rf.com/images/palinchak/palinchak1312/palinchak131200255/24704322-young-nude-woman-walking-along-a-sandy-beach-on-a-foggy-day.jpg')
print(output)