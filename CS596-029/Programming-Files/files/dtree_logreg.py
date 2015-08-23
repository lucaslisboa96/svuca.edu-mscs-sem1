# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 15:20:58 2015

@author: Yuhlin
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree, linear_model

sample = np.array([[66,170,0], [73,210,0], [72,165,0], [70,180,0], [74,185,0], [68,155,0],
                   [65,150,1], [64,120,1], [63,125,1], [67,140,1], [68,165,1], [66,130,1]])
X = sample[:,:-1]
Y = sample[:,-1]

# decision tree
print "Decision Tree:"
# Train
clf = tree.DecisionTreeClassifier()
clf.fit(X, Y)

dotfile = open('tree_d1.dot', 'w')
tree.export_graphviz(clf.tree_, out_file=dotfile, feature_names="height+weight")  #export the tree to .dot file
dotfile.close() #close that dot file.

#
#
# try logistic regression
h = .02  # step size in the mesh
logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X, Y)
# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(4, 3))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('height')
plt.ylabel('weight')

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())

plt.show()