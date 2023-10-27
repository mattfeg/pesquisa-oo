import pandas as pd
def CriarRedeMatriz(caminho_csv): # Informar o caminho no seguinte formato './DadosSUS/CSV/xxxx.csv'
    df = pd.read_csv(caminho_csv, sep=',', encoding='Latin1')
    
    filtroCirurgia =  ['41611010', '41611011', '41611012', '41611013', '41611014', '41611015', '41611016', '41611017', '41611018', '41611020', '41611021', '41611022', '41611023', '41611024', '41611025', '41611026', '41611027', '41611028', '41611030', '41611031', '41611032', '41611033', '41611034', '41611035', '41611036', '41611037', '41611038', '41611040', '41611041', '41611042', '41611043', '41611044', '41611045', '41611046', '41611047', '41611048', '41611050', '41611051', '41611052', '41611053', '41611054', '41611055', '41611056', '41611057', '41611058', '41611060', '41611061', '41611062', '41611063', '41611064', '41611065', '41611066', '41611067', '41611068', '41611070', '41611071', '41611072', '41611073', '41611074', '41611075', '41611076', '41611077', '41611078', '41611080', '41611081', '41611082', '41611083', '41611084', '41611085', '41611086', '41611087', '41611088']
    filtroInternacaoDomiciliar = ['301050074']
    filtroTratamentoClinico = ['304100021','303130067']
    filtroIntercorrencia = ['301060070','301060088','304100013']
    filtroTotal = filtroTratamentoClinico+filtroIntercorrencia + filtroCirurgia + filtroInternacaoDomiciliar
    
    
    # df = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])] #FILTRO GERAL
    # df = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])&(df['PROC_REA'].isin(filtroTotal))] #FILTRO Total
    # df = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])&(df['PROC_REA'].isin(filtroInternacaoDomiciliar))] #FILTRO INTERNAÇÃO DOMICILIAR
    # df = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])&(df['PROC_REA'].isin(filtroTratamentoClinico))] #FILTRO TRATAMENTO CLINICO
    # df = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])&(df['PROC_REA'].isin(filtroIntercorrencia))] #FILTRO INTERCORRENCIA
    df = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349']) & (df['PROC_REA'].isin(filtroCirurgia))] #FILTRO CIRURGIA
    
    

    dfcnes = pd.read_csv('./DadosSUS/CNESBR.csv', sep=',', encoding='Latin1')
    dfmunics = pd.read_csv('./DadosSUS/MUNICSBR.csv', sep=',')
    
    df['CNES'] = df['CNES'].map(dfcnes.set_index('CNES')['NOMEFANT'])
    df['MUNIC_RES'] = df['MUNIC_RES'].map(dfmunics.set_index('COD')['MUNIC'])

    tabela_cruzada = pd.crosstab(df['CNES'] , df['MUNIC_RES'])
    #tabela_cruzada.to_csv(f"./RedesMatriz/Matriz{caminho_csv.split('/')[-1].split('.')[0]}.csv", index=True, header=True)
    tabela_cruzada.to_csv(f"./RedesMatrizFiltradas/Matriz{caminho_csv.split('/')[-1].split('.')[0]}.csv", index=True, header=True)
    
