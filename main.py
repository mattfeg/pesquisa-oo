from datetime import datetime
from dateutil.relativedelta import relativedelta
from Rede import *
from RedeComplexa import *

# from calcularDistancia import *

RC1 = RedeComplexa("Completa")  # REDE COMPLETA
RC2 = RedeComplexa("Cirurgia")  # REDE CIRURGIAS
RC3 = RedeComplexa("Intercorrência")  # REDE INTERCORRENCIAS
RC4 = RedeComplexa("Internação Domiciliar")  # REDE INTERNACOES DOMICILIARES
RC5 = RedeComplexa("Tratamento Clínico")  # REDE INTERNACOES DOMICILIARES

# ListaRedes = [RC1,RC2,RC3,RC4,RC5]
ListaRedes = [RC1] #TESTAR APENAS COM 1 REDE

for i in ListaRedes:
    data_inicial = datetime(2015, 1, 1)  # DATA EXATA
    data_final = datetime(2022, 12, 31)  # DATA EXATA
    data = data_inicial
    while data <= data_final:
        ano = str(data.year)[2:]
        mes = int(data.month)
        nova_rede = Rede(
            f"./RedesMatrizFiltradas/{i.nome}/MatrizRDCE{ano}{mes:02d}.csv"
        )
        print(f"{i.nome}/{ano}/{mes:02d}")
        nova_rede.CriarRede()
        i.addlistaRedes(nova_rede)
        data += relativedelta(months=1)


for i in ListaRedes:
    i.criarRedeComplexa()

    # Plots
    # i.imprimirGraus()
    # i.imprimirQuantidadeNos()
    # i.imprimirQuantidadeArestas()
    # i.imprimirQuantidadePesos()
    # i.imprimirDensidade()
    # i.imprimirDistribuiçãoGraus()
    #plt.figure()
    #i.imprimirDistanciasPorMes()  # INCOMPLETO
    #plt.show()
    
    i.exportArestasCVS()

# Distancias
# gerarDfDistancias(RC1.redeComplexa)
