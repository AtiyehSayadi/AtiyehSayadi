# Specify the file path
import numpy as np
file_path = 'test.txt'  # Adjust the file extension if needed

# Open the file and read lines
matrix = np.loadtxt(file_path)

# نمایش ماتریس
print("Matrix:")
int_matrix = matrix.astype(int)
print(int_matrix)
print (int_matrix[47, 0])
def calculate_degree_centrality(graph):
    degree_count = {}

    # شمارش تعداد یال‌های متصل به هر راس
    for edge in graph:
        # افزودن یک به درجه راس ابتدای یال
        degree_count[edge[0]] = degree_count.get(edge[0], 0) + 1
        # افزودن یک به درجه راس انتهای یال
        degree_count[edge[1]] = degree_count.get(edge[1], 0) + 1

    # محاسبه مرکزیت درجه برای هر راس
    degree_centrality = {}
    num_nodes = len(degree_count)
    for node, degree in degree_count.items():
        degree_centrality[node] = degree / (num_nodes - 1)  # تقسیم بر تعداد کل راس‌ها منهای یک

    return degree_centrality

# مثال استفاده
graph = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D")
]

centrality_scores = calculate_degree_centrality(graph)
print("Degree Centrality Scores:")
for node, centrality in centrality_scores.items():
    print(f"{node}: {centrality}")