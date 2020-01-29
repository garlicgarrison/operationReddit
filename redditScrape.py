import praw
from gtts import gTTS
import os
import datetime

#getting dates
date = datetime.datetime.now()
year = str(date.year)
month = date.strftime("%b")
day = str(date.strftime("%d"))

#creates directory of the day with the posts
path = r"C:\Users\Jang's PC\Desktop\reddit tifu"
os.chdir(path)
try:
    os.mkdir('tifu' + year + '_' + month + day)
except OSError:
    print("Creation of the directory failed")

#accessing the api, subreddit, and setting how many
reddit = praw.Reddit(client_id = 'rbeXlfswKMdB5A',
                     client_secret = 'RsvgD0vviZybBCWXF0IbzSz025E',
                     username = 'CrypticStevenRSA',
                     password = 'kijoonkijoon',
                     user_agent = 'garlic'  )

subreddit = reddit.subreddit('tifu')
#5 refers to 5 top posts of the day
top_python = subreddit.top('day', limit=5)

#array of string
texts = []
plaintxt = []
titles = []
links = []
language = 'en'

for submission in top_python:
    if not submission.stickied:
        texts.append(submission.title + submission.selftext)
        plaintxt.append(submission.title + submission.selftext)
        titles.append(submission.title)
        links.append(submission.permalink)

for sub in range(len(texts)):
    texts[sub] = gTTS(text=texts[sub], lang = language, 
                                             slow = False)
    
os.chdir(path+ '\\tifu' + year+'_' + month + day)
os.mkdir('audio')
os.mkdir('text')

#creating and writing text file of titles and links
f = open('links_titles.txt', "w+")
for tit in titles:
    f.write(tit + '\n')
f.write('\n')    
for url in links:
    f.write('www.reddit.com' + url + '\n')
f.close()
    
#saving audio files
os.chdir(path+ '\\tifu' + year+'_' + month + day + '\\audio')
for x in range(len(texts)):
    texts[x].save("tifu" + year + month + day + 
                         '_' + str(x) + ".mp3")
    
#saving text files
os.chdir(path+ '\\tifu' + year+'_' + month + day + '\\text')
for x in range(len(plaintxt)):
    wr = open('text' + str(x) + '.txt', "w+")
    wr.write(plaintxt[x] + '\n' + '\n')
    wr.close()
    
    
    
    
    
    
    
    
    
