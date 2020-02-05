import numpy as np
from skimage import transform as tf

from moviepy.editor import *
from moviepy.video.tools.drawing import color_gradient
import time
import shlex, subprocess
import os
import datetime

# How to run script:
# pip install numpy
# pip install ffmpeg
# pip install moviepy
# pip install scikit-image
# pip install scipy

# install ImageMagick and untick Install ffmpeg in the installer:
# https://imagemagick.org/download/binaries/ImageMagick-7.0.9-21-Q16-x64-dll.exe

# Navigate to C:\Users\kevin\AppData\Local\Programs\Python\Python38\Lib\site-packages\moviepy
# Then open the config_defaults file and replace the last line with:
# IMAGEMAGICK_BINARY = "C:\Program Files\ImageMagick-7.0.9-Q16\magick.exe"

# Now run the script.

# RESOLUTION 

w = 1920
h = w*9//16 
moviesize = w,h

#getting dates
date = datetime.datetime.now()
year = str(date.year)
month = date.strftime("%b")
day = str(date.strftime("%d"))

os.chdir(r"C:\Users\kevin\Desktop\reddit")
os.chdir('tifu' + year + '_' + month + day)
os.chdir("text")

f = open("text0.txt", "r")
story = f.read()
f.close()
story = story.replace('\n', ' ').replace('\r', ' ')
sublist = []


def split_string(str, limit, sep=" "):
    words = str.split()
    #if max(map(len, words)) > limit:
        #raise ValueError("limit is too small")
    res, part, others = [], words[0], words[1:]
    for word in others:
        if len(sep)+len(word) > limit-len(part):
            res.append(part)
            part = word
        else:
            part += sep+word
    if part:
        res.append(part)
    return res


sublist = split_string(str = story, limit = 64, sep=" ")
   
        
txt = """"""
for x in sublist:
    txt = txt + x + '\n'


# CREATE THE TEXT IMAGE

clip_txt = TextClip(txt,color='cyan', align='Center', fontsize=25,
                    font='Xolonium-Bold', method='label')


# SCROLL THE TEXT IMAGE BY CROPPING A MOVING AREA
#Scrolling code

# txt_speed = 0.2 
# fl = lambda gf,t : gf(t)[int(txt_speed*t):int(txt_speed*t)+h,:]
# moving_txt= clip_txt.fl(fl, apply_to=['mask'])
# lol = moving_txt

#adding the audio
os.chdir(r"C:\Users\kevin\Desktop\reddit")
os.chdir('tifu' + year + '_' + month + day)
os.chdir("audio")
audiofile = AudioFileClip('tifu2020Feb04_0.mp3')

#change the duration dynamically to the current audio file length
os.chdir(r"C:\Users\kevin\Desktop\reddit")
clip_txt.set_duration(85).write_videofile("leggo.mp4", 
                                       fps=18, codec='libx264', audio=audiofile)

time.sleep(5)

cmd = 'ffmpeg.exe -i leggo.mp4 -i C:\\Users\\kevin\\Desktop\\reddit\\tifu2020_Feb04\\audio\\tifu2020Feb04_0.mp3 -c copy final.mp4'
subprocess.call(cmd,shell=True)