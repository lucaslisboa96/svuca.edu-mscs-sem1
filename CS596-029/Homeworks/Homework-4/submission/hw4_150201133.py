import numpy as np
from sklearn.ensemble import RandomForestClassifier

print """Question 5)
a) For targets = [1 1 1 0 0 0 1 1 1 1], what is the accuracy of the random forest?
"""

X = np.array([
    [0.1, 0.1],
    [0.2, 0.2],
    [0.3, 0.3],
    [0.4, 0.4],
    [0.5, 0.5],
    [0.6, 0.6],
    [0.7, 0.7],
    [0.8, 0.8],
    [0.9, 0.9],
    [1.0, 1.0],
])
Y = [1,1,1,0,0,0,1,1,1,1]
print "X:\n{0}".format(X)
print "Y:\n{0}".format(Y)
clf = RandomForestClassifier(n_estimators=9)
clf = clf.fit(X, Y)
print "Accuracy: {0}".format(clf.score(X, Y))


print """
b) For targets = [1 1 1 0 0 0 0 0 1 1], what is the accuracy of the random forest?
"""
X = np.array([
    [0.1, 0.1],
    [0.2, 0.2],
    [0.3, 0.3],
    [0.4, 0.4],
    [0.5, 0.5],
    [0.6, 0.6],
    [0.7, 0.7],
    [0.8, 0.8],
    [0.9, 0.9],
    [1.0, 1.0],
])
Y = [1,1,1,0,0,0,0,0,1,1]
print "X:\n{0}".format(X)
print "Y:\n{0}".format(Y)
clf = RandomForestClassifier(n_estimators=9)
clf = clf.fit(X, Y)
print "Accuracy: {0}".format(clf.score(X, Y))
X = [np.linspace(0.9, 0.1, num=10), np.linspace(0.1, 0.9, num=10)]
X = np.array(X)
X = np.transpose(X)
X = np.round(X, 1)


print """
d) Given the test data as follows, what are the prediction from the random forest classifier trained using the targets in (a)?
"""
X_train = np.array([
    [0.1, 0.1],
    [0.2, 0.2],
    [0.3, 0.3],
    [0.4, 0.4],
    [0.5, 0.5],
    [0.6, 0.6],
    [0.7, 0.7],
    [0.8, 0.8],
    [0.9, 0.9],
    [1.0, 1.0],
])
Y_train = [1,1,1,0,0,0,1,1,1,1]
print "X_train:\n{0}".format(X_train)
print "Y_train:\n{0}".format(Y_train)
clf = RandomForestClassifier(n_estimators=9)
clf = clf.fit(X_train, Y_train)
X_test = [
    [0.9, 0.1],
    [0.8, 0.2],
    [0.7, 0.3],
    [0.6, 0.4],
    [0.4, 0.6],
    [0.3, 0.7],
    [0.2, 0.8],
    [0.1, 0.9],
]
y_predict = clf.predict(X_test)
print "X_test:\n{0}".format(X_test)
print "Y_predict:\n{0}".format(y_predict)
