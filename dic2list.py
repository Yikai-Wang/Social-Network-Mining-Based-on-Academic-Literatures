#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yikai Wang
"""
import numpy as np
import pickle
import json
def load_pickle():
   pkl_file = open('vector.pkl', 'rb')
   data1 = pickle.load(pkl_file)
   pkl_file.close()
   return data1

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
edges = []
id2num = dict()
num = 0
for i in range(4):
    data = load_json('dblp-ref/dblp-ref-'+str(i)+'.json')
    for j in range(len(data)):
        id2num[data[j]['id']]=num
        num += 1
for j in range(4):
    data = load_json('dblp-ref/dblp-ref-'+str(j)+'.json')
    for i in range(len(data)):
        if 'references' in data[i].keys() and data[i]['references']:
            for nn in data[i]['references']:
                edges.append([id2num[data[i]['id']], id2num[nn]])
        else:
            edges.append([id2num[data[i]['id']], id2num[data[i]['id']]])
with open('edges_full.txt','w') as f:
   for i in range(len(edges)):
       f.write(str(edges[i][0])+'\t'+str(edges[i][1])+'\n')
with open('id2num.txt','w') as f:
   for k,v in id2num.items():
       f.write(str(k)+'\t'+str(v)+'\n')
#data = np.load('wyk.npy')