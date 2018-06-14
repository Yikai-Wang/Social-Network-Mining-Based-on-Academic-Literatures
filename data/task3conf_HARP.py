#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yikai Wang
"""
import numpy as np
import json
import random

CONFS = ['PPOPP', 'PACT', 'IPDPS', 'ICPP',
         'IJCAI', 'ICML', 'NIPS',
         'ICDE', 'SIGMOD', 'KDD', 'ICDM',
         'AIED', 'ITS', 'ICALT',
         'ACL', 'EACL', 'COLING', 'EMNLP',
         'MASCOTS', 'SOSP', 'OSDI']
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
author2num = dict()
nump = len(CONFS)
edges = []
for i in range(len(CONFS)):
    tmp = load_json('papers/'+CONFS[i]+'.txt')
    for j in range(len(tmp)):
        if int(tmp[j]['year']) < 2012:
            authors = tmp[j]['authors']
            for au in authors:
              if au.replace(' ','') not in author2num.keys():
                author2num[au.replace(' ','')] = nump
                nump += 1
              edges.append([author2num[au.replace(' ','')],i])
with open('edges_mixture_4task3conf.txt','w') as f:
   for i in range(len(edges)):
       f.write(str(edges[i][0])+" "+str(edges[i][1])+"\n")