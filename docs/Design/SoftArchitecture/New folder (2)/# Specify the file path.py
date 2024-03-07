# Specify the file path
file_path = 'p2p-Gnutella04.txt'

# Read the file and convert values to integers
with open(file_path, 'r') as file:
    matrix = [list(map(int, line.split())) for line in file]

# Print the matrix
print("Matrix from file:")
for row in matrix:
    print(row)
