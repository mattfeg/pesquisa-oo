import networkx as nx
import pandas as pd
from Funções.calcularDistancia import *

df = pd.read_csv("./RedesMatrizCirurgia/MatrizRDCE1501.csv", sep=',', encoding='Latin1',index_col='CNES')
rede = nx.DiGraph()
for municipio in df.columns:
    for hospital in df.index:
            if df[municipio][hospital] > 0:
                rede.add_edge(municipio, hospital, weight=df[municipio][hospital])

gerarDfDistancias(rede)