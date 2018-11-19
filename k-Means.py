import random
import numpy as np

def assign_to_clusters(k, centers, data):
    ''' receivers k = no. clusters, k centers, n-dimensional data '''
    clusters = [[] for i in range(k)]
    for i, pt in enumerate(data):
        dist = [np.linalg.norm(np.array(pt)-np.array(center)) for center in centers]
        clusters[dist.index(min(dist))].append(data[i])
    return clusters

def calculateCenterOfGravity(data):
    centers = [sum(el) for el in zip(*data)]
    no_pts = len(data)
    centers = [x/no_pts for x in centers]
    return centers

def kmeans(data, k, max_iterations=20):
    ''' Llyod's algorithm for k means'''
    n = len(data)
    centers = []
    curr_no_iterations = 0
    for i in range(k):
        rand_choice = random.randrange(0, n, 1)
        if rand_choice not in centers:
            centers.append(data[rand_choice])

    # Centers to clusters
    old_centers = []
    while (curr_no_iterations < max_iterations and centers != old_centers):
        old_centers = centers
        clusters = assign_to_clusters(k, centers, data)
        centers = [calculateCenterOfGravity(cluster) for cluster in clusters]
        curr_no_iterations += 1
    return clusters, centers

dataset = [[1,2], [1,5], [3,4], [5,6], [6,7], [8,9], [0.5, 5], [19, 101], [20, 121]]
clusters, centers = kmeans(dataset, 3, 12)
print(clusters)