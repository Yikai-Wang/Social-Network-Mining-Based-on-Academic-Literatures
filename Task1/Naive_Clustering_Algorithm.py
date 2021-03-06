#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yikai Wang
"""
#Using KMeans and Birch to cluster.
import numpy as np
from sklearn.cluster import KMeans,MeanShift,DBSCAN,Birch
import pickle
from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter

def load_pickle():
    """
    load wordvec.pkl
    :return: wordvec as a dictionary.
    """
    pkl_file = open('wordvec.pkl', 'rb')
    data1 = pickle.load(pkl_file)
    pkl_file.close()
    return data1


def write_in_pickle(data,name):
    """
    :param data: data we need to save
    :param name: the filename
    :return: nothing
    """
    output = open('cluster_'+name+'_nrl.pkl', 'wb')
    pickle.dump(data, output)
    output.close()


def list2dict(result,labels,name):
    """
    :param result: result of clustering
    :param labels: the label set in the clustering
    :param name: filename
    :return: nothing
    """
    for_wooden = {}
    for i in result:
        for_wooden[i[0]]=i[1]
    write_in_pickle(for_wooden,name)
    print('Finish Data saving')
    tmp = list(for_wooden.values())
    tmp = np.array(tmp)
    print('Number of each class:')
    print(labels)
    print([sum(tmp == i) for i in labels])


class Clustering():

    def __init__(self,data,n_clusters):
        """
        :param data: vectors of data and its number.
        :param n_clusters: number of cluster set.
        """
        self.n_clusters = n_clusters
        self.id = []
        self.features = []
        for i in data:
            self.id.append(i[0])
            self.features.append(i[1])

    def feature_to_result(self, feature):
        """
        save the cluster result.
        :param feature: the labels we get.
        :return: each id with its cluster result.
        """
        result = []
        for i in range(len(self.id)):
            result.append([self.id[i],feature[i]])
        return result

    def method_KMeans(self):
        """
        Using KMeans to cluster
        :return: id with label and all label.
        """
        clf = KMeans(n_clusters=self.n_clusters,max_iter=1000000)
        result = clf.fit(self.features)
        print('Finish result')
        return [self.feature_to_result(result.labels_), list(range(self.n_clusters))]

    def method_DBSCAN(self):
        """
        Using DBSCAN to cluster
        :return: id with label and all label.
        """
        clf = DBSCAN(min_samples=5000,eps=1,n_jobs=-1)
        result = clf.fit(self.features)
        print('Finish result')
        return self.feature_to_result(result.labels_)

    def method_MeanShift(self):
        """
        Using MeanShift to cluster
        :return: id with label and all label.
        """
        clf = MeanShift(n_jobs=-1)
        result = clf.fit(self.features)
        print('Finish result')
        return [self.feature_to_result(result.labels_), list(set(result.labels_))]

    def method_Birch(self):
        """
        Using Birch to cluster
        :return: id with label and all label.
        """
        clf = Birch(n_clusters=self.n_clusters)
        result = clf.fit(self.features)
        print('Finish result')
        return [self.feature_to_result(result.labels_), list(range(self.n_clusters))]

parser = ArgumentParser('NCA',
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
parser.add_argument('--model', default='line',
                        help='Embedding model to use. Could be deepwalk,node2vec,line,metapath2vec,')
parser.add_argument('--mixture', default=False,
                        help='Using word2vec or not.')
parser.add_argument('--KMeans', default=True,
                        help='Using KMeans or not.')
parser.add_argument('--Birch', default=True,
                        help='Using Birch or not.')
parser.add_argument('--classes', default=6,
                        help='Number of classes.')
args = parser.parse_args()
if args.model == 'word2vec':
    w2v = load_pickle()
    #data = [[k,(v[0]+v[1])/2] if np.sum(v[1]) != 0 else [k, v[0]] for k,v in w2v.items()]
    data = [[k,v]for k,v in w2v.items()]
else:
    n2v = np.load('model_'+args.model+'.npy')
    data = [[i,n2v[i]] for i in range(67581)]
if args.mixture:
    args.model += '_word2vec'
    w2v = load_pickle()
    mix_data = []
    for i in range(len(data)):
        tmp = data[i][1]
        tmp = np.append(tmp,w2v[i])
        mix_data.append([i,tmp])
    data = mix_data
print('Finish Data preprocessing')
cluster = Clustering(data,args.classes)
if args.KMeans==True:
    [result, labels] = cluster.method_KMeans()
    list2dict(result, labels,'KMeans_'+args.model)
if args.Birch==True:
    [result, labels] = cluster.method_Birch()
    list2dict(result, labels,'Birch'+args.model)


