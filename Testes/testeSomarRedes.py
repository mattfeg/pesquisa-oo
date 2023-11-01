import networkx as nx

# Criar três redes menores de exemplo
G1 = nx.Graph()
G1.add_edge('A', 'B', distancia=4, duracao=2)
G1.add_edge('B', 'C', distancia=3, duracao=1)

G2 = nx.Graph()
G2.add_edge(1, 2, distancia=2, duracao=1)
G2.add_edge(2, 3, distancia=3, duracao=2)

G3 = nx.Graph()
G3.add_edge('X', 'Y', distancia=5, duracao=2)
G3.add_edge('Y', 'Z', distancia=4, duracao=3)

# Combinar as três redes menores em uma rede maior
G = nx.compose_all([G1, G2, G3])

# Verificar se a rede maior foi criada corretamente
print(G.edges(data=True))
