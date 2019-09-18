# K Nearest Neighbor Example
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import random

start_time =  time.time()

# Getting data
pd_data = pd.read_csv("rabbits.csv") # reads csv file
rabbits_data = pd_data.values # assigning the values to rabbits_data

# assigning X and Y to it's corresponding values
x = rabbits_data[:, 1]
y = rabbits_data[:, 2]
centroids = []

# a is an array that stores other arrays that hold x and y values
def mean_of_points(a):
    sum_x = 0
    sum_y = 0
    for c in a:
        sum_x += c[0]
        sum_y += c[1]
    
    if len(a) != 0 :
        mean_x = sum_x / len(a)
        mean_y = sum_y / len(a)
        return [mean_x, mean_y]
    
    return None

def K_Means(k):
  
    cluster_members = []

    for c in range(k):
        centroid = [random.randint(0,12), random.randint(0,12)]
        centroids.append(centroid)
        cluster_members.append([])

    print(centroids)
    
    counter = 0
    while counter < 100:
        for i in range(int(x.size)):
            distances = []
            for g in range(k):
                cur_c = centroids[g] # current centroid
                distance = ((cur_c[0]-x[i])**2+(cur_c[1]-y[i])**2)**(1/2)
                distances.append(distance)
            clos_c_i = distances.index(min(distances)) # closest centroid index
            cluster_members[clos_c_i].append([x[i],y[i]])

        for i in range(len(centroids)):
            new_centroid = mean_of_points(cluster_members[i])
            if new_centroid != None:
                centroids[i] = new_centroid
        counter += 1    

K_Means(2)

# Rabbits Data being plotted
plt.plot(x[0:int(x.size/2)], y[0: int(y.size/2)], '.')
plt.plot(x[int(x.size/2):], y[int(y.size/2):], '.')

print(centroids)
centroids = np.array(centroids)
plt.plot(centroids[:, 0], centroids[:, 1], 'g.', markersize=12)

plt.ylabel('speed (m/s)')
plt.xlabel('weight (lb)')

run_time = time.time() - start_time

print("run time:", run_time, "s")

plt.show() # shows the graph