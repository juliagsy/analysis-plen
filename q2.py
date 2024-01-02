from graph import *
import numpy as np
from utils import *


# network init

pl_network = create_pl_graph()
pl_random_network = maximal_random_rewiring(pl_network)

print(f"pl_network total nodes: {len(pl_network.nodes)}")
print(f"pl_network total edges: {len(pl_network.edges)}")
print()


# community

pl_communities = nx.community.greedy_modularity_communities(pl_network, resolution=1.35)
pl_communities = sorted(pl_communities, key=len, reverse=True)
pl_mod = nx.community.modularity(pl_network, pl_communities)

print(f"pl_network largest modularity: {pl_mod}")
print(f"pl_network number of communities: {len(pl_communities)}")
print(f"pl_network top 5 largest communities sizes: {len(list(pl_communities[0]))}, {len(list(pl_communities[1]))}, {len(list(pl_communities[2]))}, {len(list(pl_communities[3]))}, {len(list(pl_communities[4]))}")
# print("\n", pl_communities)
print()


# plots

plot_network(1, pl_network, pl_communities, with_labels=False, node_size=50)

show_graph()