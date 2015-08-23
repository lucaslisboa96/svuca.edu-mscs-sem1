"""
================================================
HW 2-Problem 3-Nearest Neighbors Classification
================================================

"""
print(__doc__)

import numpy as np
from sklearn import neighbors

X = np.array([
[66,170], [73,210], [72,165], [70,180], [74,185], [68,155], [65,150], [64,120],
[63,125], [67,140], [68,165], [66,130]
])

y = np.array([0,0,0,0,0,0,1,1,1,1,1,1])



#a)	k=1, distance = Euclidean, weight = uniform
n_neighbors=1 #k = 1
euclidean = 2 #Euclidean
uniform = 'uniform'
clf = neighbors.KNeighborsClassifier(n_neighbors, weights=uniform, p=euclidean)
clf.fit(X, y)
test_case_1 = np.array([[69,155]])
test_case_2 = np.array([[72,160]])
print "a) k=1, distance = Euclidean, weight = uniform"
print ("  Result of test case 1 (h=69, w=155): %g" % clf.predict(test_case_1))
print ("  Result of test case 2 (h=72, w=160): %g" % clf.predict(test_case_2))


#b) k=3, distance = Manhattan, weight = uniform
n_neighbors=3 #k = 3
manhattan = 1 #Manhattan
uniform = 'uniform'
clf = neighbors.KNeighborsClassifier(n_neighbors, weights=uniform, p=manhattan)
clf.fit(X, y)
test_case_1 = np.array([[69,155]])
test_case_2 = np.array([[72,160]])
print "\nb) k=3, distance = Manhattan, weight = uniform"
print ("  Result of test case 1 (h=69, w=155): %g" % clf.predict(test_case_1))
print ("  Result of test case 2 (h=72, w=160): %g" % clf.predict(test_case_2))