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

pl_communities = nx.community.greedy_modularity_communities(pl_network, resolution=1.5)
# pl_communities = nx.community.louvain_communities(pl_network, resolution=1.5)
pl_communities = sorted(pl_communities, key=len, reverse=True)
pl_mod = nx.community.modularity(pl_network, pl_communities)

print(f"pl_network largest modularity: {pl_mod}")
print(f"pl_network number of communities: {len(pl_communities)}")
print(f"pl_network top3 largest communities sizes: {len(list(pl_communities[0]))}, {len(list(pl_communities[2]))}, {len(list(pl_communities[2]))}")
print()


# plots

plot_network(1, pl_network, pl_communities)

show_graph()