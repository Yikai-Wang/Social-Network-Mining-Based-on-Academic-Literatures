#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yikai Wang
"""
import json
import pickle
def load_pickle(path):
    pkl_file = open(path, 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data

def load_txt(path):
    with open(path,'r') as f:
        data = []
        while True:
            a = f.readline().split()
            if a:
                data.append(a[0])
            else:
                break
    return data
def write_txt(path,data):
    with open(path,'w') as f:
        for i in range(len(data)):
            f.writelines(str(data[i]))
    return
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
vectors = load_pickle('data/task3cp.pkl')
train_id = load_txt('data/train_id_4task3.txt')
valid_id = load_txt('data/valid_id_4task3.txt')
papers = load_json('data/allpaper.txt')
chosen_authors = list(vectors.keys())
exist_edges = []
missing_edges = []
nonexist_edges = []
for i in range(len(papers)):
    if str(i) in train_id:
        authors = papers[i]['authors']
        new_authors = [au.replace(' ','') for au in authors]
        for i in range(len(new_authors)-1):
            if new_authors[i] in chosen_authors:
                for j in range(i+1,len(authors)):
                    if new_authors[j] in chosen_authors:
                        exist_edges.append([new_authors[i],new_authors[j]])
    elif str(i) in valid_id:
        authors = papers[i]['authors']
        new_authors = [au.replace(' ','') for au in authors]
        for i in range(len(new_authors)-1):
            if new_authors[i] in chosen_authors:
                for j in range(i+1,len(authors)):
                    if new_authors[j] in chosen_authors:
                        missing_edges.append([new_authors[i],new_authors[j]])
tmp = exist_edges + missing_edges
for i in range(len(chosen_authors)-1):
    for j in range(i+1, len(chosen_authors)):
        if ([chosen_authors[i],chosen_authors[j]] not in tmp) and ([chosen_authors[j],chosen_authors[i]] not in tmp):
            nonexist_edges.append([chosen_authors[i],chosen_authors[j]])
        print(i,j)
write_txt('exist_edges_cp.txt',exist_edges)
write_txt('missing_edges_cp.txt',missing_edges)
write_txt('nonexist_edges_cp.txt',nonexist_edges)
