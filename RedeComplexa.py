import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class RedeComplexa:
    def __init__(self,nome) -> None:
        self.__listaRedes = []
        self.__redeComplexa = nx.DiGraph()
        self.nome = nome
    
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

        # Gera os rótulos do eixo X com anos correspondentes
        anos = np.arange(2016, 2024, 1)
        meses = np.arange(1, 97, 1)
        posicao_dos_anos = [(i - 2016 + 1) * 12 for i in anos]  # Posições onde os anos começam

        plt.title(f"Grau Médio por mês da Rede {self.nome}")
        plt.plot(meses, listaGraus)

        plt.xlabel('Tempo')
        plt.ylabel('Grau Médio')

        plt.xticks(posicao_dos_anos, anos)  # Define os rótulos e as posições dos anos no eixo X
        plt.savefig(f'./Figuras/FigurasRede{self.nome}/Graus{self.nome}.png')
        plt.show()
    
    def imprimirQuantidadeNos(self):
        listaNos = []
        for i in self.__listaRedes:
            listaNos.append(len(i.rede.nodes))
        plt.title(f"Quantidade de Nós por mês da Rede {self.nome}")
        plt.plot(range(1,len(listaNos)+1),listaNos)
        plt.savefig(f'./Figuras/FigurasRede{self.nome}/QntNos{self.nome}.png')
        plt.show()
    
    def imprimirQuantidadeArestas(self):
        listaArestas = []
        for i in self.__listaRedes:
            listaArestas.append(len(i.rede.edges))
        plt.title(f"Quantidade de Arestas por mês da Rede {self.nome}")
        plt.plot(range(1,len(listaArestas)+1),listaArestas)
        plt.savefig(f'./Figuras/FigurasRede{self.nome}/QntArs{self.nome}.png')
        plt.show()

    def imprimirDensidade(self):
        listaDensidade = []
        for i in self.__listaRedes:
            listaDensidade.append(nx.density(i.rede))
        plt.title(f"Densidade por mês da Rede {self.nome}")
        plt.plot(range(1,len(listaDensidade)+1),listaDensidade)
        plt.savefig(f'./Figuras/FigurasRede{self.nome}/Densidade{self.nome}.png')
        plt.show()

    def imprimirDistribuiçãoGraus(self):
        GrausRedeComplexa = [d for n, d in self.__redeComplexa.degree()]
        print(GrausRedeComplexa)
        plt.title(f"Distribuição de Graus por mês da Rede {self.nome}")
        plt.hist(GrausRedeComplexa, bins=np.arange(1,max(GrausRedeComplexa),1), density=False, alpha=0.75, color='b', align='left')
        plt.savefig(f'./Figuras/FigurasRede{self.nome}/DistribuiçãoGraus{self.nome}.png')
        plt.show()

    def imprimirQuantidadePesos(self):
        listaPesos = []
        for i in self.__listaRedes:
            listaPesos.append(np.sum([w for s,t,w in i.rede.edges.data('weight')]))
        plt.title(f"Quantidade internações por mês da Rede {self.nome}")
        plt.plot(range(1,len(listaPesos)+1),listaPesos)
        plt.savefig(f'./Figuras/FigurasRede{self.nome}/QntInternações{self.nome}.png')
        plt.show()
    
        
        
