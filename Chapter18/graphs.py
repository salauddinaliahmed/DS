class Graph:
    def __init__(self, value) -> None:
        self.vertex = value
        # Holds values/objects of its neighbours.
        self.adjecent_vertices = []

    # def add_adjecent_vertex(self, vertex):
    #     # This is a directed graph, the relationships are not necessarily two way.
    #     self.adjecent_vertices.append(vertex)

    def add_adjecent_vertex(self, vertex):
        # Undirected graph, meaning all relationships go two ways.

        if vertex in self.adjecent_vertices:
            return
        # Add the vertex to the current object.
        self.adjecent_vertices.append(vertex)

        # Add the current object/ self to the passed argument (vertex's) adjecent vertices.
        vertex.add_adjecent_vertex(self)

        #vertex.adjecent_vertices.append(self)

    @staticmethod
    def depth_first_search(node=None, traversed_dict={}):
        for each_node in node.adjecent_vertices:
            if traversed_dict.get(each_node, False):
                return False
            print("Printer", each_node.vertex)
            traversed_dict[each_node] = True
            Graph.depth_first_search(node=each_node, traversed_dict=traversed_dict)

    def dfs(self, node=None):
        if not node:
            node=self
        
        self.depth_first_search(node=node)
        return False

    def __str__(self) -> str:
        vertices = [_.vertex for _ in self.adjecent_vertices]
        return f"{self.vertex} has connection with the following nodes/vertices: {', '.join(vertices)}"


if __name__=='__main__':
    a = Graph('Adam')
    e = Graph('Eve')
    ab = Graph('Able')
    a.add_adjecent_vertex(e)
    a.add_adjecent_vertex(ab)
    e.add_adjecent_vertex(Graph('Bella'))
    a.dfs()