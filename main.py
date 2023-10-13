from datetime import datetime
from dateutil.relativedelta import relativedelta
from Rede import *
from RedeComplexa import *

RC1 = RedeComplexa()

data_inicial = datetime(2015, 1, 1)
data_final = datetime(2015, 4, 30)

data = data_inicial
while data <= data_final:
    ano = str(data.year)[2:]
    mes = int(data.month)
    nova_rede = Rede(f'./CSV/MatrizRDCE{ano}{mes:02d}.csv')
    print("Path da Rede: ",nova_rede.pathCSV)
    nova_rede.CriarRede()
    
    RC1.addlistaRedes(nova_rede)
    data += relativedelta(months=1)
print("----------------------------------------")   
RC1.criarRedeComplexa()
RC1.mostrarRedeComplexa()