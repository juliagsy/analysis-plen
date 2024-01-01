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


# knn

# pl_in_in_nn = get_knn(pl_network, "in", "in", 10)
# pl_in_out_nn = get_knn(pl_network, "in", "out", 10)
# pl_in_io_nn = get_knn(pl_network, "in", "in+out", 10)
# pl_out_in_nn = get_knn(pl_network, "out", "in", 10)
# pl_out_out_nn = get_knn(pl_network, "out", "out", 10)
# pl_out_io_nn = get_knn(pl_network, "out", "in+out", 10)
# pl_io_in_nn = get_knn(pl_network, "in+out", "in", 10)
# pl_io_out_nn = get_knn(pl_network, "in+out", "out", 10)
# pl_io_io_nn = get_knn(pl_network, "in+out", "in+out", 10)

# print(f"pl_network top 10 KNN in-in: {pl_in_in_nn}")
# print(f"pl_network top 10 KNN in-out: {pl_in_out_nn}")
# print(f"pl_network top 10 KNN in-io: {pl_in_io_nn}")
# print(f"pl_network top 10 KNN out-in: {pl_out_in_nn}")
# print(f"pl_network top 10 KNN out-out: {pl_out_out_nn}")
# print(f"pl_network top 10 KNN out-io: {pl_out_io_nn}")
# print(f"pl_network top 10 KNN io-in: {pl_io_in_nn}")
# print(f"pl_network top 10 KNN io-out: {pl_io_out_nn}")
# print(f"pl_network top 10 KNN io-io: {pl_io_io_nn}")
# print()

# pl_in_in_k, pl_in_in_knn = calculate_knn(pl_network, "in", "in")
# pl_in_out_k, pl_in_out_knn = calculate_knn(pl_network, "in", "out")
# pl_in_io_k, pl_in_io_knn = calculate_knn(pl_network, "in", "in+out")
# pl_out_in_k, pl_out_in_knn = calculate_knn(pl_network, "out", "in")
# pl_out_out_k, pl_out_out_knn = calculate_knn(pl_network, "out", "out")
# pl_out_io_k, pl_out_io_knn = calculate_knn(pl_network, "out", "in+out")
# pl_io_in_k, pl_io_in_knn = calculate_knn(pl_network, "in+out", "in")
# pl_io_out_k, pl_io_out_knn = calculate_knn(pl_network, "in+out", "out")
# pl_io_io_k, pl_io_io_knn = calculate_knn(pl_network, "in+out", "in+out")


# page rank / hits

pl_pg = get_top_pagerank(pl_network, 10)
pl_hub, pl_auth = get_hits(pl_network, 10)

print(f"pl_network top 10 pagerank: {pl_pg}")
print(f"pl_network top 10 hub: {pl_hub}")
print(f"pl_network top 10 authority: {pl_auth}")
print()


# degree centrality

pl_in_c = get_centrality(pl_network, True, 10)
pl_out_c = get_centrality(pl_network, False, 10)

print(f"pl_network in-degree centrality: {pl_in_c}")
print(f"pl_network out-degree centrality: {pl_out_c}")
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

# plot_graph(1, [pl_in_k, pl_out_k], [pl_in_Pk, pl_out_Pk], ["in deg", "out deg"], "k", "Pk", "Linear plot of Pk")
# plot_graph(2, [pl_in_k, pl_out_k], [pl_in_Pk, pl_out_Pk], ["in deg", "out deg"], "k", "Pk", "Log-log scale: in and out degree distribution of PLEN", log=True)
# plot_graph(3, [pl_in_in_k, pl_in_out_k, pl_in_io_k, pl_out_in_k, pl_out_out_k, pl_out_io_k, pl_io_in_k, pl_io_out_k, pl_io_io_k], [pl_in_in_knn, pl_in_out_knn, pl_in_io_knn, pl_out_in_knn, pl_out_out_knn, pl_out_io_knn, pl_io_in_knn, pl_io_out_knn, pl_io_io_knn], ["in-in", "in-out", "in-io", "out-in", "out-out", "out-io", "io-in", "io-out", "io-io"], "k", "knn", "Log plot of knn against k", log=True)
plot_network(4, pl_network, pl_communities)

show_graph()