import random
import networkx as nx

# تولید یک دیتاست تصادفی
edges = [(random.randint(1, 200), random.randint(1, 200)) for _ in range(400)]

# ایجاد گراف از لیست یال‌ها
G = nx.Graph(edges)

# یافتن تمام مجموعه‌های متصل
connected_components = list(nx.connected_components(G))

# انتخاب یکی از مجموعه‌ها به عنوان گراف متصل
connected_nodes = list(connected_components[0])
connected_graph = G.subgraph(connected_nodes)

# ذخیره یال‌ها در یک فایل متنی
with open("connected_graph_edges.txt", "w") as file:
    for edge in connected_graph.edges():
        file.write(f"{edge[0]} {edge[1]}\n")
