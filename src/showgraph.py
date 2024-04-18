"""GUI Module"""
import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from src.file import File
class ShowGraph:
    """A class for graph visualization and computations."""
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Show Graphs")
        self.win.geometry("400x300")
        self.degree_button = tk.Button(self.win, text="Degree Centrality",
        command=lambda: self.show_degree_centrality(File().read_file("CIG-data.txt")),
        bg="pink", font=("Calibri", 20, "bold"), width=20)
        self.degree_button.pack(pady=50)
        self.closeness_button = tk.Button(self.win, text="Closeness Centrality",
        command=lambda: self.show_closeness_centrality(File().read_file("CIG-data.txt")),
        bg="lightblue",font=("Calibri", 20, "bold") , width=20)
        self.closeness_button.pack(pady=20)

    def show_degree_centrality(self, graph):
        """Graph visualization for degree centrality."""
        plt.figure("Degree Centrality")
        graph_diagram = nx.Graph(graph.get_adj_matrix())
        pos = nx.spring_layout(graph_diagram)
        centrality_values = [graph.degree_centrality(int(node)) for node in graph_diagram.nodes()]
        min_size = 200
        max_size = 2000
        scaled_sizes = [min_size + (max_size - min_size) * (centrality - min(centrality_values)) /
        (max(centrality_values) - min(centrality_values)) for centrality in centrality_values]
        nx.draw(graph_diagram, pos, edge_color='red',
        node_color='lightblue', node_size=scaled_sizes)
        labels = {node: f"{node}= {graph.degree_centrality(int(node)):.2f}"
        for node in graph_diagram.nodes()}
        nx.draw_networkx_labels(graph_diagram, pos, labels=labels, font_size=6)
        plt.show()
    def show_closeness_centrality(self, graph):
        """Graph visualization for closeness centrality."""
        plt.figure("Closeness Centrality")
        graph_diagram = nx.Graph(graph.get_adj_matrix())
        for node in graph_diagram.nodes():
            if graph.get_degree(int(node))==0:
                pos = nx.spring_layout(graph_diagram)
                nx.draw(graph_diagram, pos, edge_color='red',
                node_color='lightblue', node_size=500)
                labels = {node: f"{node}= {0:.2f}"
                for node in graph_diagram.nodes()}
                nx.draw_networkx_labels(graph_diagram, pos, labels=labels, font_size=6)
                plt.show()
                return
        pos = nx.spring_layout(graph_diagram)
        centrality_values =[graph.closeness_centrality(int(node))for node in graph_diagram.nodes()]
        min_size = 200
        max_size = 2000
        scaled_sizes = [min_size + (max_size - min_size)* (centrality - min(centrality_values)) /
        (max(centrality_values) - min(centrality_values))
        for centrality in centrality_values]
        nx.draw(graph_diagram, pos, edge_color='red',
        node_color='lightblue', node_size=scaled_sizes)
        labels = {node: f"{node}= {graph.closeness_centrality(int(node)):.2f}"
        for node in graph_diagram.nodes()}
        nx.draw_networkx_labels(graph_diagram, pos, labels=labels, font_size=6)
        plt.show()
gui = ShowGraph()
gui.win.mainloop()
