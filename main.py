from datetime import datetime
from dateutil.relativedelta import relativedelta
from Rede import *
from RedeComplexa import *
from calcularDistancia import *

RC1 = RedeComplexa() #REDE COMPLETA

data_inicial = datetime(2015, 1, 1)
data_final = datetime(2022, 12, 31)
data = data_inicial
while data <= data_final:
    ano = str(data.year)[2:]
    mes = int(data.month)
    nova_rede = Rede(f'./RedesMatriz/MatrizRDCE{ano}{mes:02d}.csv')
    #print("Path da Rede: ",nova_rede.pathCSV)
    nova_rede.CriarRede()
    RC1.addlistaRedes(nova_rede)
    data += relativedelta(months=1)
    #nova_rede.MostrarRede()

print("----------------------------------------")   
RC1.criarRedeComplexa()
#RC1.mostrarRedeComplexa()
#RC1.imprimirGraus()
RC1.imprimirQuantidadeNos()
#RC1.imprimirQuantidadeArestas()
RC1.imprimirQuantidadePesos()
#RC1.imprimirDensidade()
#RC1.imprimirDistribuiçãoGraus()
plt.title("Quantidade de Nós versus Quantidade Internações")
plt.legend(['Nos','Internações'])
plt.show()

#Distancias
#gerarDfDistancias(RC1.redeComplexa)