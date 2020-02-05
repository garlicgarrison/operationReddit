import numpy as np
from skimage import transform as tf

from moviepy.editor import *
from moviepy.video.tools.drawing import color_gradient
import os
import time

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

#INSERT THE RAW TEXT (here: "A New Hope")


os.chdir(r"C:\Users\Jang's PC\Desktop\reddit tifu\tifu2020_Jan28\text")
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
    


# Add blanks before and after text
# txt = 10*"\n" +txt + 10*"\n"


# CREATE THE TEXT IMAGE

clip_txt = TextClip(txt,color='cyan', align='Center', fontsize=25,
                    font='Xolonium-Bold', method='label')


# SCROLL THE TEXT IMAGE BY CROPPING A MOVING AREA

txt_speed = 0.2 
fl = lambda gf,t : gf(t)[int(txt_speed*t):int(txt_speed*t)+h,:]
moving_txt= clip_txt.fl(fl, apply_to=['mask'])
lol = moving_txt


# # ADD A VANISHING EFFECT ON THE TEXT WITH A GRADIENT MASK

# grad = color_gradient(moving_txt.size,p1=(0,2*h/3),
#                 p2=(0,h/4),col1=0.0,col2=1.0)
# gradmask = ImageClip(grad,ismask=True)
# fl = lambda pic : np.minimum(pic,gradmask.img)
# moving_txt.mask = moving_txt.mask.fl_image(fl)


# # WARP THE TEXT INTO A TRAPEZOID (PERSPECTIVE EFFECT)

# def trapzWarp(pic,cx,cy,ismask=False):
#     Y,X = pic.shape[:2]
#     src = np.array([[0,0],[X,0],[X,Y],[0,Y]])
#     dst = np.array([[cx*X,cy*Y],[(1-cx)*X,cy*Y],[X,Y],[0,Y]])
#     tform = tf.ProjectiveTransform()
#     tform.estimate(src,dst)
#     im = tf.warp(pic, tform.inverse, output_shape=(Y,X))
#     return im if ismask else (im*255).astype('uint8')

# fl_im = lambda pic : trapzWarp(pic,0.2,0.3)
# fl_mask = lambda pic : trapzWarp(pic,0.2,0.3, ismask=True)
# warped_txt= moving_txt.fl_image(fl_im)
# warped_txt.mask = warped_txt.mask.fl_image(fl_mask)

#adding the audio
os.chdir('C:/Users/kevin/Desktop')
audiofile = AudioFileClip('tifu2020Feb02_0.mp3')


# BACKGROUND IMAGE, DARKENED HERE AT 60%

stars = ImageClip('C:/Users/kevin/Desktop/movie/blacknew.png')
#stars_darkened = stars.fl_image(lambda pic: (0.6*pic).astype('int16'))


# COMPOSE THE MOVIE

# final = CompositeVideoClip([
#          audiofile,
#          lol],
#          size = moviesize)


# WRITE TO A FILE
#For the duration dynamically take the time for the audio file and set_duration to that time
no_sound = clip_txt.set_duration(85).write_videofile("leggo.mp4", 
                                       fps=18, codec='libx264')

# final_clip = concatenate_videoclips([audiofile,clip_txt])
# final_clip.set_duration(85).write_videofile("LFG.mp4", fps=18, codec='libx264')

time.sleep(5)


#final_audio = CompositeAudioClip([leggo.mp4.audio, audiofile])
final_clip = CompositeAudioClip(audiofile,no_sound)
final_clip.write_videofile("leggo_sound.mp4",fps=18, codec='libx264')




