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
papers = load_json('allpaper.txt')
paper2num = dict()
author2num = dict()
nump = len(CONFS)
for pa in papers:
    if int(pa['year']) <2012:
      paper2num[pa['id']] = str(nump)
      nump += 1
edges = []
for i in range(len(CONFS)):
    tmp = load_json('papers/'+CONFS[i]+'.txt')
    for j in range(len(tmp)):
        if int(tmp[j]['year']) < 2012:
            edges.append([paper2num[tmp[j]['id']],i])
            authors = tmp[j]['authors']
            for au in authors:
              if au.replace(' ','') not in author2num.keys():
                author2num[au.replace(' ','')] = nump
                nump += 1
              edges.append([author2num[au.replace(' ','')],i])
            if 'references' in tmp[j].keys():
              refer = tmp[j]['references']
            else:
                continue
            if refer == []:
                continue
            for re in refer:
                if re in paper2num.keys():
                    edges.append([paper2num[tmp[j]['id']],paper2num[re]])
with open('edges_mixture_4task3all.txt','w') as f:
   for i in range(len(edges)):
       f.write(str(edges[i][0])+" "+str(edges[i][1])+"\n")