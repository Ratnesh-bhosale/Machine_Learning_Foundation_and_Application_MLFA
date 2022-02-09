# -*- coding: utf-8 -*-
"""groupno_FirstName_LastName_RidgeRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X0lzc2vipgbiyoU9at5jjeK1WTIlj-_d
"""

# Do not make any changes in this cell
# Simply execute it and move on

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
ans = [0]*8

# The exercise uses Boston housing dataset which is an inbuilt dataset of scikit learn.
# Run the cell below to import and get the information about the data.

# Do not make any changes in this cell.
# Simply execute it and move on

from sklearn.datasets import load_boston
boston=load_boston()
boston

# Creating a dataframe

# Do not make any changes in this cell
# Simply execute it and move on

boston_df=pd.DataFrame(boston['data'], columns=boston['feature_names'])
boston_df['target'] = pd.DataFrame(boston['target'])
boston_df

# Question 1: Find the mean of the "target" values in the dataframe (boston_df)  
#             Assign the answer to ans[0] 
#             eg. ans[0] = 24.976534890123 (if mean obtained = 24.976534890123)

# Your Code: Enter your Code below

target_mean = boston_df['target'].mean()

#1 mark
ans[0] = target_mean

# Just to get a look into distribution of data into datasets
# Plot a histogram for boston_df

histogram = boston_df.hist(figsize = (14, 12))

"""**Splitting the data using train_test_split from sklearn library**"""

# Import machine learning libraries  for train_test_split

from sklearn.model_selection import train_test_split

# Split the data into X and Y

X = np.array(boston_df.drop(columns = ['target']))
Y = np.array(boston_df['target'])

# Spliting our data further into train and test (train-90% and test-10%)
# Use (randon_state = 42) in train_test_split, so that your answer can be evaluated

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 42)

"""**LINEAR REGRESSION**"""

# Question 2: Find mean squared error on the test set and the linear regression intercept(b)  
#             Assign the answer to ans[0] in the form of a list 
#             eg. ans[1] = [78.456398468,34.276498234098] 
#                  here , mean squared error             = 78.456398468
#                         linear regression intercept(b) = 34.276498234098

# Fit a linear regression model on the above training data and find MSE over the test set.
# Your Code: Enter your Code below

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

reg = LinearRegression()
reg.fit(x_train, y_train)
y_preds = reg.predict(x_test)

mse = mean_squared_error(y_preds, y_test)
intercept = reg.intercept_

# 2 marks
ans[1] = [mse, intercept]

"""**RIDGE REGRESSION**"""

# Question 3: For what value of lambda (alpha)(in the list[0.5,1,5,10,50,100]) will we have least value of the mean squared error of testing set 
#             Take lambda (alpha) values as specified i.e. [0.5,1,5,10,50,100]
#             Assign the answer to ans[2]  
#             eg. ans[1] = 5  (if  lambda(alpha)=5)

# Your Code: Enter your Code below

from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

lambda_list = [0.5, 1, 5, 10, 50, 100]
best_lambda = None
best_mse = 99999

for lambda_ in lambda_list:
    reg = Ridge(alpha = lambda_)
    reg.fit(x_train, y_train)
    test_preds = reg.predict(x_test)
    mse = mean_squared_error(test_preds, y_test)
    if mse < best_mse:
        best_lambda = lambda_
        best_mse = mse

#1 mark
ans[2] = best_lambda

# Question 4: Find mean squared error on the test set and the Ridge regression intercept(b)
#             Use the lamba(alpha) value obtained from question-3 
#             Assign the answer to ans[3] in the form of a list 
#             eg. ans[3] = [45.456398468,143.276498234098] 
#                  here , mean squared error             = 45.456398468
#                         Ridge regression intercept(b) = 143.276498234098

# Your Code: Enter your Code below

