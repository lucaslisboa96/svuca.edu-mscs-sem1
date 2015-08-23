# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:33:52 2015

@author: Yuhlin
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
from sklearn.metrics import confusion_matrix

digits = datasets.load_digits()
print(digits.data)
print(digits.target)
# clf = svm.SVC()
clf = svm.SVC(gamma=0.001, C=100)
X,y = digits.data[:-10], digits.target[:-10]
clf.fit(X,y)
print(clf.predict(digits.data[-5]))
plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

iris = datasets.load_iris()

clf = svm.SVC().fit(iris.data, iris.target)
clf_pred = clf.predict(iris.data)
print confusion_matrix(clf_pred, iris.target)
# [[50  0  0]
#  [ 0 48  2]
#  [ 0  0 50]]