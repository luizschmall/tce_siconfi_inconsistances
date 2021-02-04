import pandas
import csv
import os
import glob
import string
from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def localize_floats(row):
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el
        for el in row
    ]

def main():
    diretorio = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\ORIG\\RESULT2_despesas\\2018_tratado\\"
    i = 0
    files = glob.glob(diretorio + "*tratado.csv")
    print(diretorio + "INDEX.csv")
    index_cod = pandas.read_csv(diretorio + "INDEX.csv", sep = ';', encoding='latin1')
    print(index_cod)
    finbra2 = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\SICONFI\\2018 - despesas_mod.csv"
    finbra2_df = pandas.read_csv(finbra2, sep= ';', encoding='latin1')
    finbra2_2 = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\SICONFI\\2018 - despesas_intra_mod.csv"
    finbra2_2_df = pandas.read_csv(finbra2_2, sep= ';', encoding='latin1')
    print(finbra2_df)
    print(finbra2_2_df)

    with open("C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\SICONFI\\2018_compara_desp.csv", mode = 'w+') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

        compara_writer.writerow(localize_floats(["cod_ibge", "processo", "cidade", "key", "valor_finbra", "valor_tce","compara"]))

        for file in files:
            i += 1
            print(i, file)
            f1 = file.split("\\")
            f1 = f1[11].split("_")
            print(f1[0], f1[1])
            df_file = pandas.read_csv(file, sep = ';', encoding='latin1')
            cod_ibge = index_cod[index_cod['Index'] == int(f1[0])]
            unidade = cod_ibge['Unidade'].values[0]
            cod_ibge = cod_ibge['cod_ibge'].values[0]
            finbra2_file = finbra2_df[finbra2_df['Cod_IBGE'] == cod_ibge]
            finbra2_2_file = finbra2_2_df[finbra2_2_df['Cod_IBGE'] == cod_ibge]
            finbra2_file = finbra2_file[finbra2_df['Coluna'] == "DESPESAS EMPENHADAS ATÉ O BIMESTRE (f)"]
            finbra2_2_file = finbra2_2_file[finbra2_2_df['Coluna'] == "DESPESAS EMPENHADAS ATÉ O BIMESTRE (f)"]
            print(finbra2_file)
            print(finbra2_2_file)

            for index, row in df_file.iterrows():
                print(row.values[0])
                key = row.values[0].upper()
                if key == "TRANFERENCIAS DE CAPITAL":
                    key = "TRANSFERENCIAS DE CAPITAL"
                if key == "CONTRIBUICAO DE ILUMINACAO PUBLICA":
                    key = "ILUMINACAO PUBLICA"

                mask2 = finbra2_file.applymap(lambda x: key in remover_acentos(str(x).upper()))
                mask22 = finbra2_2_file.applymap(lambda x: key in remover_acentos(str(x).upper()))
                # print(mask)
                df12 = finbra2_file[mask2.any(axis=1)]
                df122 = finbra2_2_file[mask22.any(axis=1)]
                print(df12)
                print(df122)

                if df12.empty != True and df122.empty != True:
                    compara_writer.writerow(localize_floats([cod_ibge, f1[0], unidade, row.values[0].upper(), float(float(df12['Valor'].values[0].replace(",",".")) + float(df122['Valor'].values[0].replace(",","."))),
                                             float(row.values[3]), float(float(df12['Valor'].values[0].replace(",",".")) + float(df122['Valor'].values[0].replace(",","."))) == float(row.values[3])]))
                    print([cod_ibge, f1[0], unidade, row.values[0].upper(), float(df12['Valor'].values[0].replace(",",".")) + float(df122['Valor'].values[0].replace(",",".")),
                                             float(row.values[3]), float(df12['Valor'].values[0].replace(",",".")) + float(df122['Valor'].values[0].replace(",",".")) == float(row.values[3])])
                elif df12.empty != True and df122.empty == True:
                    compara_writer.writerow(localize_floats([cod_ibge, f1[0], unidade, row.values[0].upper(), float(df12['Valor'].values[0].replace(",",".")),
                                             float(row.values[3]), float(df12['Valor'].values[0].replace(",",".")) == float(row.values[3])]))
                    print([cod_ibge, f1[0], unidade, row.values[0].upper(), float(df12['Valor'].values[0].replace(",",".")),
                                             float(row.values[3]), float(df12['Valor'].values[0].replace(",",".")) == float(row.values[3])])

                if df12.empty == True:
                    compara_writer.writerow(localize_floats([cod_ibge, f1[0], unidade, row.values[0].upper(), 0.0, float(row.values[3]), 0.0 == float(row.values[3])]))
                    print(cod_ibge, f1[0], unidade, key + " - " + row.values[0].upper(), 0.0, float(row.values[3]), 0.0 == float(row.values[3]))



if __name__=="__main__":
    main()

