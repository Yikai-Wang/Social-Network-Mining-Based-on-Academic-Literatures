import numpy as np
from sklearn.cluster import KMeans,MeanShift,DBSCAN,Birch
import pickle

def load_pickle():
    pkl_file = open('data1.pkl', 'rb')
    data1 = pickle.load(pkl_file)
    pkl_file.close()
    return data1

def write_in_pickle(data):
    output = open('cluster_DBSCAN.pkl', 'wb')
    pickle.dump(data, output)
    output.close()

class Clustering():

    def __init__(self,data,n_clusters,max_iter):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
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
        clf = KMeans(n_clusters=self.n_clusters,max_iter=self.max_iter)
        result = clf.fit(self.features)
        print('Finish result')
        pred = result.fit_predict(self.features)
        print('Finish pred')
        return self.feature_to_result(pred)

    def method_DBSCAN(self):
        clf = DBSCAN(min_samples=10000,eps=1,n_jobs=-1)
        result = clf.fit(self.features)
        print('Finish result')
        pred = result.fit_predict(self.features)
        print('Finish pred')
        return self.feature_to_result(pred)

    def method_MeanShift(self):
        clf = MeanShift(n_jobs=-1)
        result = clf.fit(self.features)
        print('Finish result')
        pred = result.fit_predict(self.features)
        print('Finish pred')
        return self.feature_to_result(pred)

    def method_Birch(self):
        clf = Birch(n_clusters=self.n_clusters)
        result = clf.fit(self.features)
        print('Finish result')
        pred = result.fit_predict(self.features)
        print('Finish pred')
        return self.feature_to_result(pred)


a = load_pickle()
data = [[k,(v[0]+v[1])/2] if np.sum(v[1]) != 0 else [k, v[0]] for k,v in a.items()]
print('Finish Data preprocessing')
c = Clustering(data,10,100000)
# result = c.method_KMeans()
#result = c.method_DBSCAN()
result = c.method_MeanShift()
for_wooden = {}
for i in result:
    for_wooden[i[0]]=i[1]
write_in_pickle(for_wooden)
print('Finish Data saving')
tmp = list(for_wooden.values())
tmp = np.array(tmp)
print([sum(tmp==i) for i in range(10)])
# result = c.method_DBSCAN()
# c.method_MeanShift()
# c.method_Birch()
