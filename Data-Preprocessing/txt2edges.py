#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yikai Wang
"""
#This file generate edges of papers based on references.
dp_conf = ['PPOPP', 'PACT', 'IPDPS', 'ICPP']
ml_conf = ['IJCAI', 'ICML', 'NIPS']
dm_conf = ['ICDE', 'SIGMOD','KDD' , 'ICDM']
ed_conf = ['AIED', 'ITS', 'ICALT']
nl_conf = ['ACL','EACL' , 'COLING', 'EMNLP']
os_conf = ['MASCOTS', 'SOSP', 'OSDI']


import pickle
import json

def load_pickle():
    """
    load pkl file.
    :return: data as a dictionary.
    """
    pkl_file = open('cluster_Birch_nrl.pkl', 'rb')
    data1 = pickle.load(pkl_file)
    pkl_file.close()
    return data1

def load_json(dir):
    """
    load json file
    :param dir: path we save the data
    :return: data as a list.
    """
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
id2num = dict()
num = 0
for j in range(len(papers)):
    id2num[papers[j]['id']]=num
    num += 1
for i in range(len(papers)):
    if 'references' in papers[i].keys() and papers[i]['references']:
        tmp = len(papers[i]['references'])
        for nn in papers[i]['references']:
            if id2num.get(nn,-1)!=-1:
                edges.append([id2num[papers[i]['id']], id2num[nn]])
            elif [id2num[papers[i]['id']], id2num[papers[i]['id']]] not in edges[-tmp-1:]:
                edges.append([id2num[papers[i]['id']], id2num[papers[i]['id']]])
                
    else:
        edges.append([id2num[papers[i]['id']], id2num[papers[i]['id']]])
with open('edges_select.txt','w') as f:
   for i in range(len(edges)):
       f.write(str(edges[i][0])+" "+str(edges[i][1])+"\n")
with open('id2num.txt','w') as f:
   for k,v in id2num.items():
       f.write(str(k)+' '+str(v)+'\n')
