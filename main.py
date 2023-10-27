from datetime import datetime
from dateutil.relativedelta import relativedelta
from Rede import *
from RedeComplexa import *
# from calcularDistancia import *

RC1 = RedeComplexa("Completa") #REDE COMPLETA
# RC2 = RedeComplexa("Cirurgias") #REDE CIRURGIAS
# RC3 = RedeComplexa("Intercorrências") #REDE INTERCORRENCIAS
# RC4 = RedeComplexa("Internações Domiciliares") #REDE INTERNACOES DOMICILIARES

# data_inicial = datetime(2015, 1, 1)
# data_final = datetime(2022, 12, 31)
# data = data_inicial
# while data <= data_final:
#     ano = str(data.year)[2:]
#     mes = int(data.month)
#     nova_rede = Rede(f'./RedesMatriz/MatrizRDCE{ano}{mes:02d}.csv')
#     nova_rede.CriarRede()
#     RC1.addlistaRedes(nova_rede)
#     data += relativedelta(months=1)

# data_inicial = datetime(2015, 1, 1)
# data_final = datetime(2022, 12, 31)
# data = data_inicial
# while data <= data_final:
#     ano = str(data.year)[2:]
#     mes = int(data.month)
#     nova_rede = Rede(f'./RedesMatriz/MatrizRDCE{ano}{mes:02d}.csv')
#     nova_rede.CriarRede()
#     RC1.addlistaRedes(nova_rede)
#     data += relativedelta(months=1)

# data_inicial = datetime(2015, 1, 1)
# data_final = datetime(2022, 12, 31)
# data = data_inicial
# while data <= data_final:
#     ano = str(data.year)[2:]
#     mes = int(data.month)
#     nova_rede = Rede(f'./RedesMatrizCirurgia/MatrizRDCE{ano}{mes:02d}.csv')
#     nova_rede.CriarRede()
#     RC2.addlistaRedes(nova_rede)
#     data += relativedelta(months=1)

# data_inicial = datetime(2015, 1, 1)
# data_final = datetime(2022, 12, 31)
# data = data_inicial
# while data <= data_final:
#     ano = str(data.year)[2:]
#     mes = int(data.month)
#     nova_rede = Rede(f'./RedesMatrizCirurgia/MatrizRDCE{ano}{mes:02d}.csv')
#     nova_rede.CriarRede()
#     RC4.addlistaRedes(nova_rede)
#     data += relativedelta(months=1)

# data_inicial = datetime(2015, 1, 1)
# data_final = datetime(2022, 12, 31)
# data = data_inicial
# while data <= data_final:
#     ano = str(data.year)[2:]
#     mes = int(data.month)
#     nova_rede = Rede(f'./RedesMatrizIntDom/MatrizRDCE{ano}{mes:02d}.csv')
#     nova_rede.CriarRede()
#     RC4.addlistaRedes(nova_rede)
#     data += relativedelta(months=1)


# ListaRedes = [RC1,RC2,RC3,RC4]
ListaRedes = [RC1]


for i in ListaRedes:
    data_inicial = datetime(2015, 1, 1)
    data_final = datetime(2022, 12, 31)
    data = data_inicial
    while data <= data_final:
        ano = str(data.year)[2:]
        mes = int(data.month)
        nova_rede = Rede(f'./RedesMatriz{i.nome}/MatrizRDCE{ano}{mes:02d}.csv')
        nova_rede.CriarRede()
        i.addlistaRedes(nova_rede)
        data += relativedelta(months=1)

for i in ListaRedes:
    i.criarRedeComplexa()
    i.imprimirGraus()
    i.imprimirQuantidadeNos()
    i.imprimirQuantidadeArestas()
    i.imprimirQuantidadePesos()
    i.imprimirDensidade()
    i.imprimirDistribuiçãoGraus()
    i.imprimirQuantidadePesos()

# RC1.criarRedeComplexa()
# #RC1.mostrarRedeComplexa()
# RC1.imprimirGraus()
# RC1.imprimirQuantidadeNos()
# RC1.imprimirQuantidadeArestas()
# RC1.imprimirQuantidadePesos()
# RC1.imprimirDensidade()
# RC1.imprimirDistribuiçãoGraus()

#plt.title("Quantidade de Nós versus Quantidade Internações")
#plt.legend(['Nos','Internações'])
#plt.show()

#Distancias
#gerarDfDistancias(RC1.redeComplexa)