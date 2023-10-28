import pandas as pd
def CriarRedeMatriz(caminho_csv): # Informar o caminho no seguinte formato './DadosSUS/CSV/xxxx.csv'
    df = pd.read_csv(caminho_csv, sep=',', encoding='Latin1')
    
    filtroCirurgia = [416110010, 416110011, 416110012, 416110013, 416110014, 416110015, 416110016, 416110017, 416110018, 416110020, 416110021, 416110022, 416110023, 416110024, 416110025, 416110026, 416110027, 416110028, 416110030, 416110031, 416110032, 416110033, 416110034, 416110035, 416110036, 416110037, 416110038, 416110040, 416110041, 416110042, 416110043, 416110044, 416110045, 416110046, 416110047, 416110048, 416110050, 416110051, 416110052, 416110053, 416110054, 416110055, 416110056, 416110057, 416110058, 416110060, 416110061, 416110062, 416110063, 416110064, 416110065, 416110066, 416110067, 416110068, 416110070, 416110071, 416110072, 416110073, 416110074, 416110075, 416110076, 416110077, 416110078, 416110080, 416110081, 416110082, 416110083, 416110084, 416110085, 416110086, 416110087, 416110088]
    filtroInternacaoDomiciliar = [301050074]
    filtroTratamentoClinico = [304100021, 303130067]
    filtroIntercorrencia = [301060070, 301060088, 304100013]
    filtroTotal = filtroTratamentoClinico + filtroIntercorrencia + filtroCirurgia + filtroInternacaoDomiciliar
    
    dfgeral = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])] #FILTRO GERAL
    #dftotal = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])&(df['PROC_REA'].isin(filtroTotal))] #FILTRO TOTAL
    dfInternaçaoDomiciliar = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])&(df['PROC_REA'].isin(filtroInternacaoDomiciliar))] #FILTRO INTERNAÇÃO DOMICILIAR
    dfTratamentoClinico = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])&(df['PROC_REA'].isin(filtroTratamentoClinico))] #FILTRO TRATAMENTO CLINICO
    dfIntercorrencia = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])&(df['PROC_REA'].isin(filtroIntercorrencia))] #FILTRO INTERCORRENCIA
    dfCirurgia = df[df['DIAG_PRINC'].isin(['C340', 'C341', 'C342', 'C343', 'C348', 'C349'])&(
                    (df['PROC_REA'].isin(filtroCirurgia))|
                    (df['PROC_REA'].astype(str).str.startswith(('41201','41202','41203','41204','41205'))))] #FILTRO CIRURGIA

    dictDfs = {'Completa':dfgeral, 'Internação Domiciliar':dfInternaçaoDomiciliar, 'Tratamento Clínico':dfTratamentoClinico, 'Intercorrência':dfIntercorrencia, 'Cirurgia':dfCirurgia}


    dfcnes = pd.read_csv('./DadosSUS/CNESBR.csv', sep=',', encoding='Latin1')
    dfmunics = pd.read_csv('./DadosSUS/MUNICSBR.csv', sep=',')
    
    for nome, dataf in dictDfs.items():
        dataf['CNES'] = dataf['CNES'].map(dfcnes.set_index('CNES')['NOMEFANT'])
        dataf['MUNIC_RES'] = dataf['MUNIC_RES'].map(dfmunics.set_index('COD')['MUNIC'])
        tabela_cruzada = pd.crosstab(dataf['CNES'] , dataf['MUNIC_RES'])
        tabela_cruzada.to_csv(f"./RedesMatrizFiltradas/{nome}/Matriz{caminho_csv.split('/')[-1].split('.')[0]}.csv", index=True, header=True)
    

    # df['CNES'] = df['CNES'].map(dfcnes.set_index('CNES')['NOMEFANT'])
    # df['MUNIC_RES'] = df['MUNIC_RES'].map(dfmunics.set_index('COD')['MUNIC'])
    # tabela_cruzada = pd.crosstab(df['CNES'] , df['MUNIC_RES'])
    # tabela_cruzada.to_csv(f"./RedesMatrizFiltradas/Matriz{caminho_csv.split('/')[-1].split('.')[0]}.csv", index=True, header=True)
    
