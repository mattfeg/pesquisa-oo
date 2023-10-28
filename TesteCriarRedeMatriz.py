from CriarRedeMatriz import *

for ano in range(15, 23):
    for mes in range(1, 13):
        CriarRedeMatriz(f'./DadosSUS/CSV/RDCE{ano}{mes:02d}.csv')
