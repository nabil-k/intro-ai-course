# Linear Regression Example

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Getting data
pd_data = pd.read_csv("icecream.csv") # reads csv file
icecream_data = pd_data.values # assigning the values to icecream_data

# shows data

x = icecream_data[:, 1]
y = icecream_data[:, 0]


# plots the data
plt.plot(x, y, 'b.')
plt.ylabel('Income')
plt.xlabel('Temperature')

# calculates the differences between the profit and predicted profits
def meanSquaredError(y1s, y2s):
    differences = y1s - y2s
    for i in range(len(differences)):
        differences[i] *= differences[i]
    return differences.mean()

# plots line of best fit y = mx + b

max_meanSquaredError = 999999999999999999
best_m = 0
best_b = 0
m = -10
b = -10

# Finds best possible m and b
while m <= 10:
    while b <= 10:
        current_pred_income = []
        for i in x:
            current_pred_income.append(m * i + b)
        
        current_meanSquaredError = meanSquaredError(y,current_pred_income)
        
        if  max_meanSquaredError > current_meanSquaredError:
            #print(current_meanSquaredError, m, b)
            best_m = m
            best_b = b
            max_meanSquaredError = current_meanSquaredError

        b += 1
    b = 0
    m += 1

print("Mean Squared Error:", max_meanSquaredError)  
# Plots best prediction
pred_income =[]
for i in x:
    pred_income.append((best_m * i) + best_b)

plt.plot(x, pred_income, 'g-')

# Plotting Error
for i in range(len(x)):
    plt.plot([x[i], x[i]], [y[i], pred_income[i]], 'r-')



plt.show() # shows the graph

