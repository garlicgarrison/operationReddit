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

txt = """TIFU sleeping on a flightThis morning I fell asleep on the plane. It was an early flight. Napping was inevitable. 
Now, when it comes to sleeping on a plane, I always get insecure about my slack-jawed coma face. Hence, window seat. 
I was able to comfortably doze off without facing the passengers next to me. 
Whom, by the way, was a dad and his teenage daughter who only seem to speak German. 

Cue fuck up. The moment my eyes opened, my face was on the daughter's boob while the dad was frantically shaking me awake. 
The daughter, who also happened to be asleep, woke up the same time I did and immediately started ranting in German. 
I backed as far away from her boobs as possible and profusely apologized to both of them. 
If that wasn't awkward enough, I also felt compelled to offer the daughter a tissue to wipe away my drool from her chest. 
The dad wasted no time making his daughter switch seats with him. She didn't seem too happy about that, but he didn't give a fuck. 
His primary objective was to provide a barrier between my face and his daughter's breast.

Needless to say, I remained wide awake for the rest of the flight. 

TL:DR Fell asleep on the plane. Woke up on a boob. Triggered a German."""


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





