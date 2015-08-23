# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:23:11 2015

@author: Yuhlin
"""

import numpy as np
from sklearn import linear_model
from sklearn import metrics

X=np.array([[3,5,2],
            [5,5,5],
            [3,0,2],
            [3,4,1],
            [5,0,2],
            [2,1,3],
            [4,3,1],
            [2,5,1],
            [0,2,1],
            [2,1,5]])
C=np.array([0,0,0,0,0,1,1,1,1,1]) # class labels
print "Example data - 3 features, last column is label"
print np.hstack((X,np.transpose(np.atleast_2d(C))))
W=1.0/len(C)*np.ones(C.shape[0])
print "Initial weights"
print W
M=5 #Number of iterations
reg=linear_model.LogisticRegression()
bestClassifier=np.zeros((M,3)) # Array to store 1.)best feature, 2.)threshold, 3.)alpha of best classifier in each iteration
for F in range(M):
    print "\n\n"
    print "#"*30
    print "Start of Iteration %d"%F
    IndicatorList=[]
    betaList=[]
    thresholdList=[]
    bestVal=10
    bestFeat=10
    for i in range(X.shape[1]):
        print "\nClassification with respect to feature %d"%i
        indata= np.transpose(np.atleast_2d(X[:,i]))
        reg.fit(indata,C)
        threshold=-1*reg.intercept_/reg.coef_
        print "Threshold = ",threshold
        CE=reg.predict(indata)
        print "target :     ",C
        print "predicted :  ",CE
        Indicator = np.abs(CE-C)
        errors=np.dot(Indicator,W)
        print "J =",errors
        if errors < bestVal:
            bestVal=errors
            bestFeat=i
        J=errors
        beta=1.0*J/(1-J)
        IndicatorList.append(Indicator)
        betaList.append(beta)
        thresholdList.append(threshold)
        print '-'*30

    I=IndicatorList[bestFeat]
    beta= betaList[bestFeat]
    threshold=thresholdList[bestFeat]
    alpha=np.log(1.0/beta)
    print "BestFeature:          ",bestFeat
    print "Threshold =           ",threshold
    print "Best Beta =           ",beta
    print "Corresponding alpha = ",alpha
    bestClassifier[F,:]=np.array([bestFeat,threshold,alpha])
    for r in range(C.shape[0]):
        W[r]=W[r]*np.power(beta,1-I[r])
    Wnorm=np.sum(W)
    W=W/Wnorm
    print "New weights for training samples: "
    print W
    print "#"*30
    print"\n\n"
    print "*"*50
        
print "Best Classifiers in each iteration:"
print "Feature|Threshold|Alpha"
print bestClassifier
halfSumAlpha=0.5*np.sum(bestClassifier[:,2])
print "Threshold of combined Classifier  :  ",halfSumAlpha
newdata=np.array([[1,5,1],[2,10,2],[5,3,1]])
for u in range(newdata.shape[0]):
    data=newdata[u,:]
    sum=0
    for v in range(M):
        if newdata[u,bestClassifier[v,0]] > bestClassifier[v,1]:
            sum=sum+bestClassifier[v,2]
    print "Data : ",newdata[u,:]
    if sum > halfSumAlpha:
        print "Classified as Class 0"
    else:
        print "Classified as Class 1"