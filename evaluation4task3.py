#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yikai Wang
"""
import random
import numpy as np
import pickle
import json
from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter

def AUC(task,nonexist,authors,times,node_vector,missing_edges,confs=None):
    if task == 'cp' or task == 're':
        n1 = 0
        n2 = 0
        for i in range(times):
            missing_edge = random.sample(missing_edges,1)[0]
            nonexist_edge = []
            while True:
                tmp1 = random.randint(0,len(authors)-1)
                tmp2 = random.randint(0,len(authors)-1)
                if tmp1 == tmp2 or (not nonexist[tmp1][tmp2]):
                    continue
                else:
                    if nonexist[tmp1][tmp2] and nonexist_edge == []:
                        nonexist_edge = [authors[tmp1],authors[tmp2]]
                if nonexist_edge != []:
                    break
            score_miss = np.sum(np.array(node_vector[missing_edge[0]])*np.array(node_vector[missing_edge[1]]))/(np.sum(np.array(node_vector[missing_edge[0]])**2)*np.sum(np.array(node_vector[missing_edge[1]])**2))**0.5
            score_none = np.sum(np.array(node_vector[nonexist_edge[0]])*np.array(node_vector[nonexist_edge[1]]))/(np.sum(np.array(node_vector[nonexist_edge[0]])**2)*np.sum(np.array(node_vector[nonexist_edge[1]])**2))**0.5
            if score_miss > score_none:
                n1 += 1
            elif score_miss == score_none:
                n2 += 1
        result = (n1+0.5*n2)/times
        print('Task cp/re eval AUC: '+str(result))
        return result
    if task == 'conf':
        n1 = 0
        n2 = 0
        for i in range(times):
            missing_edge = random.sample(missing_edges,1)[0]
            nonexist_edge = []
            while True:
                tmp1 = random.randint(0, len(authors) - 1)
                tmp2 = random.randint(0, len(confs) - 1)
                if tmp1 == tmp2 or (not nonexist[tmp1][tmp2]):
                    continue
                else:
                    if nonexist[tmp1][tmp2] and nonexist_edge == []:
                        nonexist_edge = [authors[tmp1], confs[tmp2]]
                if nonexist_edge!=[]:
                    break
            score_miss = np.sum(np.array(node_vector['author'][missing_edge[0]])*np.array(node_vector['conf'][missing_edge[1]]))/(np.sum(np.array(node_vector['author'][missing_edge[0]])**2)*np.sum(np.array(node_vector['conf'][missing_edge[1]])**2))**0.5
            score_none = np.sum(np.array(node_vector['author'][nonexist_edge[0]])*np.array(node_vector['conf'][nonexist_edge[1]]))/(np.sum(np.array(node_vector['author'][nonexist_edge[0]])**2)*np.sum(np.array(node_vector['conf'][nonexist_edge[1]])**2))**0.5
            if score_miss > score_none:
                n1 += 1
            elif score_miss == score_none:
                n2 += 1
        result = (n1+0.5*n2)/times
        print('Task conf eval AUC: '+str(result))
        return result

def Precision(task,nonexist,authors,L,node_vector,confs=None):
    if task == 'cp':
        k = 0
        non_observed_edges = []
        for i in range(len(authors)-1):
            for j in range(i+1, len(authors)):
                if k < L:
                    score = np.sum(np.array(node_vector[authors[i]])*np.array(node_vector[authors[j]]))/(np.sum(np.array(node_vector[authors[i]])**2)*np.sum(np.array(node_vector[authors[j]])**2))**0.5
                    non_observed_edges.append([[i,j],score])
                    k += 1
                else:
                    non_observed_edges.sort(key=lambda x: -x[1])
                    score = np.sum(np.array(node_vector[authors[i]]) * np.array(node_vector[authors[j]]))/(np.sum(np.array(node_vector[authors[i]])**2)*np.sum(np.array(node_vector[authors[j]])**2))**0.5
                    if score > non_observed_edges[-1][1]:
                        non_observed_edges[-1] = [[i,j],score]
        non_observed_edges.sort(key= lambda x: -x[1])
        Lr = 0
        for i in range(L):
            if not nonexist[non_observed_edges[i][0][0]][non_observed_edges[i][0][1]]:
                Lr += 1
        result = Lr/L
        print('Task cp eval Precision: '+str(result))
        return result
    if task == 're':
        k = 0
        non_observed_edges = []
        for i in range(len(authors)):
            for j in range(len(authors)):
                if i!=j:
                    if k<L:
                        score = np.sum(np.array(node_vector[authors[i]])*np.array(node_vector[authors[j]]))/(np.sum(np.array(node_vector[authors[i]])**2)*np.sum(np.array(node_vector[authors[j]])**2))**0.5
                        non_observed_edges.append([[i,j],score])
                        k += 1
                    else:
                        non_observed_edges.sort(key=lambda x: -x[1])
                        score = np.sum(np.array(node_vector[authors[i]]) * np.array(node_vector[authors[j]]))/(np.sum(np.array(node_vector[authors[i]])**2)*np.sum(np.array(node_vector[authors[j]])**2))**0.5
                        if score > non_observed_edges[-1][1]:
                            non_observed_edges[-1] = [[i, j], score]
        non_observed_edges.sort(key= lambda x: -x[1])
        Lr = 0
        for i in range(L):
            if not nonexist[non_observed_edges[i][0][0]][non_observed_edges[i][0][1]]:
                Lr += 1
        result = Lr/L
        print('Task re eval Precision: '+str(result))
        return result
    if task =='conf':
        k = 0
        non_observed_edges = []
        for i in range(len(authors)):
            for j in range(len(confs)):
                if k<L:
                    score = np.sum(np.array(node_vector['authors'][authors[i]])*np.array(node_vector['confs'][confs[j]]))/(np.sum(np.array(node_vector['authors'][authors[i]])**2)*np.sum(np.array(node_vector['confs'][confs[j]])**2))**0.5
                    non_observed_edges.append([[i,j],score])
                    k += 1
                else:
                    non_observed_edges.sort(key=lambda x: -x[1])
                    score = np.sum(np.array(node_vector['authors'][authors[i]]) * np.array(node_vector['confs'][confs[j]]))/(np.sum(np.array(node_vector['authors'][authors[i]])**2)*np.sum(np.array(node_vector['confs'][confs[j]])**2))**0.5
                    if score > non_observed_edges[-1][1]:
                        non_observed_edges[-1] = [[i,j],score]
        non_observed_edges.sort(key= lambda x: -x[1])
        Lr = 0
        for i in range(L):
            if not nonexist[non_observed_edges[i][0][0]][non_observed_edges[i][0][1]]:
                Lr += 1
        result = Lr/L
        print('Task conf eval Precision: '+str(result))
        return result


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

def load_txt_1(filename):
    txt = {}
    with open(filename,'r') as f:
        while True:
            tmp = f.readline()
            if not tmp:
                break
            tmp = tmp.split()
            txt[tmp[0]] = tmp[1]
    return txt

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
parser = ArgumentParser('evaluation',
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
parser.add_argument('--task', default='all',
                        help='cp/re/conf/all')
parser.add_argument('--AUC', default=True,
                        help='1 or 0')
parser.add_argument('--p', default=False,
                        help='1 or 0')
args = parser.parse_args()
if args.task=='cp' or args.task == 'all':
    #vectors = load_pickle('data/task3cp.pkl')
    #vectors = load_pickle('data/deepwalk_task3cp_vectors.pkl')
    #vectors = load_pickle('data/line_task3cp_vectors.pkl')
    #vectors = load_pickle('data/deepwalk_task3all_vectors.pkl')['author']
    vectors = load_pickle('data/line_task3all_vectors.pkl')['author']
    valid_id = load_txt('data/valid_id_4task3.txt')
    chosen_authors = list(vectors.keys())
    authors2num = dict()
    for i in range(len(chosen_authors)):
        authors2num[chosen_authors[i]]=i
    nonexist = np.ones((len(chosen_authors), len(chosen_authors)))
    papers = load_json('data/allpaper.txt')
    missing_edges= []
    for i in range(len(papers)):
        if str(i) in valid_id:
            authors = papers[i]['authors']
            new_authors = [au.replace(' ','') for au in authors]
            for i in range(len(new_authors)-1):
                if new_authors[i] in chosen_authors:
                    for j in range(i+1,len(authors)):
                        if new_authors[j] in chosen_authors:
                            nonexist[authors2num[new_authors[i]]][authors2num[new_authors[j]]]=0
                            nonexist[authors2num[new_authors[j]]][authors2num[new_authors[i]]]=0
                            missing_edges.append([new_authors[i],new_authors[j]])
    print('Finished Loading!Sample numbers: '+str(len(missing_edges)))
    if args.AUC!=False:
        AUC(task='cp',nonexist=nonexist,missing_edges=missing_edges,authors=chosen_authors,times=len(missing_edges),node_vector=vectors)
    if args.p!=False:
        Precision(task='cp',nonexist=nonexist,authors=chosen_authors,L=len(missing_edges),node_vector=vectors)
if args.task=='re' or args.task == 'all':
    #vectors = load_pickle('data/task3re.pkl')
    #vectors = load_pickle('data/deepwalk_task3re_vectors.pkl')
    #vectors = load_pickle('data/line_task3re_vectors.pkl')
    #vectors = load_pickle('data/deepwalk_task3all_vectors.pkl')['author']
    vectors = load_pickle('data/line_task3all_vectors.pkl')['author']
    valid_id = load_txt('data/valid_id_4task3.txt')
    id2num = load_txt_1('data/id2num.txt')
    chosen_authors = list(vectors.keys())
    authors2num = dict()
    for i in range(len(chosen_authors)):
        authors2num[chosen_authors[i]]=i
    nonexist = np.ones((len(chosen_authors), len(chosen_authors)))
    papers = load_json('data/allpaper.txt')
    missing_edges= []
    for i in range(len(papers)):
        if str(i) in valid_id:
            authors = papers[i]['authors']
            new_authors = [au.replace(' ','') for au in authors]
            new_authors = [au for au in new_authors if au in chosen_authors]
            re_authors = []
            if 'references' in papers[i].keys():
                if papers[i]['references']!=[]:
                    for reference in papers[i]['references']:
                        if reference in id2num.keys():
                            tmp_au = papers[int(id2num[reference])]['authors']
                            new_tmp_au = [au.replace(' ','') for au in tmp_au]
                            new_tmp_au = [au for au in new_tmp_au if au in chosen_authors]
                            re_authors += new_tmp_au
            for i in range(len(new_authors)):
                for j in range(len(re_authors)):
                    nonexist[authors2num[new_authors[i]]][authors2num[re_authors[j]]]=0
                    missing_edges.append([new_authors[i],re_authors[j]])
    print('Finished Loading!Sample numbers: '+str(len(missing_edges)))
    if args.AUC!=False:
        AUC(task='re',nonexist=nonexist,missing_edges=missing_edges,authors=chosen_authors,times=len(missing_edges),node_vector=vectors)
    if args.p!=False:
        Precision(task='re',nonexist=nonexist,authors=chosen_authors,L=len(missing_edges),node_vector=vectors)
if args.task =='conf' or args.task == 'all':
    CONFS = ['PPOPP', 'PACT', 'IPDPS', 'ICPP',
         'IJCAI', 'ICML', 'NIPS',
         'ICDE', 'SIGMOD', 'KDD', 'ICDM',
         'AIED', 'ITS', 'ICALT',
         'ACL', 'EACL', 'COLING', 'EMNLP',
         'MASCOTS', 'SOSP', 'OSDI']
    #vectors = load_pickle('data/task3conf.pkl')
    #vectors = load_pickle('data/deepwalk_task3conf_vectors.pkl')
    #vectors = load_pickle('data/line_task3conf_vectors.pkl')
    #vectors = load_pickle('data/deepwalk_task3all_vectors.pkl')
    vectors = load_pickle('data/line_task3all_vectors.pkl')
    valid_id = load_txt('data/valid_id_4task3.txt')
    id2num = load_txt_1('data/id2num.txt')
    chosen_authors = list(vectors['author'].keys())
    chosen_confs = list(vectors['conf'].keys())
    nonexist = np.ones((len(chosen_authors),len(chosen_confs)))
    authors2num = dict()
    missing_edges = []
    for i in range(len(chosen_authors)):
        authors2num[chosen_authors[i]]=i
    for i in range(len(CONFS)):
        tmp = load_json('data/papers/'+CONFS[i]+'.txt')
        for j in range(len(tmp)):
            if id2num[tmp[j]['id']] in valid_id:
                authors = tmp[j]['authors']
                for au in authors:
                    tmp_au = au.replace(' ','')
                    if tmp_au in chosen_authors:
                        nonexist[authors2num[tmp_au]][i] = 0
                        missing_edges.append([tmp_au,CONFS[i]])
    print('Finished Loading!Sample numbers: '+str(len(missing_edges)))
    if args.AUC!=False:
        AUC(task='conf', nonexist=nonexist,authors=chosen_authors, times=len(missing_edges),
        node_vector=vectors,confs=CONFS,missing_edges=missing_edges)
    if args.p!=False:
        Precision(task='conf', nonexist=nonexist,authors=chosen_authors, L=len(missing_edges),
              node_vector=vectors,confs=CONFS)










