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
        self.dist_matrix = np.array([[-1]*(2*n+1)]*(2*n+1))

        # initialise distance matrix to be 2n+1 by 2n+1
        for i in range(n):
            self.dist_matrix[i][:n] = dist_matrix[i]

        # initialise clusters of single nodes
        for i in range(n):
            self.clusters.append(Cluster(label=str(i), nodes=[i]))


    def print_clusters(self, clusters, alive_clusters_indices):
        for i in range(len(alive_clusters_indices)):
            index = alive_clusters_indices[i]
            print ("cluster" + str(i) + ", age: " + str(clusters[index].age))
            # tree = [(node,no) for node in clusters[index].nodes]
            print (clusters[index].nodes)

    def upgma(self):
        clusters = self.clusters
        no_clusters = self.n

        alive_clusters_indices = [i for i in range(no_clusters)] # stores indices into distance matrix of alive clusters
        new_node_id = self.n

        self.print_clusters(clusters, alive_clusters_indices)
        while(no_clusters > 1):
            ci_index = 0
            cj_index = 0

            lowest_dist = sys.maxsize

            for x in range(no_clusters): # loop through clusters
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


            clusters.append(c_new)
            alive_clusters_indices.append(new_node_id)


            no_clusters -= 1
            new_node_id += 1

            self.print_clusters(clusters, alive_clusters_indices)

        return clusters


dist_matrix = np.array([[0, 3, 4, 4, 4],
                         [3, 0, 4, 4, 4],
                         [4, 4, 0, 1, 2],
                         [4, 4, 1, 0, 1],
                         [4, 4, 2, 2, 0]])
upgma = UPGMA(dist_matrix, len(dist_matrix))
upgma.upgma()

