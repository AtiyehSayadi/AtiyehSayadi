"""Software testing module."""
import numpy as np
import networkx as nx
import sys
sys.path.append('../')
from src.file import File
def test_degree_centrality_bound():
    """Testing the correctness of the degree centrality range."""
    graph = File().read_file(r"C:\Users\atiye\Centrality-In-Graphs\src\CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len=len(adj_matrix)
    i=0
    nodes=list()
    #a.append(2)
    while i< matrix_len:
        if (graph.degree_centrality(i)<0) or (graph.degree_centrality(i)>1):
            nodes.append(i)
        i +=1
    assert len(nodes) == 0
    return
def test_closeness_centrality_bound():
    """Testing the correctness of the closeness centrality range."""
    graph = File().read_file(r"C:\Users\atiye\Centrality-In-Graphs\src\CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len=len(adj_matrix)
    i=0
    nodes=list()
    #a.append(2)
    while i< matrix_len:
        if (graph.closeness_centrality(i)<0) or (graph.closeness_centrality(i)>1):
            nodes.append(i)
        i +=1
    assert len(nodes) == 0
    return
def test_closeness_centrality_values():
    """Testing the correctness of closeness centrality values."""
    graph = File().read_file(r"C:\Users\atiye\Centrality-In-Graphs\src\CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len = len(adj_matrix)
    main_graph = nx.Graph(adj_matrix)
    nx_graph=nx.closeness_centrality(main_graph)
    graph_matrix=np.array([[key, value] for key, value in nx_graph.items()])
    nodes = list()
    i=0
    while i < matrix_len -1:
        if round(graph.closeness_centrality(i),5)!= round(graph_matrix[i,1],5):
            nodes.append(i)
        i +=1
    assert len(nodes)==0
    return
def test_degree_centrality_values():
    """Testing the correctness of degree centrality values."""
    graph = File().read_file(r"C:\Users\atiye\Centrality-In-Graphs\src\CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len = len(adj_matrix)
    main_graph = nx.Graph(adj_matrix)
    nx_graph=nx.degree_centrality(main_graph)
    graph_matrix=np.array([[key, value] for key, value in nx_graph.items()])
    nodes = list()
    i=0
    while i < matrix_len -1:
        if round(graph.degree_centrality(i),5)!= round(graph_matrix[i,1],5):
            nodes.append(i)
        i +=1
    assert len(nodes)==0
    return
def test_degree_values():
    """Testing the accuracy of node degree calculation."""
    graph = File().read_file(r"C:\Users\atiye\Centrality-In-Graphs\src\CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len = len(adj_matrix)
    nx_graph = nx.Graph(adj_matrix)
    nodes = list()
    i=0
    while i < matrix_len -1:
        if graph.get_degree(i)!= nx_graph.degree(i):
            nodes.append(i)
        i +=1
    assert len(nodes)==0
def test_shortest_path():
    """Testing the accuracy of calculating the shortest path length between two nodes."""
    graph = File().read_file(r"C:\Users\atiye\Centrality-In-Graphs\src\CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    nx_graph = nx.Graph(adj_matrix)
    matrix_len = len(adj_matrix)
    nodes = list()
    i=0
    j=0
    while i < matrix_len -1:
        while j < matrix_len -1:
            if i !=j:
                short_path= nx.shortest_path(nx_graph,source=i,target=j)
                if graph.get_shortest_path(i,j)!=len(short_path)-1:
                    nodes.append(i)
            j += 1
        j=0
        i +=1
    assert len(nodes)==0
    return
