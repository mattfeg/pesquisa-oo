import pandas as pd
import matplotlib.pyplot as plt

# def criarTabela(df

df = pd.read_csv('RDCE2015-2022.csv')
dfcnes = pd.read_csv('./DadosSUS/CNESBR.csv', sep=',', encoding='Latin1')
dfmunics = pd.read_csv('./DadosSUS/MUNICSBR.csv', sep=',')



df = df[['ANO_CMPT','MES_CMPT','MUNIC_RES','CNES','PROC_REA','SEXO','IDADE']]
#print(df.value_counts('IDADE'))
# idade = df.value_counts('IDADE')
count_idades_homem = [0,0,0,0,0]
count_idades_mulher = [0,0,0,0,0]
count_idades = [0,0,0,0,0]

for s,i in df[['SEXO','IDADE']].values:
    if i in range(0,50):
        count_idades[0] += 1
    if i in range(50,60):
        count_idades[1] += 1
    if i in range(60,70):
        count_idades[2] += 1
    if i in range(70,80):
        count_idades[3] += 1
    if i in range(80,120):
        count_idades[4] += 1
    if s == 1:
        if i in range(0,50):
            count_idades_homem[0] += 1
        if i in range(50,60):
            count_idades_homem[1] += 1
        if i in range(60,70):
            count_idades_homem[2] += 1
        if i in range(70,80):
            count_idades_homem[3] += 1
        if i in range(80,120):
            count_idades_homem[4] += 1
    if s == 3:
        if i in range(0,50):
            count_idades_mulher[0] += 1
        if i in range(50,60):
            count_idades_mulher[1] += 1
        if i in range(60,70):
            count_idades_mulher[2] += 1
        if i in range(70,80):
            count_idades_mulher[3] += 1
        if i in range(80,120):
            count_idades_mulher[4] += 1


print(count_idades_homem)
print(count_idades_mulher)
print('')
prcnt_homens = '{:.2f}'.format((sum(count_idades_homem)/(sum(count_idades_mulher)+sum(count_idades_homem)))*100)
prcnt_mulheres = '{:.2f}'.format((sum(count_idades_mulher)/(sum(count_idades_mulher)+sum(count_idades_homem)))*100)

print(prcnt_mulheres)
print(prcnt_homens)

#bins = ['0-49', '50-59', '60-69', '70-79', '80-120']

# bar_width = 0.35
# r1 = range(len(bins))
# r2 = [x + bar_width for x in r1]

# plt.bar_label(plt.bar(r1, count_idades_homem, width=bar_width, label='Homem'))
# plt.bar_label(plt.bar(r2, count_idades_mulher, width=bar_width, label='Mulher'))

# plt.xlabel('Idade')
# plt.ylabel('Quantidade')
# plt.title('Idade dos pacientes da Rede Completa')
# plt.xticks([r + bar_width / 2 for r in range(len(bins))], bins)
# plt.legend()
# plt.show()
# Converter os valores para float
count_idades_homem = [float(x) for x in count_idades_homem]
count_idades_mulher = [float(x) for x in count_idades_mulher]
count_idades = [float(x) for x in count_idades]

prcnt_homens = float(prcnt_homens)
prcnt_mulheres = float(prcnt_mulheres)
prcnt_049 = '{:.2f}'.format(float(count_idades[0]/sum(count_idades)*100))
prcnt_5059 = '{:.2f}'.format(float(count_idades[1]/sum(count_idades)*100))
prcnt_6069 = '{:.2f}'.format(float(count_idades[2]/sum(count_idades)*100))
prcnt_7079 = '{:.2f}'.format(float(count_idades[3]/sum(count_idades)*100))
prcnt_80120 = '{:.2f}'.format(float(count_idades[4]/sum(count_idades)*100))

# Criar o DataFrame
dfTabela = pd.DataFrame(columns=['Caracteristicas', 'Quantidade', 'Porcentagem', 'IC 95%'])

# Adicionar os valores nas linhas
dfTabela.loc[1] = ['Sexo', '', '', '']
dfTabela.loc[2] = ['Masculino', int(sum(count_idades_homem)), str(prcnt_homens)+"%", '']
dfTabela.loc[3] = ['Feminino', int(sum(count_idades_mulher)), str(prcnt_mulheres)+"%", '']
dfTabela.loc[4] = ['Idade', '', '', '']
dfTabela.loc[5] = ['49 ou menos', int(count_idades[0]), str(prcnt_049)+"%", '']
dfTabela.loc[6] = ['50-59', int(count_idades[1]), str(prcnt_5059)+"%", '']
dfTabela.loc[7] = ['60-69', int(count_idades[2]), str(prcnt_6069)+"%", '']
dfTabela.loc[8] = ['70-79', int(count_idades[3]), str(prcnt_7079)+"%", '']
dfTabela.loc[9] = ['80 ou mais', int(count_idades[4]), str(prcnt_80120)+"%", '']

print(dfTabela.to_string(index=False))
from tabulate import tabulate
# Formatar DataFrame como uma tabela
tabela_formatada = tabulate(dfTabela, headers='keys', tablefmt='pretty')

# Mostrar a tabela formatada
print(tabela_formatada)
