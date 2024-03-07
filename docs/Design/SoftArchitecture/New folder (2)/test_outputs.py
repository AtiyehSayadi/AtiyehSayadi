from main import degree_centrality ,centrality_closeness
import numpy as np #[using matrix]
def test_degree_centrality():
    matrix= degree_centrality()
    matrix_len=len(matrix)
    i=0
    j=0
    f=0
    not_inserted=list()
    while i< matrix_len:
        while j< matrix_len:
            if matrix[j,0]== i:
                f=1
            j +=1
        if f != 1:
            not_inserted.append(i)
        j=0
        i+=1
    if len(not_inserted)==0:
        print("All nodes are included")
    else:
        assert (not_inserted)
    return 
def test_closeness_centrality():
    matrix= centrality_closeness()
    matrix_len=len(matrix)
    i=0
    j=0
    f=0
    not_inserted=list()
    while i< matrix_len:
        while j< matrix_len:
            if matrix[j,0]== i:
                f=1
            j +=1
        if f != 1:
            not_inserted.append(i)
        j=0
        i+=1
    if len(not_inserted)==0:
        print("All nodes included")
    else:
        assert (not_inserted)
    return 

                
                
            
            
            
      
    