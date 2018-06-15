#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yikai Wang
"""
#This file load the txt file metapath2vec generates and save the data into a dict.
import numpy as np
import pickle
def load_txt(filename):
    """
    load txt file
    :param filename: path we save the data.
    :return: data as a dictionary.
    """
    txt = {}
    with open(filename,'r') as f:
        while True:
            tmp = f.readline()
            if not tmp:
                break
            tmp = tmp.split(' ')
            if tmp[0][0]=='a':
                k = tmp[0][1:]
                v = []
                for i in range(1,len(tmp)-1):
                    v.append(np.float(tmp[i]))
                txt[k] = v
    return txt

def write_in_pickle(data, path):
    """
    save the data as a pkl file
    :param data: data we need to save
    :param path: path we want to save
    :return: nothing
    """
    output = open(path, 'wb')
    pickle.dump(data, output)
    output.close()

def load_pickle(path):
    """
    load pkl file
    :param path: path we save the data
    :return: data as a dictionary.
    """
    pkl_file = open(path, 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data
# def load_txt(filename):
#     txt = {'conf':{},'author':{}}
#     with open(filename,'r') as f:
#         while True:
#             tmp = f.readline()
#             if not tmp:
#                 break
#             tmp = tmp.split(' ')
#             if tmp[0][0]=='a':
#                 k = tmp[0][1:]
#                 v = []
#                 for i in range(1,len(tmp)-1):
#                     v.append(np.float(tmp[i]))
#                 txt['author'][k] = v
#             if tmp[0][0]=='v':
#                 k = tmp[0][1:]
#                 v = []
#                 for i in range(1,len(tmp)-1):
#                     v.append(np.float(tmp[i]))
#                 txt['conf'][k] = v
#     return txt
txt = load_txt('task3re.vector.txt')
# result = np.array([])
# for k,v in txt.items():
#     np.append(result,np.array([k,v]))
write_in_pickle(txt,'task3re.pkl')