# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 14:50:40 2015
Illustrate end to end data processing and machine learning
@author: Yuhlin
"""
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import tree

# Read in inputs, try 3 different ways
with open('inputs.csv', 'rb') as f: #taken from the excel file
    reader = csv.reader(f)
    #for row in reader:
    #    print row

input1 = pd.read_csv('inputs.csv', sep=',',header=None)
#print input1.values

input2 = np.genfromtxt('inputs.csv',delimiter=',',skip_header=1)
#print input2

input3 = np.recfromcsv('inputs.csv', delimiter=',', filling_values=np.nan, \
    case_sensitive=True, deletechars='', replace_space=' ')
#print input3

# pre-process data
# create feature and target vectors
X = input2[:,:-3]
y = input2[:,-3]
#print X
#print y

# Standardize
mean = X.mean(axis=0) #iterate through the array and process one by one item
std = X.std(axis=0)
X_new = (X - mean) / std
#print "X_new", X_new

# create training and test data sets
total_size = X.shape[0]
test_size = total_size/4
print "total =", total_size, " test =", test_size
X_train = X[:-test_size]
X_test = X[-test_size:]
y_train = y[:-test_size]
y_test = y[-test_size:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
print "Linear Regression:"
print regr.coef_, regr.intercept_
print("Residual sum of squares: %.2f" % np.mean((y_pred - y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(X_test, y_test))
print y_test
print y_pred

# decision tree
print "Decision Tree:"
# Train
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print y_pred
print y_test
print "Decision Tree score: ", clf.score(X_test, y_test)
print "Feature importances:", clf.feature_importances_