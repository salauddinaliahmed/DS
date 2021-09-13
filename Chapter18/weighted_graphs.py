class WeightedGraph:
    def __init__(self, node) -> None:
        self.vertex = node
        self.adjecent_vertices = {}

    def add_adjecent_vertex(self, val, weight):
        self.adjecent_vertices[val] = weight

    def __str__(self):
        return f'{"; ".join([f"{k.vertex}, {val}" for k, val in self.adjecent_vertices.items()])}'


if __name__ == '__main__':
    wbob = WeightedGraph('Bob')
    wtom = WeightedGraph('Tom')
    wbob.add_adjecent_vertex(wtom, 45)
    wtom.add_adjecent_vertex(wbob, 29)
    print(wbob)
    print('-------------')
    print(wtom)