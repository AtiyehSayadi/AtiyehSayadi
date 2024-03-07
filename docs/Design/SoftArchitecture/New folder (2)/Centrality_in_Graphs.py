import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt

class File:
    def read_file(self):
        """Function reads and converts the input."""
        file_path = "test.txt"
        matrix = np.loadtxt(file_path)
        intmatrix = matrix.astype(int)
        n= np.amax(intmatrix)
        new_matrix= np.zeros((n +1, n +1))
        for row in intmatrix:
            new_matrix[row[0],row[1]]=1
            new_matrix[row[1],row[0]]=1
        return new_matrix

class Degree:
    
    def __init__(self, matrix):
        self.__matrix = matrix
        
    def find_degree(self): 
        main_matrix=self.__matrix
        matrix_size = main_matrix.shape
        n= matrix_size[0]
        degree= np.zeros((n , 2))
        i=0
        j=0
        while i <n:
            degree[i,0]=i
            while j < n:
                if main_matrix[i,j]==1:
                    degree[i,1] = degree[i,1] + 1
                j +=1
            i += 1
            j =0
        return degree
    #"end of the class"
    def degree_centrality (self):
        """Function printing python version."""
        degc= self.find_degree()
        matrix_size = degc.shape
        n= matrix_size[0]
        m=0
        while m< n:
            degc[m,1]=degc[m,1]/ (n -1)
            m +=1
        sorted_matrix = np.argsort(degc[:,1])
        sorted_matrix = sorted_matrix[::-1]
        sorted_matrix_main = degc[sorted_matrix]
        return sorted_matrix_main
    
class Closeness:
    def __init__(self, matrix):
        self.__matrix = matrix
    def dijkstra(self):
        """Function printing python version."""
        matrix= self.__matrix
        n = len(matrix)
        all_shortest_distances = []

        for start_node in range(n):
            distances = [float('infinity')] * n
            distances[start_node] = 0
            unvisited_nodes = list(range(n))

            while unvisited_nodes:
                min_distance = float('infinity')
                min_node = None

                for node in unvisited_nodes:
                    if distances[node] < min_distance:
                        min_distance = distances[node]
                        min_node = node
                unvisited_nodes.remove(min_node)

                for neighbor in range(n):
                    if matrix[min_node][neighbor] == 1:
                        distance = distances[min_node] + 1
                        if distance < distances[neighbor]:
                            distances[neighbor] = distance

            all_shortest_distances.append(distances)
        all_shortest_distances_matrix = np.array(all_shortest_distances)
        return all_shortest_distances_matrix
    def centrality_closeness(self):
        """Function printing python version."""
        matrix= self.dijkstra()
        matrix_size = matrix.shape
        n= matrix_size[0]
        main=np.zeros((n , 2 ))
        i=0
        j=0
        while i<n:
            main[i,0]=int(i)
            while j <n:
                main[i,1]=main[i,1]+matrix[i,j]
                j +=1
            j=0
            i+=1
        i=0
        while i<n:
            main[i,1]=(n-1)/main[i,1]
            i+=1
        sorted_indices = np.argsort(main[:,1])
        sorted_indices = sorted_indices[::-1]
        sorted_matrix = main[sorted_indices]
        return sorted_matrix

a = File().read_file()  
degree = Degree(a) 
close= Closeness(a)
print(degree.find_degree())  
print(close.centrality_closeness()) 
print (nx.closeness_centrality(a))

