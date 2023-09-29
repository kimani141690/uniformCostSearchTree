import matplotlib.pyplot as plt
import networkx as nx

# Create a graph object
G = nx.Graph()
coordinates = {
    'Sports\nComplex': (-6, 2),
    'Siwaka': (-4, 2),
    'Phase1A': (-2, 2),
    'Phase1B': (-2, 0),
    'Phase2': (0, 0),
    'J1': (2, 0),
    'Mada': (4,0 ),
    'STC': (-2, -2),
    'Phase3': (2, -2),
    'Parking\nlot': (2, -4),
}

# Add nodes
G.add_nodes_from(coordinates.keys())

# Add edges with distances as weights
edges_with_distances = [
    ('Sports\nComplex', 'Siwaka', {'weight': 450}),
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
    ('Mada', 'Parking\nlot', {'weight': 700}),
    ('Phase3', 'Parking\nlot', {'weight': 350}),
    ('STC', 'Parking\nlot', {'weight': 250}),





]
G.add_edges_from(edges_with_distances)

# Draw the graph
# pos = nx.spring_layout(G, seed=42)  # positions for all nodes
nx.draw(G, coordinates, with_labels=True, font_weight='bold', node_size=3000, node_color='green', font_size=10)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, coordinates, edge_labels=edge_labels)

plt.title('Madaraka Estate Network with Distances')
plt.show()
