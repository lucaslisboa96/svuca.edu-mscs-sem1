from sklearn.datasets import load_iris
from itertools import cycle
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from numpy.random import RandomState

import pylab as pl
import scipy



class clustering:

    def __init__(self):
        self.plot(load_iris().data)

    def plot(self, X):
        X_dataset = []
        X_dataset.append(PCA(n_components=2, whiten=True).fit(X).transform(X))
        X_dataset.append(X[:,:2])
        X_dataset.append(X[:,2:])
        
        
        print "\n\n\nPlotting of k-means clustering results for PCA, features (1,2), and features(3,4) subsequently: "
        for Xi in X_dataset:
            kmeans = KMeans(n_clusters=3,random_state=RandomState(42)).fit(Xi)
            self.plot_2D(Xi, kmeans.labels_, ['c0', 'c1', 'c2'])
            IV = self.calculate_IV(Xi)
            
            
    def plot_2D(self, data, target, target_names):
        colors = cycle('rgbcmykw')
        target_ids = range(len(target_names))
        pl.figure()
        for (i, c, label) in zip(target_ids, colors, target_names):
            pl.scatter(data[target == i, 0], data[target == i, 1], c=c,
                       label=label)
        pl.legend()
        pl.show()
        

    def calculate_IV(self, dataset):
        distance = 0
        for i in range(0, len(dataset)-1):
            for j in range(i+1, len(dataset)-1):
                #use euclidean distance
                distance += scipy.spatial.distance.euclidean(dataset[i], 
                                                             dataset[j])                                                              
        return distance                



if __name__ == '__main__':
    c = clustering()
