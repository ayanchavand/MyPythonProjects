import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets ,linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()

#print(diabetes.DESCR)
#print(diabetes.key)

diabetes_x = diabetes.data


diabetes_x_train= diabetes_x[:-30]
diabetes_x_test = diabetes_x[-30:]

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_x_train,diabetes_y_train)

diabetes_y_predicted = model.predict(diabetes_x_test)

print("mean squared error is ",mean_squared_error(diabetes_y_test,diabetes_y_predicted))
print("weight: ",model.coef_)
print("intercept: ",model.intercept_)
#diabetes_x = diabetes.data

