import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges with weights
G.add_edge('ORE', 'A', weight=10)
G.add_edge('ORE', 'B', weight=1)
G.add_edge('A', 'C', weight=7)
G.add_edge('B', 'C', weight=1)
G.add_edge('A', 'D', weight=7)
G.add_edge('C', 'D', weight=1)
G.add_edge('A', 'E', weight=7)
G.add_edge('D', 'E', weight=1)
G.add_edge('A', 'FUEL', weight=7)
G.add_edge('E', 'FUEL', weight=1)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
