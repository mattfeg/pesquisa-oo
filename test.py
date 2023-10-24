import networkx as nx

graph = nx.DiGraph()
graph.add_edge(1,2,weight = 3)
graph.add_edge(2,3,weight = 4)
graph.add_edge(3,4,weight = 1)
graph.add_edge(4,1,weight = 5)
graph.add_edge(4,2,weight = 7)

graph2 = nx.DiGraph()
graph2.add_edge(1,2,weight = 6)
graph2.add_edge(2,3,weight = 1)
graph2.add_edge(3,4,weight = 10)
graph2.add_edge(4,1,weight = 9)
graph2.add_edge(4,2,weight = 4)

graph3 = nx.DiGraph()
graph3.add_weighted_edges_from(graph.edges.data('weight'))
print(graph.get_edge_data(1,2))
print(graph3.get_edge_data(1,2))


def criarRedeComplexa(self):
        for i in self.__listaRedes:
            self.__redeComplexa.add_weighted_edges_from(i.edges.data('weight'))