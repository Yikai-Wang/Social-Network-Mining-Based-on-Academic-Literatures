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
confs = {'dp':dp_conf,'ml':ml_conf,'dm':dm_conf,'ed':ed_conf,'nl':nl_conf,'os':os_conf}

import numpy as np
import pickle
import json

def load_pickle(filename):
   pkl_file = open(filename, 'rb')
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

def load_txt(filename):
    txt = {}
    with open(filename,'r') as f:
        while True:
            tmp = f.readline()
            if not tmp:
                break
            tmp = tmp.split()
            txt[tmp[0]] = tmp[1]
    return txt

result = load_pickle('cluster_KMeans_word2vec_nrl.pkl')
id2num = load_txt('id2num.txt')
true_label = {}
for k,v in confs.items():
  tmp = []
  for m in v:
      tmp += load_json('papers/'+m+'.txt')
  for i in range(len(tmp)):
      true_label[id2num[tmp[i]['id']]]=k
    
predict={}
for i in range(6):
    predict[i]=dict()
    for k in confs.keys():
      predict[i][k] = 0
for k,v in result.items():
    predict[v][true_label[str(k)]] += 1

print(predict)
num2str = dict()
num2str[0]='os'
num2str[1]='nl'
num2str[2]='ml'
num2str[3]='ed'
num2str[4]='dp'
num2str[5]='dm'
prop = {}
for k in confs.keys():
  prop[k] = [0,0]
for k,v in true_label.items():
    prop[v][1] += 1
    try:
        if num2str[result[int(k)]]==v:
            prop[v][0] += 1
    except:
        pass
num0 = 0
num1 = 0
for k,v in prop.items():
    num0 += v[0]
    num1 += v[1]
print(num0/num1)