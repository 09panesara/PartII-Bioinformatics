import numpy as np
import sys


class Cluster:
    def __init__(self, label, nodes, left=None, right=None, age=None):
        self.label = label
        self.left = left
        self.right = right
        self.nodes = nodes
        if age is None:
            self.age = 0
        else:
            self.age = age


class UPGMA:
    def __init__(self, dist_matrix, n):
        # need to initialise nodes
        self.n = n
        self.clusters = []
        self.dist_matrix = dist_matrix
        # initialise clusters of single nodes
        # initialise distance matrix to be 2n+1 by 2n+1
        for i in range(n, 2*n+1):
            self.dist_matrix[i] = self.dist_matrix[i] + [-1 for j in range(n, 2*n+1)]
            self.dist_matrix.append([-1 for k in range(2*n+1)])
        for i in range(n):
            self.clusters[i] = Cluster(label=str(i), nodes=[i])


    def print_clusters(clusters):
        for i in range(len(clusters)):
            print ("cluster" + str(i))
            print(clusters[i].nodes)

    def upgma(self):
        clusters = self.clusters
        no_clusters = self.n

        alive_clusters_indices = [i for i in range(no_clusters)] # stores indices into distance matrix of alive clusters
        new_node_id = self.n
        dist_matrix_sz = len(self.dist_matrix)

        while(no_clusters > 0):
            ci_index = 0
            cj_index = 0

            lowest_dist = sys.maxsize

            for x in range(no_clusters): # loop to 2n+1
                for y in range(x+1, no_clusters): # loop from i+1 to avoid repeated comparisons
                    i = alive_clusters_indices[x]
                    j = alive_clusters_indices[y]

                    dist = sum([x + y for x in clusters[i].nodes for y in clusters[j].nodes])
                    dist = dist / (len(clusters[i].nodes) + len(clusters[j].nodes))
                    if dist < lowest_dist:
                        lowest_dist = dist
                        ci_index = i
                        cj_index = j

            # merge two closest clusters into single cluster
            ci = clusters[ci_index]
            cj = clusters[cj_index]

            c_new = Cluster(label=ci.label+cj.label, nodes=ci.nodes+cj.nodes, age=dist/2, left=ci, right=cj)

            # Update distance matrix by setting Ci, Cj to -1, update row and column at index new_node_id (=index of new node)

            alive_clusters_indices.remove(ci_index)
            alive_clusters_indices.remove(cj_index)

            for i in range(no_clusters):
                d_avg = (self.dist_matrix[ci_index][i] + self.dist_matrix[cj_index][i]) / 2
                self.dist_matrix[i][new_node_id] = d_avg
                self.dist_matrix[new_node_id][i] = d_avg


            self.dist_matrix[ci_index] = -1
            self.dist_matrix[:, ci_index] = -1
            self.dist_matrix[cj_index] = -1
            self.dist_matrix[:, cj_index] = -1

            clusters.append(c_new)
            alive_clusters_indices.append(new_node_id)


            no_clusters -= 1
            new_node_id += 1

            self.print_clusters(clusters)

        return clusters


dist_matrix = np.matrix([[0, 3, 4, 4, 4],
                         [3, 0, 4, 4, 4],
                         [4, 4, 0, 1, 2],
                         [4, 4, 1, 0, 1],
                         [4, 4, 2, 2, 0]])
upgma = UPGMA(dist_matrix, dist_matrix.size)
upgma.upgma()

