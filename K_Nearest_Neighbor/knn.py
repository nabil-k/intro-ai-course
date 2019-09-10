# K Nearest Neighbor Example
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Getting data
pd_data = pd.read_csv("rabbits.csv") # reads csv file
rabbits_data = pd_data.values # assigning the values to rabbits_data

# assigning X and Y to it's corresponding values
x = rabbits_data[:, 1]
y = rabbits_data[:, 2]

plt.plot(x[0:int(x.size/2)], y[0: int(y.size/2)], '.')
plt.plot(x[int(x.size/2):], y[int(y.size/2):], '.')

plt.ylabel('speed (m/s)')
plt.xlabel('weight (lb)')

plt.show() # shows the graph

