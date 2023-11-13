import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class Rede:
    def __init__(self, path):
        self.__pathCSV = path
        self.__periodo = None
        self.__rede = nx.DiGraph()
        self.__NumNodes = len(self.__rede.nodes)
        self.__NumArestas = len(self.__rede.edges)
        self.__dfdistancia = pd.read_csv("distancias.csv", sep=",", encoding="Latin1")

    @property
    def rede(self):
        return self.__rede

    @property
    def periodo(self):
        return self.__periodo

    @property
    def pathCSV(self):
        return self.__pathCSV

    @property
    def NumNodes(self):
        self.__NumNodes = len(self.__rede.nodes)
        return self.__NumNodes

    @property
    def NumArestas(self):
        self.__NumArestas = len(self.__rede.edges)
        return self.__NumArestas

    def CriarRede(self):
        df = pd.read_csv(self.__pathCSV, sep=",", encoding="Latin1", index_col="CNES")
        for municipio in df.columns:
            for hospital in df.index:
                if df[municipio][hospital] > 0:  # Remover arestas com peso 0
                    for index, row in self.__dfdistancia.iterrows():
                        if (
                            municipio == row["Source"]
                            and hospital == row["Target"]
                            and row["Weight"] > 0
                        ):
                            self.__rede.add_edge(
                                municipio,
                                hospital,
                                weight=df[municipio][hospital],
                                distancia=row["Distancia"],
                                duracao=row["Duracao"],
                            )
        return print("Rede Criada: ", self)

    def MostrarRede(self):
        nx.draw(self.__rede, with_labels=True)
        plt.show()
