from dotpy.components.node import Node
from dotpy.components.edge import Edge

class Digraph:

    def __init__(self, name, stmt_list):
        self.name = name
        self.stmt_list = stmt_list

    def __str__(self):
        return 'digraph {0} {{\n{1}\n}}'.format(self.name, "\n".join(map(str, self.stmt_list)))

    def get_nodes(self):
        nodes = []
        for stmt in self.stmt_list:
            if isinstance(stmt, Node):
                nodes.append(stmt)
        return nodes

    def get_edges(self):
        edges = []
        for stmt in self.stmt_list:
            if isinstance(stmt, Edge):
                edges.append(stmt)
        return edges

    def delete_node(self, name):
        for stmt in self.stmt_list:
            if isinstance(stmt, Node) and stmt.name == name:
                self.stmt_list.remove(stmt)

    def delete_edge(self, source, destination):
        for stmt in self.stmt_list:
            if isinstance(stmt, Edge) and stmt.source == source and stmt.destination == destination:
                self.stmt_list.remove(stmt)

    def add_edge(self, source, destination):
        self.stmt_list.append(Edge(source, destination, []))

    def is_singleton(self):
        nodes = self.get_nodes()
        if len(nodes) > 2:
            return False
        else:
            return True