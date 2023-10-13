from Rede import *

class RedeComplexa:
    def __init__(self) -> None:
        self.__listaRedes = []
        self.__redeComplexa = nx.DiGraph()
    
    @property
    def listaRedes(self):
        return self.__listaRedes
    
    def addlistaRedes(self,rede):
        self.__listaRedes.append(rede)
    
    def QuantidadeRedes(self):
        return print(len(self.__listaRedes))
    
    def criarRedeComplexa(self,):
        for i in self.__listaRedes:
            print("Add nodes: ",i)
            self.__redeComplexa.add_nodes_from(i.rede.nodes)
            self.__redeComplexa.add_edges_from(i.rede.edges)
            #for no in i.rede.nodes:
            #    self.__redeComplexa.add_node(no)
            print("Add arestas: ",i)
            #for arestas in i.rede.nodes:
            #    self.__redeComplexa.add_edge(arestas[0],arestas[1])
        print("Nos RC: ",len(self.__redeComplexa.nodes))
        print("Arestas RC: ",len(self.__redeComplexa.edges))
    
    def mostrarRedeComplexa(self):
        nx.draw(self.__redeComplexa, with_labels=True)
        plt.show()
              
    def MostrarRedesIndividuais(self,rede: Rede):
        for i in self.__listaRedes:
            i.rede.MostrarRede()