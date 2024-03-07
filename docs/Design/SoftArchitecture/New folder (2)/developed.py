
import numpy as np 
import networkx as nx

def find_max(matrix):
    max_value = np.amax(matrix)
    return max_value

file_path = 'test.txt' 
matrix = np.loadtxt(file_path)
print("Matrix:")

int_matrix = matrix.astype(int)
print(int_matrix)
print (int_matrix[2, 0])
n= np.amax(int_matrix)
print (n)

def finddegree (matrix):
    n= np.amax(matrix)
    degree= np.zeros((n +1, 2))
    m=0
    while m <=n:
        q=0
        count= np.count_nonzero(matrix[:, 0] == m)
        degree[m:]=[m,count]
        m +=1
    return degree   
print (finddegree(int_matrix))
 
def degreecen (matrix,n):
    degc= finddegree(matrix)
    m=0
    while m<= n:
        degc[m,1]=degc[m,1]/ (n)
        m +=1
    return degc
print (degreecen (int_matrix,n))

def changematrix(matrix):
    n= np.amax(matrix)
    shpath= np.zeros((n +1, n +1))
    for row in matrix:
        shpath[row[0],row[1]]=1
    return shpath
print(changematrix(int_matrix))

def dijkstra(matrix):
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

print(dijkstra(changematrix(int_matrix)))

def cencen(matrix):
    cenmatrix= dijkstra(changematrix(int_matrix))
    n= np.amax(matrix)
    main=np.zeros((n+1 , 2 ))
    i=0
    j=0
    while i<=n:
        main[i,0]=i
        while j <=n:
            main[i,1]=main[i,1]+cenmatrix[i,j]
            j +=1
        j=0    
        i+=1
        
    i=0
    while i<=n:
        main[i,1]=n/main[i,1]
        i+=1
    sorted_indices = np.argsort(main[:,1])
    sorted_indices = sorted_indices[::-1]
    sorted_matrix = main[sorted_indices]
    return (sorted_matrix)
print (cencen(int_matrix))

closeness_centrality = nx.closeness_centrality(int_matrix)
degree_centrality = nx.degree_centrality(int_matrix)       
    
    
      
    
    
    

        
       
    
    
