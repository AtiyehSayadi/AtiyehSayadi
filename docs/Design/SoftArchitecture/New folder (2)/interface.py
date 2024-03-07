import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_graph():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)

    plt.close()  # بستن پنجره متعلق به متپلت‌لیب
    canvas.draw()

# ساختن پنجره
root = tk.Tk()
root.title("Graph Viewer")

# ساختن شیء Figure و Canvas برای نمایش گراف
fig = plt.figure(figsize=(6, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# دکمه برای نمایش گراف
draw_button = tk.Button(root, text="Draw Graph", command=draw_graph)
draw_button.pack(side=tk.BOTTOM)

root.mainloop()
