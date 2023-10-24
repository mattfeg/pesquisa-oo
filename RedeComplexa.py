import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class RedeComplexa:
    def __init__(self) -> None:
        self.__listaRedes = []
        self.__redeComplexa = nx.DiGraph()
    
    @property
    def listaRedes(self):
        return self.__listaRedes
    
    @property
    def redeComplexa(self):
        return self.__redeComplexa
    
    def addlistaRedes(self,rede):
        self.__listaRedes.append(rede)
    
    def QuantidadeRedes(self):
        return print(len(self.__listaRedes))
    
    def criarRedeComplexa(self,):
        for i in self.__listaRedes:
            self.__redeComplexa.add_nodes_from(i.rede.nodes)
            #self.__redeComplexa.add_edges_from(i.rede.edges)
            self.__redeComplexa.add_weighted_edges_from(i.rede.edges.data('weight'))
            
    def mostrarRedeComplexa(self):
        nx.draw_circular(self.__redeComplexa, with_labels=True)
        plt.show()
              
    def MostrarRedesIndividuais(self):
        for i in self.__listaRedes:
            i.MostrarRede()

    def imprimirGraus(self):
        listaGraus = []
        for i in self.__listaRedes:
            listaGraus.append(np.mean([d for n, d in i.rede.degree()]))
        print(listaGraus)
        plt.plot(range(1,len(listaGraus)+1),listaGraus)
        #plt.show()
    
    def imprimirQuantidadeNos(self):
        listaNos = []
        for i in self.__listaRedes:
            listaNos.append(len(i.rede.nodes))
        plt.plot(range(1,len(listaNos)+1),listaNos)
        #plt.show()
    
    def imprimirQuantidadeArestas(self):
        listaArestas = []
        for i in self.__listaRedes:
            listaArestas.append(len(i.rede.edges))
        plt.plot(range(1,len(listaArestas)+1),listaArestas)
        #plt.show()

    def imprimirDensidade(self):
        listaDensidade = []
        for i in self.__listaRedes:
            listaDensidade.append(nx.density(i.rede))
        plt.plot(range(1,len(listaDensidade)+1),listaDensidade)
        #plt.show()

    def imprimirDistribuiçãoGraus(self):
        GrausRedeComplexa = [d for n, d in self.__redeComplexa.degree()]
        print(GrausRedeComplexa)
        plt.hist(GrausRedeComplexa, bins=np.arange(1,max(GrausRedeComplexa),1), density=False, alpha=0.75, color='b', align='left')
        #plt.show()

    def imprimirQuantidadePesos(self):
        listaPesos = []
        for i in self.__listaRedes:
            listaPesos.append(np.sum([w for s,t,w in i.rede.edges.data('weight')]))
        print(listaPesos)
        plt.plot(range(1,len(listaPesos)+1),listaPesos)
        #plt.show()
