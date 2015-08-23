# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:57:16 2015

@author: stevenvo
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:00:27 2015

@author: Yuhlin
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# HW4-Q2
#COLOR_N = 'r'
#COLOR_P = 'b'
#negative = np.array([[1, 1], [-1, -1]])
#positive = np.array([[-1, 1], [1, -1]])
#fig, ax = plt.subplots()
#listP = positive.tolist()
#x, y = zip(*listP)
#ax.scatter(x, y, c=COLOR_P)
#listN = negative.tolist()
#x, y = zip(*listN)
#ax.scatter(x, y, c=COLOR_N)
##plt.plot([-2, 4], [6, 0], color='k', linestyle='-', linewidth=1)
#for point in positive.tolist() + negative.tolist():
#    ax.annotate(np.array_str(np.array(point)), point)
##ax.annotate('y = -x + 4', [-2, 6])
#plt.show()

#X = np.array([[1,2],
#             [3,4],
#             [1,4],
#             [7,8],
#             [9,10],
#             [9,8]])
#y = [0,0,0,1,1,1]
#clf = svm.SVC(kernel='linear', C = 10.0)
#clf.fit(X,y)
#
#h = .02
## create a mesh to plot in
#x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
#y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
#xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                     np.arange(y_min, y_max, h))
#
#Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#Z = Z.reshape(xx.shape)
#plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
#plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
#plt.xlabel('Sepal length')
#plt.ylabel('Sepal width')
#plt.xlim(xx.min(), xx.max())
#plt.ylim(yy.min(), yy.max())
#plt.xticks(())
#plt.yticks(())
#plt.show()
#w = clf.coef_[0]
#print(w)



#X = np.array([[1,2],
#             [5,8],
#             [1.5,1.8],
#             [8,8],
#             [1,0.6],
#             [9,11]])
#y = [0,1,0,1,0,1]

X = np.array([
[1,1], [-1,-1], [-1,1], [1,-1]
])
y = [-1,-1,1,1]
clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)

w = clf.coef_[0]
a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]
h0 = plt.plot(xx, yy, 'k-', label="")
# plot the parallels to the separating hyperplane that pass through the
    # support vectors
margin = 2 / np.sqrt(np.sum(clf.coef_ ** 2))
yy_down = yy + a * margin
yy_up = yy - a * margin
#fignum = 1
#plt.figure(fignum, figsize=(2, 1))
plt.clf()
plt.plot(xx, yy, 'k-')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')

plt.scatter(X[:, 0], X[:, 1], c = y, cmap=plt.cm.Paired)
plt.show()


print("coefficients: {0}".format(w))
print("margin: {0}".format(margin))
print("clf.coef_: {0}".format(clf.coef_))