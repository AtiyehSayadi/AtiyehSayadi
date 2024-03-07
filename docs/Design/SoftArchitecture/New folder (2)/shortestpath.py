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

def shortest_path():
    """Function printing python version."""
    matrix= change_matrix()
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
            if (node==float('inf')):
                min_distance +=1
                if short_path:
                    node= short_path.pop(0)
                    short_path.append(float('inf'))
                    
            if (node!= float('inf')):
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
    return main

print("dic=",dijkstra())
print(centrality_closeness())
G = nx.from_numpy_array(change_matrix())
print(nx.closeness_centrality(G))