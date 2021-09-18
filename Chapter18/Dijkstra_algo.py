import sys
sys.path.append('./')

from Chapter16.heaps import Heap
from weighted_graphs import WeightedGraph


def dijkstras_algo(source, destination):
    min_prices_from_source_city = {source.vertex: 0}
    min_price_from_start_city_via_stepover_city = {}

    unvisited_cites = Heap(source)

    visited_cities = {}

    while unvisited_cites:
        current_city = unvisited_cites.delete()
        visited_cities[source.vertex] = True
        for adj_city, price in current_city.adjecent_vertices.items():
            if visited_cities.get(adj_city, False):
                unvisited_cites.insert(adj_city)
            print("Adjecent_city ", adj_city)
            print("Price ", price)
        
        current_city = unvisited_cites.delete()
    print("Algo end")




            

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

    dijkstras_algo(atlanta, denver)