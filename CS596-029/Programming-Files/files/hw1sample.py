# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 11:32:24 2015

@author: Yuhlin
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

sample = np.array([[1,3], [2,5], [3,7], [4,9],[5,11]])
#print "sample: ", sample
X_train = sample[:,:1] #x must be the vector - i.e. multi dimension single array
#print "x_train: ", X_train
y_train = sample[:,1] #y can just be the single dimension array
#print "y_train:", y_train

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train) #Notes: this function takes X as a vector

print "Linear Regression:\n", 
print "  coef=", regr.coef_
print "  intercept=", regr.intercept_

# Plot outputs
plt.scatter(X_train, y_train,  color='black')
plt.plot(X_train, regr.predict(X_train), color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

# Add outlier data
np.random.seed(0)
for x in np.nditer(y_train, op_flags=['readwrite']):
    x[...] = x + np.random.normal(scale=2)
# Train the model using the training sets
regr.fit(X_train, y_train)

print "New targets:", y_train
print "Linear Regression:\n", 
print "  coef=", regr.coef_
print "  intercept=", regr.intercept_

# Plot outputs
plt.scatter(X_train, y_train,  color='black')
plt.plot(X_train, regr.predict(X_train), color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()