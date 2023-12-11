#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
from glob import glob
import argparse


# In[4]:


arg=argparse.ArgumentParser()
arg.add_argument('--input',help='folder images for rename')
args=arg.parse_args()


# In[19]:


images=glob(args.input+'/*')
for file in images:
    src=os.path.split(file)[1].replace('amin_','')
    des=args.input+'/'+src
    os.rename(file,des)

