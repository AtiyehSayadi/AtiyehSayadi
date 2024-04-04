import numpy as np
import networkx as nx
from file import*
from graph import*
from showgraph import *
def test_disconnect():
    graph = File().read_file("disconnect.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len=len(adj_matrix)
    i=0
    nodes=list()
    #a.append(2)
    while i< matrix_len:
        if (graph.closeness_centrality(i) !=0):
            nodes.append(i)
        i +=1
    assert len(nodes) == 0
    return
def test_exist():
    """Testing the correctness of closeness centrality values."""
    graph = File().read_file("CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len = len(adj_matrix)
    exist = graph.exist_edge(-1,matrix_len)
    assert exist==False
    return
def test_degree():
    """Testing the correctness of closeness centrality values."""
    graph = File().read_file("CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len = len(adj_matrix)
    degree = graph.get_degree(matrix_len)
    assert degree==0
    degree = graph.get_degree(-1)
    assert degree==0
    return
def test_shortest_path():
    """Testing the correctness of closeness centrality values."""
    graph = File().read_file("CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len = len(adj_matrix)
    path = graph.get_shortest_path(0,matrix_len)
    assert path==float('inf')
    path = graph.get_shortest_path(-1,matrix_len-1)
    assert path==float('inf')
    return
def test_degree_centrality():
    """Testing the correctness of closeness centrality values."""
    graph = File().read_file("CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len = len(adj_matrix)
    dc = graph.degree_centrality(matrix_len+10)
    assert dc==0
    dc = graph.degree_centrality(-4)
    assert dc==0
    return
def test_closeness_centrality():
    """Testing the correctness of closeness centrality values."""
    graph = File().read_file("CIG-data.txt")
    adj_matrix=graph.get_adj_matrix()
    matrix_len = len(adj_matrix)
    dc = graph.closeness_centrality(matrix_len+14)
    assert dc==0
    dc = graph.closeness_centrality(-7)
    assert dc==0
    return
