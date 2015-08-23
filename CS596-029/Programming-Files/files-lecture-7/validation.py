# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:05:12 2015

@author: Yuhlin
"""

import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

# hold out
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
            iris.data, iris.target, test_size=0.4, random_state=0)
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print clf.score(X_test, y_test)

# illustrate KFold
X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]]) #input
y = np.array([1, 2, 3, 4]) #output
kf = cross_validation.KFold(4, n_folds=2) # 50% Training, 50% Testing
for train_index, test_index in kf:
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

# f measure    
y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]

print f1_score(y_true, y_pred, average='macro')  #skew the result base on the different combination, one combination can take more weight than the other
print f1_score(y_true, y_pred, average='micro')  
print f1_score(y_true, y_pred, average='weighted')
print f1_score(y_true, y_pred, average=None)
print confusion_matrix(y_true, y_pred)