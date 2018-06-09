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
train_author2conf = dict()
train_conf2author = dict()
for conf in CONFS:
    tmp = load_json('papers/'+conf+'.txt')
    train_conf2author['v'+conf] = []
    for i in range(len(tmp)):
        if int(tmp[i]['year']) < 2012:
            authors = tmp[i]['authors']
            for au in authors:
                tmp_au = 'a' + au.replace(' ','')
                train_conf2author['v' + conf].append(tmp_au)
                if tmp_au not in train_author2conf.keys():
                    train_author2conf[tmp_au] = []
                train_author2conf[tmp_au].append('v'+conf)

      
numwalks = 40
walklength = 10
outfilename = 'task3conf.w40.l10.txt'
outfile = open(outfilename, 'w')
wyk = 0
for author in train_author2conf.keys():
    tmp_author = author
    for i in range(numwalks):
        outline = tmp_author
        for j in range(walklength):
            confs = train_author2conf[author]
            numc = len(confs)
            confid = random.randrange(numc)
            conf = confs[confid]
            outline += ' '+conf
            authors = train_conf2author[conf]
            numa = len(authors)
            authorid = random.randrange(numa)
            author = authors[authorid]
            outline += ' ' + author
        outfile.write(outline + "\n")
    wyk += 1
    print(wyk)
outfile.close()