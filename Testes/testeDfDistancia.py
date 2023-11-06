import os
import sys
import pandas as pd

# Adicione o caminho da pasta superior ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Agora você pode importar o arquivo da pasta superior
df = pd.read_csv(
    "./RedesMatrizFiltradas/Completa/MatrizRDCE1501.csv",
    sep=",",
    encoding="Latin1",
    index_col="CNES",
)
dfdistancias = pd.read_csv("distancias.csv", sep=",", encoding="Latin1")
print(dfdistancias)

for municipio in df.columns:
    for hospital in df.index:
        if df[municipio][hospital] > 0:  # Remover arestas com peso 0
            for index, row in dfdistancias.iterrows():
                if (
                    municipio == row["Source"]
                    and hospital == row["Target"]
                    and row["Weight"] > 0
                ):
                    print("Source: ", row["Source"])
                    print("Target: ", row["Target"])
                    print("Distancia: ", row["Distancia"])
                    print("Duracao: ", row["Duracao"])
                    print("\n")
