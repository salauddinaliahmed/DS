import sys
sys.path.append('../')

from Chapter9 import Queues
# Todo: Learn about imports and creating packages.


class Graph:
    def __init__(self, value) -> None:
        self.vertex = value
        # Holds values/objects of its neighbours.
        self.adjecent_vertices = []

    # def add_adjecent_vertex(self, vertex):
    #     # This is a directed graph, the relationships are not necessarily two way.
    #     self.adjecent_vertices.append(vertex)

    def add_adjecent_vertex(self, vertex):
        if isinstance(vertex, list):
           self.adjecent_vertices.extend(vertex)
           return

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
                continue
            else:
                print('Printer: ', each_node.vertex)
                traversed_dict[each_node] = True
                Graph.depth_first_search(node=each_node, traversed_dict=traversed_dict)

    @staticmethod
    def dfs_find_node(node, search_for, traversed_dict={}):
        """
        This function works recursively by calling itself on each of the adjecent nodes individual node.
        There by adding a node to the call stack with each call to its own adjecent node. 
        We only stop If we find the node that we are following for.


        Here only the else part has the recursive call, so if is the base case of the recursion, which ends the for loop.
        """


        if search_for == node.vertex:
            return node
        for each_node in node.adjecent_vertices:
            if traversed_dict.get(each_node, False):
                continue
            else:
                print('Printer: ', each_node.vertex)
                traversed_dict[each_node] = True
                val = Graph.dfs_find_node(node=each_node,search_for=search_for, traversed_dict=traversed_dict)
                if val:
                    return val
        return None

    def dfs(self, node=None, find_node_val=None):
        if not node:
            node=self
        if not find_node_val:    
            self.depth_first_search(node=node)
        else:
            return self.dfs_find_node(node, find_node_val)

    def __str__(self) -> str:
        vertices = [_.vertex for _ in self.adjecent_vertices]
        return f"{self.vertex} has connection with the following nodes/vertices: {', '.join(vertices)}"

    @staticmethod
    def _bfs(node, find_node_val=None):
        """
        For BFS you visit each of the adjecent vertices of the node sequentially. 
        Without going into each nodes own adjecent node. We use queue keep track of those nodes to move onto next.

        """
        l = []
        l.append(node)
        visted_nodes = {}
        visted_nodes[node]=True
        while l:
            print(f"Printer: {l[0].vertex}")
            for _ in l[0].adjecent_vertices:
                if _.vertex == find_node_val:
                    return _

                if visted_nodes.get(_, False):
                    continue
                    
                else:
                    visted_nodes[_] = True
                    l.append(_)
            l.pop(0)
                    
    
    
    def bfs(self, node=None, find_node_val=None):
        if node == None:
            node = self
        return self._bfs(node, find_node_val=find_node_val)
        

    def bfs_with_queue(self):
        current_node = self
        visited_nodes = {}
        visited_nodes[current_node] = True
        q = Queues.Queue(current_node)
        while q:
            current_node = q.dequeue()
            print("Printer: ", current_node.vertex)
            for each_node in current_node.adjecent_vertices:
                if visited_nodes.get(each_node, False):
                    continue

                q.enqueue(each_node)
                visited_nodes[each_node] = True


if __name__=='__main__':
    a = Graph('Adam')
    e = Graph('Eve')
    ab = Graph('Able')
    bb = Graph('Bopp')
    a.add_adjecent_vertex(e)
    a.add_adjecent_vertex(bb)
    e.add_adjecent_vertex(bb)
    a.add_adjecent_vertex(ab)
    e.add_adjecent_vertex(Graph('Bella'))
    # a.dfs()
    # # print([x.vertex for x in e.adjecent_vertices])
    # val = a.dfs(find_node_val='Able')
    # print(f"Result: {val.vertex}")
    print('_______________________________________')
    a.bfs()
    print('_______________________________________')
    a.bfs_with_queue()
    print(a.bfs(find_node_val='Bella'))
