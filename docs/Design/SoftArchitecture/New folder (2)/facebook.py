import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt

def readfile():
    file_path = 'facebook_combined.txt' 
    matrix = np.loadtxt(file_path)
    intmatrix = matrix.astype(int)
    return (intmatrix)

def changematrix():
    matrix= readfile()
    n= np.amax(matrix)
    shpath= np.zeros((n +1, n +1))
    for row in matrix:
        shpath[row[0],row[1]]=1
        shpath[row[1],row[0]]=1
    return shpath
G = nx.from_numpy_array(changematrix())

print (nx.closeness_centrality(G))
nx.draw(G, with_labels=True)
plt.savefig("graph.png") 

def is_connected(matrix):
    n = len(matrix)
    visited = [False] * n

    # انتخاب یک گره به عنوان نقطه شروع
    start_node = next((i for i, v in enumerate(visited) if not v), None)

    if start_node is None:
        # اگر همه گره‌ها بازدید شده‌اند (یعنی گراف خالی است)
        return False

    stack = [start_node]
    visited[start_node] = True

    while stack:
        current_node = stack.pop()
        for neighbor in range(n):
            if matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True

    return all(visited)
# بررسی اتصال گراف
matrix=changematrix()
print (matrix)
print(is_connected(matrix))