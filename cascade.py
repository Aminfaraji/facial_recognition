#!/usr/bin/env python
# coding: utf-8

# In[8]:


from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os
from pathlib import Path


# In[6]:


arg=argparse.ArgumentParser('detect face and eyes')
arg.add_argument('-c','--cascade',type=str,help='import cascade file face detect')
arg.add_argument('--input',type=str,default='0',help='import cascade file face detect')
args=arg.parse_args()


# In[3]:


detectorpath={
    'face' : 'haarcascade_frontalface_default.xml',
    'eye' : 'haarcascade_eye.xml',
    'smile': 'haarcascade_smile.xml'
}
detectcascade={}
for name,path in detectorpath.items():
    path=os.path.join(args.cascade,path)
    detectcascade[name]=cv2.CascadeClassifier(path)


# In[6]:


# detect_eyes='E:\project_windows\.venv311\Lib\site-packages\cv2\data\haarcascade_eye.xml'
# detect_face='E:\project_windows\.venv311\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'


# In[7]:


def run(input):
    video=VideoStream(input).start()
    #time.sleep(2.0)
    while True:
        fram=video.read()
        fram=imutils.resize(fram,width=500,height=500)
        gray=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
        faces=detectcascade['face'].detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
        for (x,y,w,h) in faces:
            face=gray[y:y+h,x:x+w]
            smile=detectcascade['smile'].detectMultiScale(face,scaleFactor=1.1,minNeighbors=10,minSize=(15,15),flags=cv2.CASCADE_SCALE_IMAGE)
            eyes=detectcascade['eye'].detectMultiScale(face,scaleFactor=1.1,minNeighbors=10,minSize=(15,15),flags=cv2.CASCADE_SCALE_IMAGE)
            for (ex,ey,eh,ew) in eyes:
                cv2.rectangle(fram,(ex+x,ey+y),(x+ex+ew,ey+eh+y),(0,255,0),1)
            for (sx,sy,sh,sw) in smile:
                cv2.rectangle(fram,(y+sy,x+sx),(y+sy+sh,x+sx+sw),(0,0,255),1)
            cv2.rectangle(fram,(x,y),(x+w,y+h),(255,0,0),1)
        cv2.imshow('video',fram)
        if cv2.waitKey(15) & 0xFF==ord('q'):
            break
    cv2.destroyAllWindows()
    video.stop()

# In[9]:

if args.input=='0':
    run(int(args.input))
elif os.path.exists(args.input):
    run(str(args.input))
else:
    print('is not directory')
    


# In[ ]:




