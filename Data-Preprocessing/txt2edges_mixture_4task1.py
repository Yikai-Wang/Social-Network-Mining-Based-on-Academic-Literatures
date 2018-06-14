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
author2num = dict()
paper2num = dict()
nump = 0
for pa in papers:
  paper2num[pa['id']] = str(nump)
  nump += 1
print(nump)
for pa in papers:
  authors = pa['authors']
  for au in authors:
    if au not in author2num.keys():
      author2num[au] = nump
      nump += 1
edges = []
for pa in papers:
  for au in pa['authors']:
    edges.append([paper2num[pa['id']],author2num[au]])
  if 'references' in pa.keys():
    refer = pa['references']
  else:
    continue
  if refer == []:
    continue
  for re in refer:
    if re in paper2num.keys():
      edges.append([paper2num[pa['id']],paper2num[re]])
with open('edges_mixture_4task1.txt','w') as f:
   for i in range(len(edges)):
       f.write(str(edges[i][0])+" "+str(edges[i][1])+"\n")

