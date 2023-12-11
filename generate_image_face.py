#!/usr/bin/env python
# coding: utf-8

# In[1]:


from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os
from pathlib import Path


# In[2]:


arg=argparse.ArgumentParser(description='Generate Face amin faraji')
arg.add_argument('--cascade',
                 default='./Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml',
                help='Path your cascade')
arg.add_argument('--output', default='dataset_face_amin',help='Path output images face')
args=arg.parse_args()


# In[5]:

if not os.path.exists(args.output):
    os.mkdir(args.output)
vs=VideoStream(0).start()
detect_face=cv2.CascadeClassifier(args.cascade)
count=0
while True:
    fram=vs.read()
    orig=fram.copy()
    fram=cv2.resize(fram,(600,600))
    gray=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    face_amin=detect_face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    for (x,y,w,h) in face_amin:
        cv2.rectangle(fram,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('video',fram)
    key=cv2.waitKey(1) & 0xFF
    if key==ord('k'):
        p=args.output+'/amin_{}.png'.format(str(count))
        cv2.imwrite(p,orig)
        count+=1
    elif key==ord('q'):
        break
vs.stop()
cv2.destroyAllWindows()


# In[6]:


"amin_{}.png".format(str(5))


# In[ ]:




