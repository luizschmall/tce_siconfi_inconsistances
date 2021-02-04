import pandas
import string
import math
import csv
import os
import re
from unicodedata import normalize
import unicodedata


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

def corrigir_nomes(nome):
    nome = nome.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U').replace('Ç', 'C')
    return nome

def localize_floats(row):
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el
        for el in row
    ]

def converte_float(elemento):
    elemento = float(str(elemento).replace(",","."))
    return elemento

def primeiro_algarismo(txt):
    txt = txt[0]
    return txt

def troca_primeiro_algarismo(txt):
    if txt[0] == "9":
        txt = txt[1:]
        if txt == "":
            txt = "*"
    return txt

def troca_primeiro_algarismo2(txt):
    if txt[0] == "7":
        txt = str(txt).replace("7","1")
    return txt

def tres_caracteres(txt):
    txt = txt[0:3]
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
    df1 = finbra_file[mask.any(axis=1)]
    if df1.empty != True:
        valor = float(df1['Valor'].values[0].replace(",", "."))
        conta = key
    else:
        valor = 0.0
        conta = key
    return valor, conta


def compara_dados(key, key2, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2):
    with open(diretorio + "Finbra_balorc\\" + ano + "_compara_receitas.csv", mode='a+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_ALL)
        try:
            df2_key = df2.loc[key]["VL_ARRECADADO"]
        except:
            df2_key = 0.0
        try:
            df_key = df1.loc[key]["VL_ARRECADADO"]
        except:
            df_key = 0.0
        try:
            finbra = finbra_file.loc[key2]["Valor"]
        except:
            finbra = 0.0

        compara_writer.writerow(localize_floats([cod_ibge, cidade, key2, finbra,
                                             df2_key, df_key,
                                             finbra == df2_key, finbra == df_key]))
    return


def processa_dados_balorc_receitas(df1, df2, cidade, cod_ibge, balorc, diretorio, ano):
        print(cidade)

        key = "1"
        key2 = "RECEITAS CORRENTES"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "11"
        if ano == "2017":
            key2 = "RECEITA TRIBUTARIA"
        else:
            key2 = remover_acentos("IMPOSTOS, TAXAS E CONTRIBUIÇÕES DE MELHORIA".upper())
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "12"
        if ano == "2017":
            key2 = "RECEITA DE CONTRIBUICOES"
        else:
            key2 = "CONTRIBUICOES"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "13"
        key2 = "RECEITA PATRIMONIAL"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "17"
        key2 = "TRANSFERENCIAS CORRENTES"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "19"
        key2 = "Outras Receitas Correntes".upper()
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "2"
        key2 = "RECEITAS DE CAPITAL"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "21"
        key2 = "OPERACOES DE CREDITO"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "22"
        key2 = "ALIENACAO DE BENS"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "24"
        key2 = "TRANSFERENCIAS DE CAPITAL"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        if ano == "2017":
            key = "25"
        else:
            key = "29"
        key2 = "OUTRAS RECEITAS DE CAPITAL"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)




def main():
    diretorio = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_RS\\"
    ano = '2017'
    municipios = pandas.read_csv(diretorio + 'RS_municipios_TCE.csv', sep = ';', encoding='latin1')
    balorc_finbra_receitas = pandas.read_csv(diretorio + 'Finbra_balorc\\' + ano + ' - receitas.csv', sep=';', encoding='latin1')
    balorc_finbra_receitas_intra = pandas.read_csv(diretorio + 'Finbra_balorc\\' + ano + ' - receitas_intra.csv', sep=';', encoding='latin1')
    balorc_finbra_receitas = pandas.concat([balorc_finbra_receitas, balorc_finbra_receitas_intra])
    print(municipios)
    with open(diretorio + "Finbra_balorc\\" + ano + "_compara_receitas.csv", mode='w+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        compara_writer.writerow(["cod_ibge", "cidade", "key", "valor_finbra", "valor_tce", "valor_tce_prefeitura",
                                                                                    "compara", "compara_prefeitura"])

    for index, row in municipios.iterrows():
        diretorio2 = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_RS\\dados - receitas - 2017\\"
        registros = carrega_dados(diretorio2, row['NOME_MUNICIPIO'])

        df1 = registros[registros['NOME_MUNICIPIO'] == row['NOME_MUNICIPIO']]
        df1 = df1[~df1['NOME_ORGAO'].str.contains('INTER', regex=False)]
        df1["CD_CONTA_SG"] = df1["CD_CONTA_SG"].apply(remover_ponto_virgula_zero)
        df1["CD_CONTA_SG"] = df1["CD_CONTA_SG"].apply(troca_primeiro_algarismo)
        df1["CD_CONTA_SG"] = df1["CD_CONTA_SG"].apply(troca_primeiro_algarismo2)

        df2 = df1.groupby(["CD_CONTA_SG"])[["VL_ORCADO","VL_ARRECADADO"]].agg("sum")
        df1 = df1[df1["NOME_ORGAO"].apply(tres_caracteres) == "PM "]
        df1 = df1.groupby(["CD_CONTA_SG"])[["VL_ORCADO","VL_ARRECADADO"]].agg("sum")


        balorc = balorc_finbra_receitas[balorc_finbra_receitas["Cod_IBGE"] == row['CD_MUNICIPIO_IBGE']]
        balorc = balorc[balorc["Coluna"] == 'Até o Bimestre (c)']
        balorc["Valor"] = balorc["Valor"].apply(converte_float)
        balorc["Conta"] = balorc["Conta"].apply(remover_acentos)
        balorc = balorc.groupby(["Conta"])[["Valor"]].agg("sum")
        processa_dados_balorc_receitas(df1, df2, row['NOME_MUNICIPIO'], row['CD_MUNICIPIO_IBGE'], balorc, diretorio, ano)

if __name__ == '__main__':
    main()