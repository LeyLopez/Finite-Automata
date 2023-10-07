class Directed_Graph:
    def __init__(self):
        self.graph_dict = {}
        
    def add_vertex(self, vertex):
        self.graph_dict[vertex] = []
            
    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        value=edge.get_value()
        self.graph_dict[v1].append((v2, value))
        
    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict
    
    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name==v.get_name():
                return v
        print(f"Vertex {vertex_name} does not exist")
    
    def get_neightbours(self, vertex):
        return self.graph_dict[vertex]
    
    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2,value in self.graph_dict[v1]:
                all_edges += f"{v1.get_name()} ----({value})---> {v2.get_name()}"
        
        return all_edges
                
        
            

class Edge:
    def __init__(self, v1, v2, value):
        self.v1 = v1
        self.v2 = v2
        self.value=value
        
    def get_v1(self):
        return self.v1
    
    def get_v2(self):
        return self.v2
    
    def get_value(self):
        return self.value
    
    
    def __str__(self):
        return f"{self.v1.get_name()} -----{self.get_value}----->{self.v2.get_name()}"
    
    


class Vertex:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    
    

    
    
def build_graph(graph):
    g = graph()
    for v in  ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x'):
        g.add_vertex(Vertex(v))
        
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('a'), 34))
    
    return g
    
        
G1 = build_graph(Directed_Graph)
        
print(G1)       
    