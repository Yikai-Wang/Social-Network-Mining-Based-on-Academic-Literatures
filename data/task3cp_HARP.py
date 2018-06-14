#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yikai Wang
"""
import numpy as np
import json
import random

def load_json(dir):
   data = []
   with open(dir, 'r') as f:
       while True:
           a = f.readline()
           if not a:
               break
           b = json.loads(a)
           data.append(b)
   return data

papers = load_json('allpaper.txt')
paper2num = dict()
author2num = dict()
nump = 0
for pa in papers:
  if int(pa['year']) <2012:
    paper2num[pa['id']] = str(nump)
    nump += 1
print(nump)
for pa in papers:
  if int(pa['year']) <2012:
    authors = pa['authors']
    for au in authors:
      if au.replace(' ','') not in author2num.keys():
        author2num[au.replace(' ','')] = nump
        nump += 1
#edges = []
#for pa in papers:
#    if int(pa['year'])<2012:
#        for au in pa['authors']:
#            edges.append([paper2num[pa['id']],author2num[au.replace(' ','')]])
#            
#with open('edges_mixture_4task3cp.txt','w') as f:
#   for i in range(len(edges)):
#       f.write(str(edges[i][0])+" "+str(edges[i][1])+"\n")