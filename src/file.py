"""File Module"""
import numpy as np
from src.graph import Graph
class File:
    """This module is for reading files."""    
    def read_file(self, filename):
        """This function reads the file from the input and calls Graph module."""
        file = np.loadtxt(filename)
        int_matrix = file.astype(int)
        graph= Graph(np.max(int_matrix)+1)
        for row in int_matrix:
            graph.add_edge(row[0],row[1])
        return graph