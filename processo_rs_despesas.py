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

def converte_float(elemento):
    elemento = float(str(elemento).replace(",","."))
    return elemento

def primeiro_algarismo(txt):
    txt = txt[0]
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

def compara_dados_totais(key, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2):
    with open(diretorio + "Finbra_balorc\\" + ano + "_compara_despesas.csv", mode='a+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_ALL)
        if key == "3.0":
            key2 = "DESPESAS CORRENTES"
            try:
                df2_31 = df2.loc["3.1"]["VL_EMPENHADO"]
            except:
                df2_31 = 0.0
            try:
                df2_32 = df2.loc["3.2"]["VL_EMPENHADO"]
            except:
                df2_32 = 0.0
            try:
                df2_33 = df2.loc["3.3"]["VL_EMPENHADO"]
            except:
                df2_33 = 0.0
            try:
                df_31 = df1.loc["3.1"]["VL_EMPENHADO"]
            except:
                df_31 = 0.0
            try:
                df_32 = df1.loc["3.2"]["VL_EMPENHADO"]
            except:
                df_32 = 0.0
            try:
                df_33 = df1.loc["3.3"]["VL_EMPENHADO"]
            except:
                df_33 = 0.0

            df2_key = df2_31 + df2_32 + df2_33
            df_key = df_31 + df_32 + df_33
            try:
                finbra = finbra_file.loc[key2]["Valor"]
            except:
                finbra = 0
        if key == "4.0":
            key2 = "DESPESAS DE CAPITAL"
            try:
                df2_44 = df2.loc["4.4"]["VL_EMPENHADO"]
            except:
                df2_44 = 0.0
            try:
                df2_45 = df2.loc["4.5"]["VL_EMPENHADO"]
            except:
                df2_45 = 0.0
            try:
                df2_46 = df2.loc["4.6"]["VL_EMPENHADO"]
            except:
                df2_46 = 0.0
            try:
                df_44 = df1.loc["4.4"]["VL_EMPENHADO"]
            except:
                df_44 = 0.0
            try:
                df_45 = df1.loc["4.5"]["VL_EMPENHADO"]
            except:
                df_45 = 0.0
            try:
                df_46 = df1.loc["4.6"]["VL_EMPENHADO"]
            except:
                df_46 = 0.0

            df2_key = df2_44 + df2_45 + df2_46
            df_key = df_44 + df_45 + df_46
            try:
                finbra = finbra_file.loc[key2]["Valor"]
            except:
                finbra = 0
        if key == "1.0":
            key2 = "SUBTOTAL DAS DESPESAS ("
            try:
                df2_31 = df2.loc["3.1"]["VL_EMPENHADO"]
            except:
                df2_31 = 0.0
            try:
                df2_32 = df2.loc["3.2"]["VL_EMPENHADO"]
            except:
                df2_32 = 0.0
            try:
                df2_33 = df2.loc["3.3"]["VL_EMPENHADO"]
            except:
                df2_33 = 0.0
            try:
                df_31 = df1.loc["3.1"]["VL_EMPENHADO"]
            except:
                df_31 = 0.0
            try:
                df_32 = df1.loc["3.2"]["VL_EMPENHADO"]
            except:
                df_32 = 0.0
            try:
                df_33 = df1.loc["3.3"]["VL_EMPENHADO"]
            except:
                df_33 = 0.0

            df2_key = df2_31 + df2_32 + df2_33
            df_key = df_31 + df_32 + df_33

            try:
                df2_44 = df2.loc["4.4"]["VL_EMPENHADO"]
            except:
                df2_44 = 0.0
            try:
                df2_45 = df2.loc["4.5"]["VL_EMPENHADO"]
            except:
                df2_45 = 0.0
            try:
                df2_46 = df2.loc["4.6"]["VL_EMPENHADO"]
            except:
                df2_46 = 0.0
            try:
                df_44 = df1.loc["4.4"]["VL_EMPENHADO"]
            except:
                df_44 = 0.0
            try:
                df_45 = df1.loc["4.5"]["VL_EMPENHADO"]
            except:
                df_45 = 0.0
            try:
                df_46 = df1.loc["4.6"]["VL_EMPENHADO"]
            except:
                df_46 = 0.0

            df2_key = df2_key + df2_44 + df2_45 + df2_46
            df_key = df_key + df_44 + df_45 + df_46

            indexNamesArr = finbra_file.index.values
            indexNamesArr = list(indexNamesArr)
            for text in indexNamesArr:
                if key2 in text:
                    key2 = text
            try:
                finbra = finbra_file.loc[key2]["Valor"]
            except:
                finbra = 0.0

        compara_writer.writerow(localize_floats([cod_ibge, cidade, key2, finbra,
                                             df2_key, df_key,
                                             finbra == df2_key, finbra == df_key]))
    return

def compara_dados(key, key2, finbra_file, cod_ibge, cidade, diretorio, ano, df1, df2):
    with open(diretorio + "Finbra_balorc\\" + ano + "_compara_despesas.csv", mode='a+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_ALL)
        try:
            df2_key = df2.loc[key]["VL_EMPENHADO"]
        except:
            df2_key = 0.0
        try:
            df_key = df1.loc[key]["VL_EMPENHADO"]
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


def processa_dados_balorc_despesas(df1, df2, cidade, cod_ibge, balorc, diretorio, ano):
        print(cidade)

        key = "3.0"
        compara_dados_totais(key, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "4.0"
        compara_dados_totais(key, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)
        key = "1.0"
        compara_dados_totais(key, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "3.1"
        key2 = "PESSOAL E ENCARGOS SOCIAIS"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "3.2"
        key2 = "JUROS E ENCARGOS DA DIVIDA"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "3.3"
        key2 = "OUTRAS DESPESAS CORRENTES"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "4.4"
        key2 = "INVESTIMENTOS"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "4.5"
        key2 = "INVERSOES FINANCEIRAS"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)

        key = "4.6"
        key2 = "AMORTIZACAO DA DIVIDA"
        compara_dados(key, key2, balorc, cod_ibge, cidade, diretorio, ano, df1, df2)




def main():
    diretorio = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_RS\\"
    ano = '2017'
    municipios = pandas.read_csv(diretorio + 'RS_municipios_TCE.csv', sep = ';', encoding='latin1')
    balorc_finbra_despesas = pandas.read_csv(diretorio + 'Finbra_balorc\\' + ano + ' - despesas.csv', sep=';', encoding='latin1')
    balorc_finbra_despesas_intra = pandas.read_csv(diretorio + 'Finbra_balorc\\' + ano + ' - despesas_intra.csv', sep=';', encoding='latin1')
    balorc_finbra_despesas = pandas.concat([balorc_finbra_despesas, balorc_finbra_despesas_intra])
    print(municipios)
    with open(diretorio + "Finbra_balorc\\" + ano + "_compara_despesas.csv", mode='w+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        compara_writer.writerow(["cod_ibge", "cidade", "key", "valor_finbra", "valor_tce", "valor_tce_prefeitura",
                                                                                    "compara", "compara_prefeitura"])

    for index, row in municipios.iterrows():
        diretorio2 = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_RS\\dados - despesas - 2017\\"
        registros = carrega_dados(diretorio2, row['NOME_MUNICIPIO'])
        #registros['DS_CONTA_SG'] = registros['DS_CONTA_SG'].apply(remover_acentos)
        #registros['CD_CONTA_SG'] = registros['CD_CONTA_SG'].apply(remover_ponto_virgula_zero)

        registros['CD_ELEMENTO'] = registros['CD_ELEMENTO'].apply(tres_caracteres)
        df1 = registros[registros['NOME_MUNICIPIO'] == row['NOME_MUNICIPIO']]

        df1 = df1[~df1['NOME_ORGAO'].str.contains('INTER', regex=False)]

        #df1.loc[df1["CD_CONTA_SG"].apply(primeiro_algarismo) == "1","VL_SALDO_ATUAL_DEV"] = df1["VL_SALDO_ATUAL_DEV"]  - df1["VL_SALDO_ATUAL_CRE"]
        #df1.loc[df1["CD_CONTA_SG"].apply(primeiro_algarismo) == "2","VL_SALDO_ATUAL_CRE"] = df1["VL_SALDO_ATUAL_CRE"]  - df1["VL_SALDO_ATUAL_DEV"]
        df2 = df1.groupby(["CD_ELEMENTO"])[["VL_EMPENHADO","VL_LIQUIDADO",
                                                                         "VL_PAGO"]].agg("sum")
        df1 = df1[df1["NOME_ORGAO"].apply(tres_caracteres) == "PM "]
        df1 = df1.groupby(["CD_ELEMENTO"])[["VL_EMPENHADO","VL_LIQUIDADO","VL_PAGO"]].agg("sum")


        balorc = balorc_finbra_despesas[balorc_finbra_despesas["Cod_IBGE"] == row['CD_MUNICIPIO_IBGE']]
        balorc = balorc[balorc["Coluna"] == 'DESPESAS EMPENHADAS ATÉ O BIMESTRE (f)']
        balorc["Valor"] = balorc["Valor"].apply(converte_float)
        balorc["Conta"] = balorc["Conta"].apply(remover_acentos)
        balorc = balorc.groupby(["Conta"])[["Valor"]].agg("sum")
        processa_dados_balorc_despesas(df1, df2, row['NOME_MUNICIPIO'], row['CD_MUNICIPIO_IBGE'], balorc, diretorio, ano)

if __name__ == '__main__':
    main()