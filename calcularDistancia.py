import googlemaps
import networkx as nx
import pandas as pd
from apiKey import api_key

gmaps = googlemaps.Client(key=api_key)

def buscarDistância(aresta):
    origem = aresta[0]
    destino = aresta[1]
    matrix = gmaps.distance_matrix(origem, destino)["rows"][0]["elements"][0]

    # Verifique se a solicitação foi bem-sucedida
    if matrix["status"] == "OK":
        distancia = matrix["distance"]["text"]
        duracao = matrix["duration"]["text"]
        print(f"A distância entre {origem} e {destino} é de {distancia}.")
        print(f"A duração estimada da viagem é de {duracao}.\n")
        return distancia,duracao
        
    else:
        print("Não foi possível calcular a distância.")
        return None,None

#Plotar Arestas e suas propriedades
def gerarDfDistancias(rede):
    dfarestas = pd.DataFrame(columns=['Source', 'Target', 'Weight','Distancia','Duracao'])
    for aresta in rede.edges():
        distancia,duracao = buscarDistância([aresta[0], aresta[1]])
        if distancia is not None and duracao is not None:
            dfarestas = pd.concat([dfarestas, pd.DataFrame({'Source': aresta[0], 'Target': aresta[1], 'Weight': rede[aresta[0]][aresta[1]]['weight'],'Distancia':distancia,'Duracao':duracao}, index=[0])], ignore_index=True)
    print(dfarestas)
    dfarestas.to_csv('distancias.csv', index=False, encoding='utf-8')