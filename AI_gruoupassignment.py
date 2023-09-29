import matplotlib.pyplot as plt
import networkx as nx

# Create a graph object
G = nx.Graph()

# Add nodes
nodes = ['SportsCpmplex', 'Siwaka', 'Phase1A', 'Phase1B', 'Phase2', 'J1', 'Mada', 'STC', 'Phase3', 'Parkinglot']
G.add_nodes_from(nodes)

# Add edges with distances as weights
edges_with_distances = [
    ('SportsCpmplex', 'Siwaka', {'weight': 450}),
    ('Siwaka', 'Phase1A', {'weight': 10}),
    ('Siwaka', 'Phase1B', {'weight': 230}),
    ('Phase1A', 'Mada', {'weight': 850}),
    ('Phase1A', 'Phase1B', {'weight': 100}),
    ('Phase1B', 'Phase2', {'weight': 112}),
    ('Phase1B', 'STC', {'weight': 50}),
    ('Phase2', 'J1', {'weight': 600}),
    ('Phase2', 'Phase3', {'weight': 500}),
    ('Phase2', 'STC', {'weight': 50}),
    ('J1', 'Mada', {'weight': 200}),
    ('Mada', 'Parkinglot', {'weight': 700}),
    ('Phase3', 'Parkinglot', {'weight': 350}),
    ('STC', 'Parkinglot', {'weight': 250}),





]
G.add_edges_from(edges_with_distances)

# Draw the graph
pos = nx.spring_layout(G, seed=42)  # positions for all nodes
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1500, node_color='skyblue', font_size=10)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title('Madaraka Estate Network with Distances')
plt.show()
