class Graph:
    def __init__(self, Nodes, is_directed=False):
        self.Nodes = Nodes
        self.args_list = {}
        self.is_directed = is_directed

        for node in self.Nodes:
            self.args_list[node] = []

    def add_edges(self, u, v):
        self.args_list[u].append(v)
        if not self.is_directed:
            self.args_list[v].append(u)

    def degree(self, Node):
        return len(self.args_list[Node])

    def print(self):
        for node in self.Nodes:
            print(node, "-->", self.args_list[node])


v = ["A", "B", "C", "D", "E"]
graph = Graph(v, is_directed=True)
edge_value = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]
for i, j in edge_value:
    graph.add_edges(i, j)

graph.print()
# graph.degree("A")
print("The degree of vertice", graph.degree("A"))
