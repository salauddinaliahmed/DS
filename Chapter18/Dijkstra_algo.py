from weighted_graphs import WeightedGraph

def dijkstras_algo(source, destination):
    min_prices_from_source_city = {source.vertex: 0}
    min_price_from_start_city_via_stepover_city = {}
    
    cities_visited = {}
    current_city = source

    # Need to figure out a way to get the visited cities.


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