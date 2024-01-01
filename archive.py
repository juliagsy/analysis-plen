from graph import *
import numpy as np
from utils import *


# network init

pl_network = create_pl_graph()
pl_random_network = maximal_random_rewiring(pl_network)

print(f"pl_network total nodes: {len(pl_network.nodes)}")
print(f"pl_network total edges: {len(pl_network.edges)}")
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


# degree centrality

# pl_in_c = get_centrality(pl_network, True, 10)
# pl_out_c = get_centrality(pl_network, False, 10)

# print(f"pl_network in-degree centrality: {pl_in_c}")
# print(f"pl_network out-degree centrality: {pl_out_c}")
# print()


# plots

# plot_graph(3, [pl_in_in_k, pl_in_out_k, pl_in_io_k, pl_out_in_k, pl_out_out_k, pl_out_io_k, pl_io_in_k, pl_io_out_k, pl_io_io_k], [pl_in_in_knn, pl_in_out_knn, pl_in_io_knn, pl_out_in_knn, pl_out_out_knn, pl_out_io_knn, pl_io_in_knn, pl_io_out_knn, pl_io_io_knn], ["in-in", "in-out", "in-io", "out-in", "out-out", "out-io", "io-in", "io-out", "io-io"], "k", "knn", "Log plot of knn against k", log=True)

# show_graph()