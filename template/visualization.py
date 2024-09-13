from graphviz import Digraph

def parse_input(input_data):
    graph_data = {}
    for line in input_data:
        parts = line.split(':')
        key = parts[0].strip()
        values = parts[1].strip().split(' ')
        graph_data[key] = values
    return graph_data

def visualize_graph(graph_data):
    dot = Digraph(comment='The Graph')

    # Add nodes and edges
    for node, edges in graph_data.items():
        dot.node(node, node)
        for edge in edges:
            if edge:  # Check for empty strings
                dot.edge(node, edge)

    # Render and view the graph
    dot.render('output_graph.gv', view=True)

input_data = [
    "jqt: rhn xhk nvd",
    "rsh: frs pzl lsr",
    "xhk: hfx",
    "cmg: qnr nvd lhk bvb",
    "rhn: xhk bvb hfx",
    "bvb: xhk hfx",
    "pzl: lsr hfx nvd",
    "qnr: nvd",
    "ntq: jqt hfx bvb xhk",
    "nvd: lhk",
    "lsr: lhk",
    "rzs: qnr cmg lsr rsh",
    "frs: qnr lhk lsr"
]

graph_data = parse_input(input_data)
visualize_graph(graph_data)
