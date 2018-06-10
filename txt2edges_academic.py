#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yikai Wang
"""
dp_conf = ['PPOPP', 'PACT', 'IPDPS', 'ICPP']
ml_conf = ['IJCAI', 'ICML', 'NIPS']
dm_conf = ['ICDE', 'SIGMOD','KDD' , 'ICDM']
ed_conf = ['AIED', 'ITS', 'ICALT']
nl_conf = ['ACL','EACL' , 'COLING', 'EMNLP']
os_conf = ['MASCOTS', 'SOSP', 'OSDI']

import numpy as np
import pickle
import json

def load_pickle():
   pkl_file = open('cluster_Birch_nrl.pkl', 'rb')
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
papers = []
meetings = dp_conf+ml_conf+dm_conf+ed_conf+nl_conf+os_conf
for met in meetings:
    papers += load_json(str(met)+'.txt')

edges = []
name2num = dict()
num = 0
for j in range(len(papers)):
    tmp = papers[j]['authors']
    for i in range(len(tmp)):
        if tmp[i] not in name2num.keys():
          name2num[tmp[i]] = num
          num += 1
    if len(tmp) == 1:
        edges.append([name2num[tmp[0]],name2num[tmp[0]]])
    else:
        for l in range(len(tmp)-1):
            for k in range(l+1,len(tmp)):
                edges.append([name2num[tmp[l]],name2num[tmp[k]]])
                edges.append([name2num[tmp[k]],name2num[tmp[l]]])
with open('edges_people_cooperation.txt','w') as f:
   for i in range(len(edges)):
       f.write(str(edges[i][0])+" "+str(edges[i][1])+"\n")
with open('name2num.txt','w') as f:
   for k,v in name2num.items():
       f.write(str(k)+' '+str(v)+'\n')
   
