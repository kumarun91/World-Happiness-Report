# -*- coding: utf-8 -*-
"""
Created on Thu May 04 03:43:47 2017

@author: arun
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 02 01:21:30 2017

@author: arun
"""
#from __future__ import division
import numpy as np
import pandas as py
import math
import matplotlib.pyplot as plt
from sklearn import linear_model
# Loading the  dataset as training and testing C:\Users\ArunKumarN\Desktop\DataScience\FinalProject
dataFrame = py.read_csv('C:/Users/ArunKumarN/Desktop/DataScience/FinalProject/2016.csv')
testFrame = py.read_csv('C:/Users/ArunKumarN/Desktop/DataScience/FinalProject/finalPrediction.csv')

#Using the features
xtraining = dataFrame[['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)','Generosity']].as_matrix()
xtest = testFrame[['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Freedom','Trust (Government Corruption)','Generosity']].as_matrix()

# Splitting the targets into training/testing sets
ytrain = dataFrame[['Happiness Score']].values

# Creating linear regression object
linearReg = linear_model.LinearRegression()

#To validate the model, lets gather the actual Y values
ytest = testFrame[['Happiness Score']].values
# Train the model using the training sets
linearReg.fit(xtraining, ytrain)
#predict the target
linear_predictedList = linearReg.predict(xtest)

flattenedLinear  = [val for sublist in linear_predictedList for val in sublist]
print flattenedLinear
# Ridge
from sklearn.linear_model import Ridge
clf = Ridge(alpha=0.5)
clf.fit(xtraining, ytrain)
ridge_predictedList =clf.predict(xtest)
#print ridge_predictedList[36]
print ridge
#Lasso
from sklearn import linear_model
clfLasso = linear_model.Lasso(alpha=0.5)
clfLasso.fit(xtraining, ytrain)
lasso_predictedList = clfLasso.predict(xtest)
#print lasso_predictedList[36]

#plt.plot(ytest,linear_predictedList,color='blue', linewidth=2, label='model 0')
#plt.show()
