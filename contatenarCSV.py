import pandas as pd

#Concaternar csvs
listaDfs = []
for ano in range(15, 23):
    for mes in range(1, 13):
        listaDfs.append(pd.read_csv(f'./DadosSUS/CSV/RDCE{ano}{mes:02d}.csv'))
        print(f'./DadosSUS/CSV/RDCE{ano}{mes:02d}.csv')

df = pd.concat(listaDfs, ignore_index=True)
df = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])]
df.to_csv('./RDCE2015-2022.csv', index=False)