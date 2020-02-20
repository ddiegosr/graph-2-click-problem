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


def read_input_file(file_name):
    file = open(file_name, 'r')
    readed_nodes = file.readline().strip()

    nodes_list = readed_nodes.split('|')

    readed_edges = list(map(lambda line: line.strip(), file.readlines()))
    edges_list = []

    for edge in readed_edges:
        split = edge.split(' ')
        edges_list.append((split[0], split[1]))

    return nodes_list, edges_list


def can_be_two_cliques(G):
    complement = gen_complement_graph(G)
    save_graph_to_file(complement, "complement.png")
    graph_is_bipartite = is_bipartite(complement)

    if not graph_is_bipartite:
        print("False. This graph can't be divided in two cliques")
        return

    print("True. This graph can be divided in two cliques")


def verify_edge_numbers(nodes_list, edges_lists):
    nodes_len = len(nodes_list)
    edges_len = len(edges_lists)
    maximum = (nodes_len * (nodes_len - 1)) / 2
    if edges_len > maximum:
        raise Exception('The numbers of edges is higher than the maximum allowed for this graph')
