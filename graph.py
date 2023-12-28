import csv 
import networkx as nx
import matplotlib.pyplot as plt


def create_pl_graph(file="pl.txt"):
    graph = nx.DiGraph()

    with open(file) as f:
        all_lines = csv.reader(f, delimiter=" ", quotechar='"')
        all_nodes = []
        all_edges = []
        for i, data in enumerate(all_lines):
            if data[0] == "Year":
                all_nodes.append((data[1], {"year": data[2]}))
            elif data[0] == "Cite":
                all_edges.append((data[2], data[1]))

    graph.add_nodes_from(all_nodes)
    graph.add_edges_from(all_edges)

    graph_cc = sorted(nx.weakly_connected_components(graph), key=len, reverse=True)
    graph = graph.subgraph(graph_cc[0])
    return graph


def create_random_network(n, m, seed=3446):
    connected = False
    while not connected:
        graph = nx.gnm_random_graph(n, m, seed=seed, directed=True)
        connected = nx.is_weakly_connected(graph)
        seed += 1
    return graph


def create_ba_network(n, m):
    graph = create_random_network(18, 63, seed=0)
    graph = nx.barabasi_albert_graph(len(list(graph.nodes))+500, 1, initial_graph=graph, seed=0)
    graph = nx.barabasi_albert_graph(len(list(graph.nodes))+800, 2, initial_graph=graph, seed=0)
    graph = nx.barabasi_albert_graph(len(list(graph.nodes))+400, 3, initial_graph=graph, seed=0)
    graph = nx.barabasi_albert_graph(len(list(graph.nodes))+200, 4, initial_graph=graph, seed=0)
    graph = nx.barabasi_albert_graph(len(list(graph.nodes))+100, 6, initial_graph=graph, seed=0)
    graph = nx.barabasi_albert_graph(len(list(graph.nodes))+50, 8, initial_graph=graph, seed=0)
    assert len(list(graph.nodes)) == n
    assert len(list(graph.edges)) == m
    return graph
