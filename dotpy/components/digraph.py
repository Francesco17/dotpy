class Digraph:

    def __init__(self, name, stmt_list):
        self.name = name
        self.stmt_list = stmt_list

    def __str__(self):
        return 'digraph {0} {{\n {1}\n}}'.format(self.name, "\n".join(map(str, self.stmt_list)))