# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:29:44 2015

@author: Yuhlin
"""

from sklearn.datasets import load_iris
from itertools import cycle
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from numpy.random import RandomState
import pylab as pl
from scipy.spatial import distance

   
def calculate_IV_EV(features, labels):
    index1 = index2 = 0
    N = 0
    IV = EV = 0
    for point1 in features:
        for point2 in features:
           # if (point1[0] != point2[0]) or (point1[1] != point2[1]):
            if (index1 != index2):
                if (labels[index1] == labels[index2]):
                    IV += distance.euclidean(point1, point2)
                else:
                    EV += distance.euclidean(point1, point2)
                    N += 1
            index2 += 1
        index1 += 1
        index2 = 0
    EV /= N
    print "N =", N, "IV =", IV, "EV =", EV, "Quality =", IV/EV

def plot_2D(data, target, target_names, title="Scatter Plot"):
    # print title
    colors = cycle('rgbcmykw')
    target_ids = range(len(target_names))
    pl.figure()
    for i, c, label in zip(target_ids, colors, target_names):
        pl.scatter(data[target == i, 0], data[target == i, 1],
                    c=c, label=label)
    pl.legend()
    pl.title(title)
    pl.show()
    pl.close()

class clustering:
    def __init__(self):
        self.plot1(load_iris().data)
        self.plot2(load_iris().data)
        self.plot3(load_iris().data)

    def plot1(self, X):
        pca = PCA(n_components=2, whiten=True).fit(X)
        X_pca = pca.transform(X)
        kmeans = KMeans(n_clusters=3, random_state=RandomState(42)).fit(X_pca)
        plot_2D(X_pca, kmeans.labels_, ["c0", "c1", "c2"], "Scatter Plot: Features-PCA")
        calculate_IV_EV(X_pca, kmeans.labels_)

    def plot2(self, X):
        X_01 = X[:, [0,1]]
        kmeans = KMeans(n_clusters=3, random_state=RandomState(42)).fit(X_01)
        plot_2D(X_01, kmeans.labels_, ["c0", "c1", "c2"], "Scatter Plot: Features-0-1")
        calculate_IV_EV(X_01, kmeans.labels_)

    def plot3(self, X):
        X_23 = X[:, [2,3]]
        kmeans = KMeans(n_clusters=3, random_state=RandomState(42)).fit(X_23)
        plot_2D(X_23, kmeans.labels_, ["c0", "c1", "c2"], "Scatter Plot: Features-2-3")
        calculate_IV_EV(X_23, kmeans.labels_)

if __name__ == '__main__':
    c = clustering()