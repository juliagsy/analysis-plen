from graph import *
import numpy as np
from utils import *


# network init

pl_network = create_pl_graph()
pl_random_network = maximal_random_rewiring(pl_network)

print(f"pl_network total nodes: {len(pl_network.nodes)}")
print(f"pl_network total edges: {len(pl_network.edges)}")
print()


# in/out degree

_, pl_all_in_degs = get_all_degs(pl_network, True)
_, pl_all_out_degs = get_all_degs(pl_network, False)

print(f"pl_network average in-degree: {np.mean(pl_all_in_degs)}")
print(f"pl_network average out-degree: {np.mean(pl_all_out_degs)}\n")

print(f"pl_network maximum in-degree: {np.max(pl_all_in_degs)}")
print(f"pl_network maximum out-degree: {np.max(pl_all_out_degs)}\n")
print()


pl_in_k, pl_in_Pk = calculate_all_degs(pl_network, True)
pl_out_k, pl_out_Pk = calculate_all_degs(pl_network, False)


# assortativity coefficient

pl_in_in_ac = nx.degree_assortativity_coefficient(pl_network, x="in", y="in")
pl_in_out_ac = nx.degree_assortativity_coefficient(pl_network, x="in", y="out")
pl_out_in_ac = nx.degree_assortativity_coefficient(pl_network, x="out", y="in")
pl_out_out_ac = nx.degree_assortativity_coefficient(pl_network, x="out", y="out")

print(f"pl_network average assortativity coefficient in-in: {pl_in_in_ac}")
print(f"pl_network average assortativity coefficient in-out: {pl_in_out_ac}")
print(f"pl_network average assortativity coefficient out-in: {pl_out_in_ac}")
print(f"pl_network average assortativity coefficient out-out: {pl_out_out_ac}")
print()


# clustering coefficient

pl_cc = nx.average_clustering(pl_network)

print(f"pl_network average clustering coefficient: {pl_cc}")
print()


# page rank / hits

pl_pg = get_top_pagerank(pl_network, 10)
pl_hub, pl_auth = get_hits(pl_network, 10)

print(f"pl_network top 10 pagerank: {pl_pg}")
print(f"pl_network top 10 hub: {pl_hub}")
print(f"pl_network top 10 authority: {pl_auth}")
print()


# betweenness centrality

pl_bc = get_betweenness_centrality(pl_network, 10)

print(f"pl_network betweenness centrality: {pl_bc}")
print()


# plots

plot_graph(1, [pl_in_k, pl_out_k], [pl_in_Pk, pl_out_Pk], ["in deg", "out deg"], "k", "Pk", "Linear plot of Pk")
plot_graph(2, [pl_in_k, pl_out_k], [pl_in_Pk, pl_out_Pk], ["in deg", "out deg"], "k", "Pk", "Log-log scale: in and out degree distribution of PLEN", log=True)

show_graph()