import numpy as np
from sklearn.cluster import KMeans,MeanShift,DBSCAN,Birch
import pickle

def load_pickle():
    pkl_file = open('wordvec.pkl', 'rb')
    data1 = pickle.load(pkl_file)
    pkl_file.close()
    return data1


def write_in_pickle(data,name):
    output = open('cluster_'+name+'_nrl.pkl', 'wb')
    pickle.dump(data, output)
    output.close()


def list2dict(result,labels,name):
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
        self.n_clusters = n_clusters
        self.id = []
        self.features = []
        for i in data:
            self.id.append(i[0])
            self.features.append(i[1])

    def feature_to_result(self, feature):
        result = []
        for i in range(len(self.id)):
            result.append([self.id[i],feature[i]])
        return result

    def method_KMeans(self):
        clf = KMeans(n_clusters=self.n_clusters,max_iter=1000000)
        result = clf.fit(self.features)
        print('Finish result')
        return [self.feature_to_result(result.labels_), list(range(self.n_clusters))]

    def method_DBSCAN(self):
        clf = DBSCAN(min_samples=5000,eps=1,n_jobs=-1)
        result = clf.fit(self.features)
        print('Finish result')
        return self.feature_to_result(result.labels_)

    def method_MeanShift(self):
        clf = MeanShift(n_jobs=-1)
        result = clf.fit(self.features)
        print('Finish result')
        return [self.feature_to_result(result.labels_), list(set(result.labels_))]

    def method_Birch(self):
        clf = Birch(n_clusters=self.n_clusters)
        result = clf.fit(self.features)
        print('Finish result')
        return [self.feature_to_result(result.labels_), list(range(self.n_clusters))]


# a = load_pickle()
# data = [[k,(v[0]+v[1])/2] if np.sum(v[1]) != 0 else [k, v[0]] for k,v in a.items()]
a = np.load('model_line.npy')
data = [[i,a[i]] for i in range(len(a))]
print('Finish Data preprocessing')
c = Clustering(data,6)
# [result, labels] = c.method_KMeans()
# list2dict(result, labels,'KMeans')
# [result, labels] = c.method_MeanShift()
# list2dict(result, labels,'MeanShift')
[result, labels] = c.method_Birch()
list2dict(result, labels,'Birch')
# [result, labels] = c.method_DBSCAN()
# list2dict(result, labels,'DBSCAN')


