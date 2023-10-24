from datetime import datetime
from dateutil.relativedelta import relativedelta
from Rede import *

RC1 = RedeComplexa() #CIRURGIA

data_inicial = datetime(2015, 1, 1)
data_final = datetime(2022, 12, 31)
data = data_inicial
while data <= data_final:
    ano = str(data.year)[2:]
    mes = int(data.month)
    nova_rede = Rede(f'./RedesMatrizCirurgia/MatrizRDCE{ano}{mes:02d}.csv')
    #print("Path da Rede: ",nova_rede.pathCSV)
    nova_rede.CriarRede()
    RC1.addlistaRedes(nova_rede)
    data += relativedelta(months=1)
    #nova_rede.MostrarRede()

data_inicial = datetime(2015, 1, 1)
data_final = datetime(2022, 12, 31)
data = data_inicial
RC2 = RedeComplexa() #TRATAMENTO CLINICO
while data <= data_final:
    ano = str(data.year)[2:]
    mes = int(data.month)
    nova_rede = Rede(f'./RedesMatrizTratClin/MatrizRDCE{ano}{mes:02d}.csv')
    #print("Path da Rede: ",nova_rede.pathCSV)
    nova_rede.CriarRede()
    RC2.addlistaRedes(nova_rede)
    data += relativedelta(months=1)
    #nova_rede.MostrarRede()

data_inicial = datetime(2015, 1, 1)
data_final = datetime(2022, 12, 31)
data = data_inicial
RC3 = RedeComplexa() #INCORRENCIA
while data <= data_final:
    ano = str(data.year)[2:]
    mes = int(data.month)
    nova_rede = Rede(f'./RedesMatrizIntercor/MatrizRDCE{ano}{mes:02d}.csv')
    #print("Path da Rede: ",nova_rede.pathCSV)
    nova_rede.CriarRede()
    RC3.addlistaRedes(nova_rede)
    data += relativedelta(months=1)
    #nova_rede.MostrarRede()

data_inicial = datetime(2015, 1, 1)
data_final = datetime(2022, 12, 31)
data = data_inicial
RC4 = RedeComplexa() #INTERNAÇÃO DOMICILIAR
while data <= data_final:
    ano = str(data.year)[2:]
    mes = int(data.month)
    nova_rede = Rede(f'./RedesMatrizIntDom/MatrizRDCE{ano}{mes:02d}.csv')
    #print("Path da Rede: ",nova_rede.pathCSV)
    nova_rede.CriarRede()
    RC4.addlistaRedes(nova_rede)
    data += relativedelta(months=1)
    #nova_rede.MostrarRede()


print("----------------------------------------")   
RC1.criarRedeComplexa()
#RC1.mostrarRedeComplexa()
RC1.imprimirGraus()
#RC1.imprimirQuantidadeNos()
#RC1.imprimirQuantidadeArestas()
#RC1.imprimirDensidade()
#RC1.imprimirDistribuiçãoGraus()
RC2.imprimirGraus()
RC3.imprimirGraus()
RC4.imprimirGraus()
plt.legend(['Cirurgia', 'Tratamento Clinico', 'Intercorrência', 'Internação Domiciliar'])
plt.title('Média de Grau por mês')
plt.show()