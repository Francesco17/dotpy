class Edge:

    def __init__(self, source, destination, attr_list):
        self.source = source
        self.destination = destination
        self.attr_list = attr_list

    def __str__(self):
        if self.attr_list:
            return "{0} -> {1} [{2}];".format(self.source, self.destination, " ".join(map(str, self.attr_list)))
        else:
            return "{0} -> {1};".format(self.source, self.destination)