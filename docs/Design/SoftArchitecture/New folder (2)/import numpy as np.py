def calculate_degree_centrality(graph):
    degree_count = {}
    for edge in graph:
        degree_count[edge[0]] = degree_count.get(edge[0], 0) + 1
        degree_count[edge[1]] = degree_count.get(edge[1], 0) + 1
    degree_centrality = {}
    num_nodes = len(degree_count)
    for node, degree in degree_count.items():
        degree_centrality[node] = degree / (num_nodes - 1) 
    return degree_centrality
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