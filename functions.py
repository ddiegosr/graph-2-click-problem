import networkx as nx
import matplotlib.pyplot as plt


def create_graph(nodes, edges):
    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    return g


def gen_complement_graph(G):
    return nx.complement(G)


def is_bipartite(G):
    return nx.is_bipartite(G)


def save_graph_to_file(G, filename='plot.png'):
    plt.subplot(121)
    nx.draw(G, pos=nx.spiral_layout(G), with_labels=True, font_weight="bold")
    plt.savefig(filename)
    plt.close()
