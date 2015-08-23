# -*- coding: utf-8 -*-
"""
========================================================
Created on Fri Jun 23 11:32:24 2015

@course:       CS596 - Data Mining and Machine Learning
@student_name: Doan Quoc Sy VO
@student_id:   150201133
@homework:     2
========================================================

"""
print(__doc__)

import numpy as np
import csv
from sklearn import neighbors
from sklearn import tree

X = np.array([
[66,170], [73,210], [72,165], [70,180], [74,185], [68,155], [65,150], [64,120],
[63,125], [67,140], [68,165], [66,130]
])

y = np.array([0,0,0,0,0,0,1,1,1,1,1,1])

print(
"""
===================================================
HW 2-Problem 3-Nearest Neighbors Classification
===================================================
""")

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





print(
"""\n\n\n
===================================================
HW 2-Problem 4 - Decision Tree & K nearest neighbor
===================================================
""")


# Read in inputs, try 3 different ways
with open('inputs.csv', 'rb') as f:
    reader = csv.reader(f)

input2 = np.genfromtxt('inputs.csv',delimiter=',',skip_header=1)


# Pre-process data: create feature and target vectors
X = input2[:,:-3]
y = input2[:,-3]

# 2) Remove gender column
X = np.delete(X,1,1) 


# Create TRAINING and TEST data sets
total_size = X.shape[0]
test_size = total_size/4
print "\nInput data:"
print "   - Total =", total_size, ", Test =", test_size
X_train = X[:-test_size]
X_test = X[-test_size:]
y_train = y[:-test_size]
y_test = y[-test_size:]


# Process data using Decision Tree Technique
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print "\nDecision Tree:"
print "   - Score: ", clf.score(X_test, y_test)
print "\n  COMPARISON of prediction vs ground truth vectors:"
print "   - Test result (y_test):\t", y_test
print "   - Predicted result:\t\t", y_pred
print "   - Feature importances:\t", clf.feature_importances_



# Process data using K-nearest Neighbor Technique
n_neighbors=5 #k = 5
clf = neighbors.KNeighborsClassifier(n_neighbors)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print "\n\n\nK-nearest neighbor result:"
print "   - Score: ", clf.score(X_test, y_test)
print "\n  COMPARISON of prediction vs ground truth vectors:"
print "   - Test result (y_test):\t", y_test
print "   - Predicted result:\t\t", y_pred

