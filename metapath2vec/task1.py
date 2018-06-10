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
paper2author = dict()
author2paper = dict()
paper2refer = dict()
paper2num = dict()
nump = 0
for pa in papers:
	paper2num[pa['id']] = str(nump)
	nump += 1
for pa in papers:
	tmp_id ='v'+paper2num[pa['id']]
	paper2author[tmp_id] = []
	authors = pa['authors']
	for au in authors:
		tmp_au = 'a' + au.replace(' ','')
		paper2author[tmp_id].append(tmp_au)
		if tmp_au not in author2paper.keys():
			author2paper[tmp_au] = []
		author2paper[tmp_au].append(tmp_id)

for pa in papers:
	paper2refer['v'+paper2num[pa['id']]] = []
	if 'references' in pa.keys():
		refer = pa['references']
	else:
		continue
	if refer == []:
		continue
	for re in refer:
		if re in paper2num.keys():
			tmp_re = 'v'+paper2num[re]
			paper2refer['v'+paper2num[pa['id']]].append(tmp_re)

numwalks = 40
walklength = 10
outfilename = 'output.dbis.w40.l10.txt'
outfile = open(outfilename, 'w')
wyk = 0
for paper in paper2author.keys():
	tmp_paper = paper
	for i in range(numwalks):
		outline = tmp_paper
		for j in range(walklength):
			n = random.randint(0,1)
			if n and paper2refer[paper]:
				papers = paper2refer[paper]
				nump = len(papers)
				paperid = random.randrange(nump)
				paper = papers[paperid]
				outline += ' '+paper
			else:
				authors = paper2author[paper]
				numa = len(authors)
				authorid = random.randrange(numa)
				author = authors[authorid]
				outline += ' ' + author
				papers = author2paper[author]
				nump = len(papers)
				paperid = random.randrange(nump)
				paper = papers[paperid]
				outline += ' '+paper
		outfile.write(outline + "\n")
	wyk += 1
	print(wyk)
outfile.close()