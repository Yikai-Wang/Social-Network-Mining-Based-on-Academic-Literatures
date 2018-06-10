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
train_paper2author = dict()
train_author2paper = dict()
paper2num = dict()
nump = 0
for pa in papers:
    paper2num[pa['id']] = str(nump)
    nump += 1
for pa in papers:
    if int(pa['year'])<2012:
        tmp_id ='v'+paper2num[pa['id']]
        train_paper2author[tmp_id] = []
        authors = pa['authors']
        for au in authors:
            tmp_au = 'a' + au.replace(' ','')
            train_paper2author[tmp_id].append(tmp_au)
            if tmp_au not in train_author2paper.keys():
                train_author2paper[tmp_au] = []
            train_author2paper[tmp_au].append(tmp_id)

numwalks = 40
walklength = 10
outfilename = 'task3cp.w40.l10.txt'
outfile = open(outfilename, 'w')
wyk = 0
for author in train_author2paper.keys():
    tmp_author = author
    for i in range(numwalks):
        outline = tmp_author
        for j in range(walklength):
            papers = train_author2paper[author]
            nump = len(papers)
            paperid = random.randrange(nump)
            paper = papers[paperid]
            outline += ' '+paper
            authors = train_paper2author[paper]
            numa = len(authors)
            authorid = random.randrange(numa)
            author = authors[authorid]
            outline += ' ' + author
        outfile.write(outline + "\n")
    wyk += 1
    print(wyk)
outfile.close()