import networkx as nx
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# utils

def sort_dict(graph_dict, reverse=False, top_k=None):
    if top_k is None:
        top_k = len(graph_dict)
    return {n: graph_dict[n] for n in sorted(graph_dict, reverse=reverse)[:top_k]}


# properties

def get_all_degs(graph, in_deg):
    all_degs = list(graph.in_degree) if in_deg else list(graph.out_degree)
    n = [d[0] for d in all_degs]
    degs = [d[1] for d in all_degs]
    return n, degs


def calculate_all_degs(graph, in_deg):
    all_degs = list(graph.in_degree) if in_deg else list(graph.out_degree)
    inverse_deg = {}
    for n, d in all_degs:
        if d in inverse_deg:
            inverse_deg[d].append(n)
        else:
            inverse_deg[d] = [n]

    final_degs = {}
    N = len(list(graph.nodes))
    inverse_deg = sort_dict(inverse_deg)
    for d, ns in inverse_deg.items():
        final_degs[d] = len(ns) / N
    return list(final_degs.keys()), list(final_degs.values())


def get_top_pagerank(graph, top_k):
    pg = nx.pagerank(graph)
    inverse_pg = {}
    for n, v in pg.items():
        if v != 0:
            inverse_pg[v] = n
    return sort_dict(inverse_pg, reverse=True, top_k=top_k)


def get_hits(graph, top_k):
    hub, auth = nx.hits(graph)
    inverse_hub = {}
    inverse_auth = {}
    for n, v in hub.items():
        if v != 0:
            inverse_hub[v] = n
    for n, v in auth.items():
        if v != 0:
            inverse_auth[v] = n
    return sort_dict(inverse_hub, reverse=True, top_k=top_k), sort_dict(inverse_auth, reverse=True, top_k=top_k)


def get_knn(graph, source, target, top_k):
    all_knns = nx.average_neighbor_degree(graph, source=source, target=target)
    inverse_knn = {}
    for n, v in all_knns.items():
        if v in all_knns:
            inverse_knn[v].append(n)
        else:
            inverse_knn[v] = [n]
    inverse_knn = sort_dict(inverse_knn, reverse=True, top_k=top_k)
    return inverse_knn


def calculate_knn(graph, source, target):
    all_knns = nx.average_degree_connectivity(graph, source=source, target=target)
    all_knns = sort_dict(all_knns)
    return list(all_knns.keys()), list(all_knns.values())


def get_centrality(graph, in_deg):
    all_c = nx.in_degree_centrality(graph) if in_deg else nx.out_degree_centrality(graph)
    inverse_c = {}
    for n, v in all_c.items():
        if v in all_c:
            inverse_c[v].append(n)
        else:
            inverse_c[v] = [n]
    inverse_c = sort_dict(inverse_c, reverse=True)
    return inverse_c


# rewiring

def maximal_random_rewiring(graph, n=10000):
    new_graph = nx.DiGraph(graph)
    new_graph = nx.directed_edge_swap(new_graph, nswap=n, max_tries=n*100)
    return new_graph    


# plotting

def create_node_colors(graph, communities):
    number_of_colors = len(communities)
    colors = list(matplotlib.colors.cnames.values())[:number_of_colors]
    node_colors = []
    for node in graph:
        current_community_index = 0
        for community in communities:
            if node in community:
                node_colors.append(colors[current_community_index])
                break
            current_community_index += 1
    return node_colors


def plot_graph(fig_num, xs, ys, labels, xlabel, ylabel, title, *, xlim=None, ylim=None, log=False):
    plt.figure(fig_num)
    plt_f = plt.loglog if log else plt.plot
    for i in range(len(labels)):
        plt_f(xs[i], ys[i], label=labels[i])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()
        if xlim is not None:
            plt.xlim(xlim[0], xlim[1])
        if ylim is not None:
            plt.ylim(ylim[0], ylim[1])


def plot_network(fig_num, network, community):
    plt.figure(fig_num)
    plt.title("Community structure of pl_network")
    node_colors = create_node_colors(network, community)
    nx.draw(network, node_size=50, node_color=node_colors)


def show_graph():
    plt.show()
