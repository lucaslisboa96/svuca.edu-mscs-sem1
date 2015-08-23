# -*- coding: utf-8 -*-
"""
========================================================
Created on Fri Jul 03 11:32:24 2015

@course:       CS596-029 - Data Mining and Machine Learning
@student_name: VO, Doan Quoc Sy
@student_id:   150201133
@homework:     3
========================================================

"""
print(__doc__)

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
        
        # An array storing 3 datasets of X: PCA, Features(1,2), and Features(3,4)
        datasets = [
            {'title': 'Using PCA','data': PCA(n_components=2, whiten=True).fit(X).transform(X)},
            {'title': 'Using features (1,2)','data': X[:,:2]},
            {'title': 'Using features (3,4)','data': X[:,2:]}
        ]
        
        #Iterate through 3 types of dataset
        for ds in datasets:            
            title = ds['title']
            X = ds['data']
            
            #Calculate Kmeans and start plotting
            kmeans = KMeans(n_clusters=3,random_state=RandomState(42)).fit(X)
            self.plot_2D(X, kmeans.labels_, ['c0', 'c1', 'c2'], title)
            
            #IV, EV, CQ calculation
            IV = self.calculate_IV(X)
            EV = self.calculate_EV(X, kmeans.labels_)
            CQ = IV / EV
            print "IV: %.4f" % IV
            print "EV: %.4f " % EV
            print "CQ: %.4f\n" % CQ
            
            
    def plot_2D(self, data, target, target_names, chart_name):        
        colors = cycle('rgbcmykw')
        target_ids = range(len(target_names))
        pl.figure()
        for (i, c, label) in zip(target_ids, colors, target_names):
            pl.scatter(data[target == i, 0], data[target == i, 1], c=c,
                       label=label)
        pl.legend()
        pl.suptitle(chart_name)
        pl.show()
        

    def calculate_IV(self, dataset):
        result = 0
        for i in range(0, len(dataset)):
            for j in range(i+1, len(dataset)):
                #use euclidean distance
                result += scipy.spatial.distance.euclidean(dataset[i], dataset[j])                                                              
        return result                
    
    
    def calculate_EV(self, data, target):
        result = 0
        count = 0
        for i in range(0, len(data)):
            for j in range (i+1, len(data)):
                if target[i] != target[j]: #2 points must come from DIFFERENT clusters
                    result += scipy.spatial.distance.euclidean(data[i], data[j])
                    count += 1
        result = result / count
        return result
        


if __name__ == '__main__':
    c = clustering()
