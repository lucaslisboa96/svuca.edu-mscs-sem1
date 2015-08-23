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

class clustering:
	def __init__(self):
		self.plot(load_iris().data)

	def plot(self, X):
		pca = PCA(n_components=2, whiten=True).fit(X)
		X_pca = pca.transform(X)
		kmeans = KMeans(n_clusters=3, random_state=RandomState(42)).fit(X_pca)
		plot_2D(X_pca, kmeans.labels_, ["c0", "c1", "c2"])

def plot_2D(data, target, target_names):
	colors = cycle('rgbcmykw')
	target_ids = range(len(target_names))
	pl.figure()
	for i, c, label in zip(target_ids, colors, target_names):
		pl.scatter(data[target == i, 0], data[target == i, 1],
					c=c, label=label)
	pl.legend()
	pl.show()

if __name__ == '__main__':
	c = clustering()