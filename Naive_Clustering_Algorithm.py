#Input: List with each row as [id, vectors]
#Output: List with each row as [id, class]
import numpy as np
from sklearn.cluster import KMeans,MeanShift,DBSCAN,Birch

class Clustering():

    def __init__(self,data,n_clusters,max_iter):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.id = []
        self.features = []
        for i,f in data:
            self.id.append(i)
            self.features.append(f)

    def feature_to_result(self,feature):
        result = []
        for i in range(len(self.id)):
            result.append(self.id[i],feature[i])
        return result

    def method_KMeans(self):
        clf = KMeans(n_clusters=self.n_clusters,max_iter=self.max_iter)
        result = clf.fit(self.features)
        print(result)
        print(clf.cluster_centers_)
        print(clf.labels_)
        print(clf.inertia_)
        return result

    def method_DBSCAN(self):
        clf = DBSCAN(eps=0.3,min_samples=self.n_clusters)
        result = clf.fit(self.features)
        pred = clf.fit_predict(self.features)
        print(result)
        print(clf.labels_)
        return self.feature_to_result(clf.labels_)

    def method_MeanShift(self):
        clf = MeanShift()
        result = clf.fit(self.features)
        print(result)
        print(clf.cluster_centers_)
        print(clf.labels_)
        return self.feature_to_result(clf.labels_)

    def method_Birch(self):
        clf = Birch(n_clusters=self.n_clusters)
        result = clf.fit(self.features)
        print(result)
        print(clf.labels_)
        return self.feature_to_result(clf.labels_)


data = [[i,np.random.randint(0,10,10)] for i in range(1000)]
c = Clustering(data,5,10000)
#result = c.method_KMeans()
#result = c.method_DBSCAN()
#c.method_MeanShift()
c.method_Birch()