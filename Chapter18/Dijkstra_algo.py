import sys
sys.path.append('./')

from Chapter16.heaps import Heap
from weighted_graphs import WeightedGraph
from graphs import Graph


# class PQ(Heap):
#     """
#     Takes Weighted graphs as nodes but sorts them based on as node weights.
#     """
#     def __init__(self, root, val) -> None:
#         super().__init__(root)
#         self.root

#     def __lt__(self, obj):
#         pass
        



def dijkstras_algo(source, destination):
    min_prices_from_source_city = {source.vertex: 0}
    min_price_from_start_city_via_stepover_city = {}

    unvisited_cites = [source]

    visited_cities = {}

    current_city = source
    while unvisited_cites:
        # Removing the current city as we are visiting it, from unvisited cities.
        unvisited_cites = list(filter(lambda x: x != current_city, unvisited_cites))
        visited_cities[current_city.vertex] = True
        for adj_city, price in current_city.adjecent_vertices.items():
            if not visited_cities.get(adj_city, False):
                unvisited_cites.append(adj_city)

                # Here we update the 2 hash tables/dictionaries to contain the shortest weight and the corresponding path to take to achieve it.
                if x:=min_prices_from_source_city.get(adj_city.vertex, -1):
                    price_to_get_here = min_prices_from_source_city[current_city.vertex] + price
                    if x == -1 or price_to_get_here < x:
                        min_prices_from_source_city[adj_city.vertex] = price_to_get_here
                        min_price_from_start_city_via_stepover_city[adj_city.vertex] = current_city.vertex

            print(f"Adjecent_city {adj_city.vertex} with price {price}")
        
        if unvisited_cites:
            # Here, we apply the logic which can be better implemented with Priority Queues.
            current_cheapest_city_price = min_prices_from_source_city[unvisited_cites[0].vertex]
            current_city = unvisited_cites[0]
            for _ in unvisited_cites:
                if current_cheapest_city_price > min_prices_from_source_city[_.vertex]:
                    current_city = _

    print("Algo end")

    print(min_prices_from_source_city)
    print("-------------------")
    print(min_price_from_start_city_via_stepover_city)

    print('_______________________')
    starting_point = source.vertex
    l = []
    look_for = destination.vertex
    while look_for != source.vertex:
        l.append(look_for)
        look_for = min_price_from_start_city_via_stepover_city[look_for]
    l.append(source.vertex)
    l = l[::-1]
    print("->".join(l))
            

    # Need to figure out a way to get the visited cities.
    
def dijkstras_algo_assignment(source, destination):
    min_prices_from_source_city = {source.vertex: 0}
    min_price_from_start_city_via_stepover_city = {}

    unvisited_cites = [source]

    visited_cities = {}

    current_city = source
    while unvisited_cites:
        # Removing the current city as we are visiting it, from unvisited cities.
        unvisited_cites = list(filter(lambda x: x.vertex != current_city.vertex, unvisited_cites))
        print([x.vertex for x in unvisited_cites])
        visited_cities[current_city.vertex] = True

        for adj_city in current_city.adjecent_vertices:
            if not visited_cities.get(adj_city.vertex, False):
                unvisited_cites.append(adj_city)

                # Here we update the 2 hash tables/dictionaries to contain the shortest weight and the corresponding path to take to achieve it.
                if x:=min_prices_from_source_city.get(adj_city.vertex, -1):
                    price_to_get_here = min_prices_from_source_city[current_city.vertex] + 1
                    if x == -1 or price_to_get_here < x:
                        min_prices_from_source_city[adj_city.vertex] = price_to_get_here
                        min_price_from_start_city_via_stepover_city[adj_city.vertex] = current_city.vertex

        
        if unvisited_cites:
            # Here, we apply the logic which can be better implemented with Priority Queues.
            current_cheapest_city_price = min_prices_from_source_city[unvisited_cites[0].vertex]
            current_city = unvisited_cites[0]
            for _ in unvisited_cites:
                if current_cheapest_city_price > min_prices_from_source_city[_.vertex]:
                    current_city = _

    print("Algo end")

    print(min_prices_from_source_city)
    print("-------------------")
    print(min_price_from_start_city_via_stepover_city)

    print('_______________________')
    starting_point = source.vertex
    l = []
    look_for = destination.vertex
    while look_for != source.vertex:
        l.append(look_for)
        look_for = min_price_from_start_city_via_stepover_city[look_for]
    l.append(source.vertex)
    l = l[::-1]
    print("->".join(l))


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

    # dijkstras_algo(atlanta, el_paso)
    idris = Graph('Idris')
    talia = Graph('Talia')
    kamil = Graph('Kamil')
    lina = Graph('Lina')
    ken = Graph('Ken')
    marco = Graph('Marco')
    sasha = Graph('Sasha')

    idris.add_adjecent_vertex([kamil, talia])
    talia.add_adjecent_vertex(ken)
    ken.add_adjecent_vertex(marco)
    marco.add_adjecent_vertex(sasha)
    sasha.add_adjecent_vertex(lina)
    lina.add_adjecent_vertex(kamil)

    dijkstras_algo_assignment(idris, sasha)





