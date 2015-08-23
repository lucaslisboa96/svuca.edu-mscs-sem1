# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 11:32:24 2015

@course:       CS596 - Data Mining and Machine Learning
@student_name: Doan Quoc Sy VO
@student_id:   150201133
@homework:     1
"""

import numpy as np
from sklearn import linear_model, datasets



"""
Problem 4
"""


total_size = 100
n_outliers = 50
test_size = 20


# Req 2 - Ask the user to input noise level instead of using the preset value (noise=10)
input_noise_level = input("Enter noise level: ")
print("Noise value of %d is entered." % input_noise_level) 


# Req 1 - Replace datasets.load_diabetes() with datasets.make_regression() function
X, y, coef = datasets.make_regression(n_samples=total_size, n_features=1,
                                      n_informative=1, noise=input_noise_level,
                                      coef=True, random_state=0)

# Req 3
# Separate the training set - 80 samples
X_train = X[:-test_size,:]
y_train = y[:-test_size]

# Separate the test set - 20 samples
X_test = X[-test_size:,:]
y_test = y[-test_size:]



# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)

# Test the model with test data
y_pred = regr.predict(X_test)

# Print out result
print "\n Linear Regression:"
print "     coef: ", regr.coef_
print "     intercept: ", regr.intercept_
print("\nResidual sum of squares: %.2f" % np.mean((y_pred - y_test) ** 2))
print('\nVariance score: %.2f' % regr.score(X_test, y_test)) #1 is perfect prediction
print y_test
print y_pred