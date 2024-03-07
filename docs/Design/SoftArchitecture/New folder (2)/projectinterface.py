"""This module introduces centralization degree and proximity computational functions."""
import tkinter as tk
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class File:
    """In this class, input is read and an adjacency matrix is constructed."""
    def read_file(self):
        """Function reads and converts the input."""
        file_path = "test.txt"
        matrix = np.loadtxt(file_path)
        intmatrix = matrix.astype(int)
        n = np.amax(intmatrix)
        new_matrix = np.zeros((n + 1, n + 1))
        for row in intmatrix:
            new_matrix[row[0], row[1]] = 1
            new_matrix[row[1], row[0]] = 1
        return new_matrix

class GUI:
    """In this class, a user interface is created for displaying the outputs."""
    def __init__(self, inteface):
        self.inteface = inteface
        self.inteface.title("Graph Analysis")
        self.inteface.geometry("300x150")
        self.degree_button = tk.Button(inteface, text="Degree Centrality",
        command=self.degree_centrality, bg="pink", font=("Helvetica", 10, "bold"), width=15)
        self.degree_button.pack(pady=10)
        self.closeness_button = tk.Button(inteface, text="Closeness Centrality",
        command=self.closeness_centrality, bg="lightblue",font=("Helvetica", 10, "bold") , width=15)
        self.closeness_button.pack(pady=10)
        self.file_button = tk.Button(inteface, text="The Main Graph",
        command=self.show_graph_matrix, bg="orange", font=("Helvetica", 10, "bold"), width=15)
        self.file_button.pack(pady=5)
    def degree_centrality(self):
        """In this class, an interface for degree centrality is constructed."""
        plt.gca().clear()
        #plt.figure()
        file = File().read_file()
        degree_file = Degree(file)
        degree_centrality = degree_file.degree_centrality()
        graph = nx.Graph(file)
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos ,edge_color='red',  node_color='lightblue', node_size=700)
        labels = {node: f"{node}= {degree_centrality[int(node), 1]:.2f}" for node in graph.nodes()}
        nx.draw_networkx_labels(graph, pos, labels=labels, font_size=6)
        plt.text(0.5, 1.02, "Degree Centrality", horizontalalignment='center',
        verticalalignment='bottom', transform=plt.gca().transAxes)
        plt.show()
    def closeness_centrality(self):
        """In this class, an interface for closeness centrality is constructed."""
        plt.gca().clear()
        #plt.figure()
        file = File().read_file()
        closeness_file = Closeness(file)
        closeness_centrality = closeness_file.centrality_closeness()
        graph = nx.Graph(file)
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, edge_color='red',  node_color='lightblue', node_size=700)
        labels = {node: f"{node}= {closeness_centrality[int(node), 1]:.2f}"
        for node in graph.nodes()}
        nx.draw_networkx_labels(graph, pos, labels=labels, font_size=6)
        plt.text(0.5, 1.02, "Closeness Centrality", horizontalalignment='center',
        verticalalignment='bottom', transform=plt.gca().transAxes)
        plt.show()
    def show_graph_matrix(self):
        """In this class, an interface for the main graph is constructed."""
        #plt.figure()
        plt.gca().clear()
        file = File().read_file()
        graph = nx.Graph(file)
        nx.draw(graph, edge_color='red', with_labels=True, node_color='lightblue',
        font_size=10, node_size=300)
        plt.text(0.5, 1.02, "The Main Graph", horizontalalignment='center',
        verticalalignment='bottom', transform=plt.gca().transAxes)
        plt.show()
class Degree:
    """In this class, centrality degree is computed."""
    def __init__(self, matrix):
        self.__matrix = matrix
    def find_degree(self):
        """This function is designed to compute the degree of each node."""
        main_matrix = self.__matrix
        matrix_size = main_matrix.shape
        n = matrix_size[0]
        degree_nodes = np.zeros((n , 2))
        i = 0
        j = 0
        while i < n:
            degree_nodes[i,0] = i
            while j < n:
                if main_matrix[i, j] == 1:
                    degree_nodes[i,1] = degree_nodes[i,1] + 1
                j += 1
            i += 1
            j = 0
        return degree_nodes

    def degree_centrality(self):
        """Function to compute degree centrality for each node."""
        degc = self.find_degree()
        matrix_size = degc.shape
        n = matrix_size[0]
        m = 0
        centrality_matrix = np.zeros((n, 2))
        while m < n:
            centrality_matrix[m, 0] = degc[m, 0]
            centrality_matrix[m, 1] = degc[m, 1] / (n - 1)
            m += 1
        return centrality_matrix
class Closeness:
    """In this class, closeness centrality is computed."""
    def __init__(self, matrix):
        self.__matrix = matrix
    def shortest_path(self):
        """This function calculates the shortest paths for each node."""
        matrix= self.__matrix
        n = len(matrix)
        final_matrix = np.full((n, n), np.inf)
        unvisited_nodes=list(range(n))
        i=0
        j=0
        short_path=[]
        while i <n:
            unvisited_nodes=list(range(n))
            unvisited_nodes.remove(i)
            final_matrix[i,i]=0
            node=i
            min_distance=1
            short_path.append(i)
            short_path.append(float('inf'))
            while short_path:
                node=short_path.pop(0)
                if node==float('inf'):
                    min_distance +=1
                    if short_path:
                        node= short_path.pop(0)
                        short_path.append(float('inf'))
                if node!= float('inf'):
                    while j< n:
                        if j in unvisited_nodes:
                            if matrix[node,j]==1:
                                short_path.append(j)
                                final_matrix[i,j]= min_distance
                                unvisited_nodes.remove(j)
                        j+=1
                    j=0
            i +=1
        return final_matrix
    def centrality_closeness(self):
        """Function to compute closeness centrality for each node."""
        matrix = self.shortest_path()
        matrix_size = matrix.shape
        n = matrix_size[0]
        main = np.zeros((n, 2))

        for i in range(n):
            main[i, 0] = i
            main[i, 1] = (n - 1) / np.sum(matrix[i])

        return main

a = File().read_file()
degree = Degree(a)
close= Closeness(a)
print(degree.find_degree())
print(degree.degree_centrality())
print(close.shortest_path())
print(close.centrality_closeness())
G = nx.Graph(a)
print (nx.closeness_centrality(G))
interface = tk.Tk()
app = GUI(interface)
interface.mainloop()
