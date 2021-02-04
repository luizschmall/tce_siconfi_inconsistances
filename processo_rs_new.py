import pandas
import string
import math
import csv
import os
import re
from unicodedata import normalize
import unicodedata


def corrigir_nomes(nome):
    nome = nome.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U').replace('Ç', 'C')
    return nome

def localize_floats(row):
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el
        for el in row
    ]

def primeiro_algarismo(txt):
    txt = txt[0]
    return txt

def remover_ponto_virgula_zero(txt):
    txt = str(txt).replace(",", "")
    txt = str(txt).replace(".", "")
    txt = str(txt).replace(" ", "")
    txt = str(txt).split("e")
    try:
        txt = txt[0]
    except:
        txt = txt
    #txt = str(txt).rsplit("0")
    while str(txt).endswith("0"):
        txt = txt[:-1]
    return txt

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('utf-8')

def remover_acentos_lista(txt):
    return [
        normalize('NFKD', el).encode('ASCII', 'ignore').decode('ASCII') for el in txt
    ]

def carrega_dados(diretorio, cidade):
    files = os.listdir(diretorio)
    files = sorted(files)
    primeiro = True
    print(cidade)
    for file in files:
        if file.split("_")[0] == cidade:
            print("entrei ->", file)
            df = pandas.read_csv(diretorio + file, sep = ',', encoding='utf-8')
            df2 = df.loc[df['NOME_MUNICIPIO'] == cidade]
            if primeiro:
                df1 = df2
                primeiro = False
            else:
                df1 = pandas.concat([df1,df2],ignore_index=True)
    return df1

def extrai_finbra(key, finbra_file):
    mask = finbra_file.applymap(lambda x: key in remover_acentos(str(x).upper()))
    # print(mask)
    df1 = finbra_file[mask.any(axis=1)]
    if df1.empty != True:
        valor = float(df1['Valor'].values[0].replace(",", "."))
#        conta = df1['Conta'].values[0]
        conta = key
    else:
        valor = 0.0
        conta = key
    return valor, conta

def compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2):
    with open(diretorio + "Finbra_balpat\\" + ano + "_compara2.csv", mode='a+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_ALL)
        key2 = remover_ponto_virgula_zero(key)
        finbra, conta = extrai_finbra(key, finbra_file)
        data_empty = False
        try:
            df2_key = df2.loc[cidade,key2]
            df_key = df1[df1["NOME_MUNICIPIO"] == cidade]
            df_key = df_key[df_key["CD_CONTA_SG"] == key2]
            df_key = df_key.iloc[0]
            if df2_key.empty == True:
                data_empty = True
        except:
            data_empty = True

        if data_empty == False:
            compara_writer.writerow(localize_floats([cod_ibge, cidade, conta, finbra,
                                                 df2_key['VL_SALDO_ATUAL_DEV'], df_key['VL_SALDO_ATUAL_DEV'],
                                                 finbra == df2_key['VL_SALDO_ATUAL_DEV'], finbra == df_key['VL_SALDO_ATUAL_DEV']]))
        else:
            compara_writer.writerow(localize_floats([cod_ibge, cidade, conta, finbra,0.0, 0.0,
                                                 finbra == 0.0, finbra == 0.0]))
    return

def compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2):
    with open(diretorio + "Finbra_balpat\\" + ano + "_compara2.csv", mode='a+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_ALL)
        key2 = remover_ponto_virgula_zero(key)
        finbra, conta = extrai_finbra(key, finbra_file)
        data_empty = False
        try:
            df2_key = df2.loc[cidade,key2]
            df_key = df1[df1["NOME_MUNICIPIO"] == cidade]
            df_key = df_key[df_key["CD_CONTA_SG"] == key2]
            df_key = df_key.iloc[0]
            if df2_key.empty == True:
                data_empty = True
        except:
            data_empty = True

        if data_empty == False:
            compara_writer.writerow(localize_floats([cod_ibge, cidade, conta, finbra,
                                                 df2_key['VL_SALDO_ATUAL_CRE'],df_key['VL_SALDO_ATUAL_CRE'],
                                                 finbra == df2_key['VL_SALDO_ATUAL_CRE'],finbra == df_key['VL_SALDO_ATUAL_CRE']]))
        else:
            compara_writer.writerow(localize_floats([cod_ibge, cidade, conta, finbra,0.0,0.0,
                                                 finbra == 0.0,finbra == 0.0]))

    return

def compara_dados_pl(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2):
    with open(diretorio + "Finbra_balpat\\" + ano + "_compara2.csv", mode='a+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_ALL)
        key2 = remover_ponto_virgula_zero(key)
        finbra, conta = extrai_finbra(key, finbra_file)
        data_empty = False
        data3_empty = False
        data4_empty = False
        try:
            df2_key = df2.loc[cidade,key2]
            df_key = df1[df1["NOME_MUNICIPIO"] == cidade]
            df_key = df_key[df_key["CD_CONTA_SG"] == key2]
            df_key = df_key.iloc[0]
            if df2_key.empty == True:
                data_empty = True
        except:
            data_empty = True
        try:
            df2_key3 = df2.loc[cidade,"3"]
            df_key3 = df1[df1["NOME_MUNICIPIO"] == cidade]
            df_key3 = df_key3[df_key3["CD_CONTA_SG"] == "3"]
            df_key3 = df_key3.iloc[0]
        except:
            data3_empty = True
        try:
            df2_key4 = df2.loc[cidade,"4"]
            df_key4 = df1[df1["NOME_MUNICIPIO"] == cidade]
            df_key4 = df_key4[df_key4["CD_CONTA_SG"] == "4"]
            df_key4 = df_key4.iloc[0]
        except:
            data4_empty = True

        if data_empty == False:
            compara_writer.writerow(localize_floats([cod_ibge, cidade, conta, finbra,
                                                 df2_key['VL_SALDO_ATUAL_CRE'] - df2_key3['VL_SALDO_ATUAL_DEV'] +
                                                     df2_key4['VL_SALDO_ATUAL_CRE'],
                                                 df_key['VL_SALDO_ATUAL_CRE'] - df_key3['VL_SALDO_ATUAL_DEV'] +
                                                     df_key4['VL_SALDO_ATUAL_CRE'],
                                                 finbra == df2_key['VL_SALDO_ATUAL_CRE'] - df2_key3['VL_SALDO_ATUAL_DEV'] +
                                                     df2_key4['VL_SALDO_ATUAL_CRE'],
                                                     finbra == df_key['VL_SALDO_ATUAL_CRE'] - df_key3[
                                                         'VL_SALDO_ATUAL_DEV'] +
                                                     df_key4['VL_SALDO_ATUAL_CRE']]))
        else:
            compara_writer.writerow(localize_floats([cod_ibge, cidade, conta, finbra,0.0,0.0,
                                                 finbra == 0.0,finbra == 0.0]))

    return

def processa_dados_balpat(df1, df2, cidade, cod_ibge, balpat_finbra, diretorio, ano):
        print(cidade)
        finbra_file = balpat_finbra.loc[balpat_finbra['Cod_IBGE'] == cod_ibge]

        key = "1.0.0.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.1.0.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.1.1.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.1.2.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.1.4.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.1.5.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.1.9.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.1.3.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.2.0.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.2.3.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.2.2.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.2.4.0.0.00.00"
        compara_dados_ativo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.1.0.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.1.1.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.1.2.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.1.3.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.1.4.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.1.5.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.1.7.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.1.8.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.2.0.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.2.1.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.2.2.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.2.3.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.2.4.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.2.7.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.2.8.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.2.9.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.3.0.0.0.00.00"
        compara_dados_pl(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.3.1.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.2.8.4.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.3.4.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.3.5.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.3.6.0.0.00.00"
        compara_dados_passivo(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.3.7.0.0.00.00"
        compara_dados_pl(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "2.0.0.0.0.00.00"
        compara_dados_pl(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2)



def main():
    diretorio = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_RS\\"
    ano = '2018'
    municipios = pandas.read_csv(diretorio + 'RS_municipios_TCE.csv', sep = ';', encoding='latin1')
    balpat_finbra = pandas.read_csv(diretorio + 'Finbra_balpat\\' + ano + '_balpat.csv' , sep = ';', encoding='latin1')
    print(municipios)
    with open(diretorio + "Finbra_balpat\\" + ano + "_compara2.csv", mode='w+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        compara_writer.writerow(["cod_ibge", "cidade", "key", "valor_finbra", "valor_tce", "valor_tce_prefeitura",
                                                                                    "compara", "compara_prefeitura"])

    for index, row in municipios.iterrows():
        diretorio2 = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_RS\\dados 2 - 2018\\"
        #diretorio2 = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_RS\\teste\\"
        registros = carrega_dados(diretorio2, row['NOME_MUNICIPIO'])
        #registros = carrega_dados(diretorio2, "SANTANA DO LIVRAMENTO")
        registros['DS_CONTA_SG'] = registros['DS_CONTA_SG'].apply(remover_acentos)
        registros['CD_CONTA_SG'] = registros['CD_CONTA_SG'].apply(remover_ponto_virgula_zero)
        df1 = registros[registros['NOME_MUNICIPIO'] == row['NOME_MUNICIPIO']]

        df1 = df1[~df1['NOME_ORGAO'].str.contains('INTER', regex=False)]

        #df1 = registros[registros['NOME_MUNICIPIO'] == "SANTANA DO LIVRAMENTO"]
        df1.loc[df1["CD_CONTA_SG"].apply(primeiro_algarismo) == "1","VL_SALDO_ATUAL_DEV"] = df1["VL_SALDO_ATUAL_DEV"]  - df1["VL_SALDO_ATUAL_CRE"]
        df1.loc[df1["CD_CONTA_SG"].apply(primeiro_algarismo) == "2","VL_SALDO_ATUAL_CRE"] = df1["VL_SALDO_ATUAL_CRE"]  - df1["VL_SALDO_ATUAL_DEV"]
        df2 = df1.groupby(["NOME_MUNICIPIO", "CD_CONTA_SG"])[["VL_SALDO_ANTERIOR_DEV","VL_SALDO_ANTERIOR_CRE",
                                                                         "VL_MOV_DEBITO", "VL_MOV_CREDITO", "VL_SALDO_ATUAL_DEV",
                                                                         "VL_SALDO_ATUAL_CRE"]].agg("sum")
        processa_dados_balpat(df1, df2, row['NOME_MUNICIPIO'], row['CD_MUNICIPIO_IBGE'], balpat_finbra, diretorio, ano)
        #processa_dados_balpat(df1, "SANTANA DO LIVRAMENTO", 0, balpat_finbra, diretorio, ano)

if __name__ == '__main__':
    main()