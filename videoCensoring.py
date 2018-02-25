## import the video, divide into subclips 
import imageio
from moviepy.editor import *

# map a flag to image file
def mapFlagToImage(flag):
	if flag == "nudity":
		return "nudity.png"
	elif flag == "drugs":
		return "drugs.png"
	elif flag == "alcohol":
		return "alcohol.png"
	elif flag == "weapon":
		return "weapon.png"

# split into subclips
clip1 = VideoFileClip("shooting.mp4").subclip(0,12)
clip2 = VideoFileClip("shooting.mp4").subclip(17, 20)

# set the censor audio clip
censoraudio = AudioFileClip("thomastrain.mp3")
censoraudio = censoraudio.set_duration(5)

# make the censored subclip wuth specified color, text, duration and audio
censorcontent = ImageClip("violentcontent.png")
censorcontent = censorcontent.set_duration(5)
censorcontent = censorcontent.set_audio(censoraudio)
censorcontent.resize((200,200))

# concatenate the clips into one final clip and write to a new file
final_clip = concatenate_videoclips([clip1,censorcontent,clip2], method="compose")
final_clip.write_videofile("censoredvideo.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

