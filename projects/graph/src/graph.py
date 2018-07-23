class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, data):
        if data in self.vertices.keys():
            raise Exception('Vertex %s already exists' % data)
        else:
            self.vertices[data] = set([])

    def add_edge(self, v1, v2):
        if v1 not in self.vertices.keys():
            raise Exception('Vertex %s does not exist' % v1)
        elif v2 not in self.vertices.keys():
            raise Exception('Vertex %s does not exist' % v2)
        elif v1 in self.vertices[v2]:
            raise Exception('Edge already exists')
        else:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