reg = Ridge(alpha = best_lambda)
reg.fit(x_train, y_train)
test_preds = reg.predict(x_test)
mse = mean_squared_error(test_preds, y_test)
intercept = reg.intercept_

# 2 marks
ans[3] = [mse, intercept]

# Plot the coefficient of the features( CRIM , INDUS , NOX ) with respective to  the lambda values specified [0.5,1,5,10,50,100]
# Enter your code below

crim_index = boston_df.columns.get_loc('CRIM')
indus_index = boston_df.columns.get_loc('INDUS')
nox_index = boston_df.columns.get_loc('NOX')

crim_coeff = []
indus_coeff = []
nox_coeff = []

lambda_list = [0.5, 1, 5, 10, 50, 100]

for lambda_ in lambda_list:
    reg = Ridge(alpha = lambda_)
    reg.fit(x_train, y_train)
    crim_coeff.append(reg.coef_[crim_index])
    indus_coeff.append(reg.coef_[indus_index])
    nox_coeff.append(reg.coef_[nox_index])

plt.figure(figsize = (6, 4))
plt.scatter(lambda_list, crim_coeff)
plt.xlabel('Lambda')
plt.ylabel('CRIM Coefficient')
plt.title('Lambda VS Coefficient of CRIM')

plt.figure(figsize = (6, 4))
plt.scatter(lambda_list, indus_coeff)
plt.xlabel('Lambda')
plt.ylabel('INDUS Coefficient')
plt.title('Lambda VS Coefficient of INDUS')

plt.figure(figsize = (6, 4))
plt.scatter(lambda_list, nox_coeff)
plt.xlabel('Lambda')
plt.ylabel('NOX Coefficient')
plt.title('Lambda VS Coefficient of NOX')

plt.show()

"""**LASSO REGRESSION**"""

# Question 5: For lambda (alpha)=1 find the lasso regression intercept and the test set mean squared error
#             Assign the answer to ans[4] in the form of a list 
#             eg. ans[4] = [35.456398468,14.276498234098] 
#                  here , mean squared error             = 35.456398468
#                         lasso regression intercept(b) = 14.276498234098

# Your Code: Enter your Code below

from sklearn.linear_model import Lasso

reg = Lasso(alpha = 1)
reg.fit(x_train, y_train)
test_preds = reg.predict(x_test)
mse = mean_squared_error(test_preds, y_test)
intercept = reg.intercept_

#2 mark
ans[4] = [mse, intercept]

# Question 6: Find the most  important feature  in the data set i.e. which feature coefficient is further most non zero if lambda is increased gradually
#             let CRIM=1,	ZN=2, INDUS=3,	CHAS=4,	NOX=5,	RM=6,	AGE=7,	DIS=8,	RAD=9,	TAX=10,	PTRATIO=11,	B=12,	LSTAT=13
#              eg. if your answer is "CHAS"
#                   then your answer should be ans[5]=4

# Your Code: Enter your Code below

max_index = None
max_val = -99999

reg = Lasso(alpha = 1)
reg.fit(x_train, y_train)

i = 1

for val in reg.coef_:
    if val > max_val:
        max_val = val
        max_index = i
    i = i + 1

#2 marks
ans[5] = max_index

"""Run the below cell only once u complete answering all the above answers 

"""

##do not change this code
import json
ans = [str(item) for item in ans]

filename = "--Replace the Jupyter Notebook filename from Title here in the described format!---"

# Eg if your name is Saurav Joshi and email id is sauravjoshi123@gmail.com, filename becomes
# filename = sauravjoshi123@gmail.com_Saurav_Joshi_LinearRegression

"""## Do not change anything below!!
- Make sure you have changed the above variable "filename" with the correct value. Do not change anything below!!
"""

from importlib import import_module
import os
from pprint import pprint

findScore = import_module('findScore')
response = findScore.main(ans)
response['details'] = filename
with open(f'evaluation_{filename}.json', 'w') as outfile:
    json.dump(response, outfile)
pprint(response)