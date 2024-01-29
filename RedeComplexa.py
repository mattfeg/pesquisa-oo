import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from configGrafico import *


class RedeComplexa:
    def __init__(self, nome) -> None:
        self.__listaRedes = []
        self.__redeComplexa = nx.DiGraph()
        # self.__redeComplexa = None
        self.nome = nome

    @property
    def listaRedes(self):
        return self.__listaRedes

    @property
    def redeComplexa(self):
        return self.__redeComplexa

    def addlistaRedes(self, rede):
        self.__listaRedes.append(rede)

    def QuantidadeRedes(self):
        return print(len(self.__listaRedes))

    def criarRedeComplexa(self):
        listaRedes = [i.rede for i in self.__listaRedes]
        self.__redeComplexa = nx.compose_all(listaRedes)
        print(listaRedes)
        print("Nos Rede Complexa: ", len(self.__redeComplexa.nodes))
        print("Arestas Rede Complexa: ", len(self.__redeComplexa.edges))

    def mostrarRedeComplexa(self):
        nx.draw_circular(self.__redeComplexa, with_labels=True)
        # plt.show()

    def MostrarRedesIndividuais(self):
        for i in self.__listaRedes:
            i.MostrarRede()

    # Infos do eixo dos Plots (Total)
    anos = np.arange(2015, 2024, 1)  # Ano Inicial +1 / Ano final + 2
    meses = np.arange(1, 97, 1)

    # Para 3 meses
    # anos = np.arange(2015, 2016, 1)
    # meses = np.arange(1, 4, 1)
    
    # # Para 3 meses
    # anos = np.arange(2015, 2020, 1)
    # meses = np.arange(1, 61, 1)

    posicao_dos_anos = [(i - 2016 + 1) * 12 for i in anos]

    def imprimirGraus(self):
        listaGraus = []
        for i in self.__listaRedes:
            listaGraus.append(np.mean([d for n, d in i.rede.degree()]))

        axs[0, 0].set_title(f"Grau Médio por mês da Rede {self.nome}")
        axs[0, 0].plot(RedeComplexa.meses, listaGraus)
        plt.xlabel("Tempo")
        plt.ylabel("Grau Médio")
        plt.xticks(RedeComplexa.posicao_dos_anos, RedeComplexa.anos)
        plt.savefig(f"./Figuras/FigurasRede{self.nome}/Graus{self.nome}.png")
        # plt.show()

    def imprimirQuantidadeNos(self):
        listaNos = []
        for i in self.__listaRedes:
            listaNos.append(len(i.rede.nodes))

        axs[0, 1].set_title(f"Quantidade de Nós por mês da Rede {self.nome}")
        axs[0, 1].plot(RedeComplexa.meses, listaNos)
        plt.xlabel("Tempo")
        plt.ylabel("Quantidade de Nós")
        plt.xticks(RedeComplexa.posicao_dos_anos, RedeComplexa.anos)
        plt.savefig(f"./Figuras/FigurasRede{self.nome}/QntNos{self.nome}.png")
        # plt.show()

    def imprimirQuantidadeArestas(self):
        listaArestas = []
        for i in self.__listaRedes:
            listaArestas.append(len(i.rede.edges))
        axs[0, 2].set_title(f"Quantidade de Arestas por mês da Rede {self.nome}")
        axs[0, 2].plot(RedeComplexa.meses, listaArestas)
        plt.xlabel("Tempo")
        plt.ylabel("Quantidade de Arestas")
        plt.xticks(RedeComplexa.posicao_dos_anos, RedeComplexa.anos)
        plt.savefig(f"./Figuras/FigurasRede{self.nome}/QntArs{self.nome}.png")
        # plt.show()

    def imprimirDensidade(self):
        listaDensidade = []
        for i in self.__listaRedes:
            listaDensidade.append(nx.density(i.rede))
        axs[1, 0].set_title(f"Densidade por mês da Rede {self.nome}")
        axs[1, 0].plot(RedeComplexa.meses, listaDensidade)
        plt.xlabel("Tempo")
        plt.ylabel("Densidade")
        plt.xticks(RedeComplexa.posicao_dos_anos, RedeComplexa.anos)
        plt.savefig(f"./Figuras/FigurasRede{self.nome}/Densidade{self.nome}.png")
        # plt.show()

    def imprimirDistribuiçãoGraus(self):
        GrausRedeComplexa = [d for n, d in self.__redeComplexa.degree()]
        axs[1, 1].set_title(f"Distribuição de Graus por mês da Rede {self.nome}")
        axs[1, 1].hist(
            GrausRedeComplexa,
            bins=np.arange(1, max(GrausRedeComplexa) + 1, 1),
            alpha=0.75,
            color="b",
            align="mid",
        )
        plt.savefig(
            f"./Figuras/FigurasRede{self.nome}/DistribuiçãoGraus{self.nome}.png"
        )
        # plt.show()

    def imprimirQuantidadePesos(self):
        listaPesos = []
        for i in self.__listaRedes:
            listaPesos.append(np.sum([w for s, t, w in i.rede.edges.data("weight")]))
        axs[1, 2].set_title(f"Quantidade internações por mês da Rede {self.nome}")
        axs[1, 2].plot(RedeComplexa.meses, listaPesos)
        plt.xlabel("Tempo")
        plt.ylabel("Quantidade de Internações")
        plt.xticks(RedeComplexa.posicao_dos_anos, RedeComplexa.anos)
        plt.savefig(f"./Figuras/FigurasRede{self.nome}/QntInternações{self.nome}.png")
        # plt.show()

    def imprimirDistanciasPorMes(self):
        listaDistancias = []
        for i in self.__listaRedes:
            listaDistancias.append(
                np.mean([d for s, t, d in i.rede.edges.data("distancia")])
            )
        # plt.title(f"Distância Média por mês da Rede {self.nome}")
        # plt.plot(RedeComplexa.meses, listaDistancias)
        axs[2, 0].set_title(f"Distância Média por mês da Rede {self.nome}")
        axs[2, 0].plot(RedeComplexa.meses, listaDistancias)
        
        plt.xlabel("Tempo")
        plt.ylabel("Distância Média (km)")
        plt.xticks(RedeComplexa.posicao_dos_anos, RedeComplexa.anos)