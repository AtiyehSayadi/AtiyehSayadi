"""Module providing a function printing python version."""
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt

def read_file():
    """Function printing python version."""
    file_path = 'test.txt'
    matrix = np.loadtxt(file_path)
    intmatrix = matrix.astype(int)
    return intmatrix

def change_matrix():
    """Function printing python version."""
    matrix= read_file()
    n= np.amax(matrix)
    shpath= np.zeros((n +1, n +1))
    for row in matrix:
        shpath[row[0],row[1]]=1
        shpath[row[1],row[0]]=1
    return shpath
print (change_matrix())

def find_degree():
    """Function printing python version."""
    matrix= change_matrix()
    matrix_size = matrix.shape
    n= matrix_size[0]
    degree= np.zeros((n , 2))
    i=0
    j=0
    while i <n:
        degree[i,0]=i
        while j < n:
            if matrix[i,j]==1:
                degree[i,1] = degree[i,1] + 1
            j +=1
        i += 1
        j =0
    return degree

def degree_centrality ( ):
    """Function printing python version."""
    degc= find_degree( )
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

def dijkstra():
    """Function printing python version."""
    matrix= change_matrix()
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

def centrality_closeness():
    """Function printing python version."""
    matrix= dijkstra( )
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


print (degree_centrality())
print(centrality_closeness())
G = nx.from_numpy_array(change_matrix())
print(nx.degree_centrality(G))
print(nx.closeness_centrality(G))
def is_central():
    G = nx.from_numpy_array(change_matrix())
    if degree_centrality().all()== nx.degree_centrality(G):
        print ("dok")
    else:
        print ("no")
    if centrality_closeness().all()== nx.closeness_centrality(G):
        print ("cok")
    else:
        print ("cno")
    return 
nx.draw(G, with_labels=True)
plt.savefig("graph.png")
print("Hello")  # LF (\n)
print("world")  # LF (\n)
# End-of-file (EOF)
is_central()