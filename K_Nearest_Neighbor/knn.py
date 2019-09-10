# K Nearest Neighbor Example
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time;

start_time =  time.time()

# Getting data
pd_data = pd.read_csv("rabbits.csv") # reads csv file
rabbits_data = pd_data.values # assigning the values to rabbits_data
new_rabbit_data = [9,10]

# assigning X and Y to it's corresponding values
x = rabbits_data[:, 1]
y = rabbits_data[:, 2]
labels = rabbits_data[:,0]

def classify(newRabbit, k):
    distances = []
    # Calculates the how far away the new rabbit is from all the other data
    for i in range(int(x.size)):
        distance = ((newRabbit[0] - x[i])**2 + (newRabbit[1] - y[i])**2)**(1/2)
        distances.append(distance)
    # sorts the distances from least to greatest
    distances_sorted = sorted(distances)

    # gets the k least distances
    k_distances_sorted = distances[:k]
    k_distances_sorted_labels = []

    for k_d in k_distances_sorted:
        i = 0
        for d in distances:
            if k_d == d:
                k_distances_sorted_labels.append(labels[i])
            i += 1
    print(k_distances_sorted_labels)
    unique_k_distances_sorted_labels = set(k_distances_sorted_labels)
    
    class_vote = []

    cv_i = 0
    for u_l in unique_k_distances_sorted_labels:
        class_vote.append(0)
        for l in k_distances_sorted_labels:
            if l == u_l:
                class_vote[cv_i] += 1
        cv_i += 1
    
    # finds index with the larget number of votes
    class_vote_largest_index = 0
    for i in range(len(class_vote)):
        if class_vote[i] > class_vote[class_vote_largest_index]:
            class_vote_largest_index = i

    predicted_rabbit_species = list(unique_k_distances_sorted_labels)[class_vote_largest_index]

    print("Predicted Rabbit's Species: ", predicted_rabbit_species)
        

classify(new_rabbit_data, 13)
# Rabbits Data being plotted
plt.plot(x[0:int(x.size/2)], y[0: int(y.size/2)], '.')
plt.plot(x[int(x.size/2):], y[int(y.size/2):], '.')
# *New* rabbits data being plotted
plt.plot(new_rabbit_data[0], new_rabbit_data[1], 's')

plt.ylabel('speed (m/s)')
plt.xlabel('weight (lb)')

run_time = time.time() - start_time

print("run time:", run_time, " s")

plt.show() # shows the graph



