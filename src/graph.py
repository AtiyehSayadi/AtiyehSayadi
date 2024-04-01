""" Graph Module"""
import numpy as np
class Graph:
    """Maintaining the adjacency matrix and related graph computations."""
    def __init__(self,n):
        self.graph = np.zeros((n , n ))
    def get_adj_matrix(self):
        """This module returns the adjacency matrix for use in other graphs."""
        return self.graph
    def add_edge(self,start, end):
        """Adding edges to the adjacency matrix."""
        self.graph[start][end]=1
        self.graph[end][start]=1
    def exist_edge(self,start,end):
        """This function indicates whether the desired edge exists
        in the adjacency matrix or not."""
        if self.graph[start][end]==1:
            return True
        else:
            return False
    def get_degree(self,node):
        """This function calculates the degree of each node."""
        row = self.graph[node]
        degree = sum(row)
        return degree
    def get_shortest_path(self,start, des):
        """This function calculates the shortest path length between two nodes."""
        n = len(self.graph)
        unvisited_nodes=list(range(n))
        min_distance=1
        j=0
        visited_nodes=[]
        visited_nodes.append(start)
        visited_nodes.append(float('inf'))
        unvisited_nodes.remove(start)
        if start==des:
            return 0
        while visited_nodes:
            node=visited_nodes.pop(0)
            if node==float('inf'):
                min_distance +=1
                if visited_nodes:
                    node= visited_nodes.pop(0)
                    visited_nodes.append(float('inf'))
            if node!= float('inf'):
                while j< n:
                    if j in unvisited_nodes:
                        if self.graph[node][j]==1:
                            if j==des:
                                return min_distance
                            visited_nodes.append(j)
                            unvisited_nodes.remove(j)
                    j+=1
                j=0
        return float('inf')
    def degree_centrality(self,node):
        """This function calculates the degree centrality."""
        n = len(self.graph)
        dc= (self.get_degree(node))/(n-1)
        return dc
    def closeness_centrality(self,node):
        """This function calculates the closeness centrality."""
        n = len(self.graph)
        sum_path=0
        i=0
        while i<n:
            sum_path += self.get_shortest_path(node,i)
            i+=1
        cc=(n-1)/ sum_path
        return cc