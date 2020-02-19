import functions as fn


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
    complement = fn.gen_complement_graph(G)
    fn.save_graph_to_file(complement, "complement.png")
    is_bipartite = fn.is_bipartite(complement)

    if not is_bipartite:
        print("False. This graph can't be divided in two cliques")
        return

    print("True. This graph can be divided in two cliques")


if __name__ == '__main__':
    nodes, edges = read_input_file('input.txt')
    graph = fn.create_graph(nodes, edges)
    fn.save_graph_to_file(graph, "graph.png")
    can_be_two_cliques(graph)
