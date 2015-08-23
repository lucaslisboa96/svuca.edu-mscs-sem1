# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:00:27 2015

@author: Yuhlin
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

#COLOR_N = 'r'
#COLOR_P = 'b'
#negative = np.array([[1, 5], [1, 6], [3, 3]])
#positive = np.array([[-1, 3], [0, 2], [0, 1], [0, 0]])
#fig, ax = plt.subplots()
#listP = positive.tolist()
#x, y = zip(*listP)
#ax.scatter(x, y, c=COLOR_P)
#listN = negative.tolist()
#x, y = zip(*listN)
#ax.scatter(x, y, c=COLOR_N)
#plt.plot([-2, 4], [6, 0], color='k', linestyle='-', linewidth=1)
#for point in positive.tolist() + negative.tolist():
#    ax.annotate(np.array_str(np.array(point)), point)
#ax.annotate('y = -x + 4', [-2, 6])
#plt.show()

X = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11]])
y = [0,1,0,1,0,1]
clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)
print(clf.predict([0.58,0.76]))
w = clf.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]
h0 = plt.plot(xx, yy, 'k-', label="non weighted div")
plt.scatter(X[:, 0], X[:, 1], c = y)
plt.legend()
plt.show()
