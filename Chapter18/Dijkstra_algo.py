from weighted_graphs import WeightedGraph

def dijkstras_algo(source, destination):
    pass


if __name__ == '__main__':
    atlanta = WeightedGraph('Atlanta')
    boston = WeightedGraph('Boston')
    chicago = WeightedGraph('Chicago')
    denver = WeightedGraph('Denver')
    el_paso = WeightedGraph('El Paso')

    atlanta.add_adjecent_vertex(boston, 100)
    atlanta.add_adjecent_vertex(denver, 160)
    boston.add_adjecent_vertex(chicago, 120)
    boston.add_adjecent_vertex(denver, 180)
    chicago.add_adjecent_vertex(el_paso, 80)
    denver.add_adjecent_vertex(chicago, 40)
    denver.add_adjecent_vertex(el_paso, 140)

    print(atlanta)