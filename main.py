import utils as utils

if __name__ == '__main__':
    nodes, edges = utils.read_input_file('input.txt')
    utils.verify_edge_numbers(nodes, edges)
    graph = utils.create_graph(nodes, edges)
    utils.save_graph_to_file(graph, "graph.png")
    utils.can_be_two_cliques(graph)
