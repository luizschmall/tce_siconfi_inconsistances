import pandas
import csv
import os
import glob
from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def localize_floats(row):
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el
        for el in row
    ]

def main():
    diretorio = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\ORIG\\RESULTS2_receitas_contas_principais\\2018_tratado\\"
    i = 0
    files = glob.glob(diretorio + "*tratado.csv")
    print(diretorio + "INDEX.csv")
    index_cod = pandas.read_csv(diretorio + "INDEX.csv", sep = ';', encoding='latin1')
    print(index_cod)
    finbra1 = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\SICONFI\\2018 - receitas_mod.csv"
    finbra1_df = pandas.read_csv(finbra1, sep= ';', encoding='latin1')
    finbra1_1 = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\SICONFI\\2018 - receitas_intra_mod.csv"
    finbra1_1_df = pandas.read_csv(finbra1_1, sep= ';', encoding='latin1')
    print(finbra1_df)
    print(finbra1_1_df)

    with open("C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\SICONFI\\2018_compara_receitas.csv", mode = 'w+', newline='') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

        compara_writer.writerow(["cod_ibge", "processo", "cidade", "key", "valor_finbra", "valor_tce","compara"])

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
            finbra1_file = finbra1_df[finbra1_df['Cod_IBGE'] == cod_ibge]
            finbra1_1_file = finbra1_1_df[finbra1_1_df['Cod_IBGE'] == cod_ibge]
            finbra1_file = finbra1_file[finbra1_df['Coluna'] == "Até o Bimestre (c)"]
            finbra1_1_file = finbra1_1_file[finbra1_1_df['Coluna'] == "Até o Bimestre (c)"]
            print(finbra1_file)
            print(finbra1_1_file)


            for index, row in df_file.iterrows():
                print(row.values[0])
                key = row.values[0].upper()
                if key == "TRANFERENCIAS DE CAPITAL":
                    key = "TRANSFERENCIAS DE CAPITAL"
                if key == "CONTRIBUICAO DE ILUMINACAO PUBLICA":
                    key = "ILUMINACAO PUBLICA"

                mask1 = finbra1_file.applymap(lambda x: key in remover_acentos(str(x).upper()))
                mask11 = finbra1_1_file.applymap(lambda x: key in remover_acentos(str(x).upper()))
                # print(mask)
                df11 = finbra1_file[mask1.any(axis=1)]
                df111 = finbra1_1_file[mask11.any(axis=1)]
                print(df11)
                print(df111)
                if df11.empty != True and df111.empty != True:
                    compara_writer.writerow(localize_floats([cod_ibge, f1[0], unidade, row.values[0].upper(), float((float(df11['Valor'].values[0].replace(",",".")) + float(df111['Valor'].values[0].replace(",",".")))),
                                             float(row.values[3]), float((float(df11['Valor'].values[0].replace(",",".")) + float(df111['Valor'].values[0].replace(",",".")))) == float(row.values[3])]))
                    print(localize_floats([cod_ibge, f1[0], unidade, row.values[0].upper(), float(df11['Valor'].values[0].replace(",",".")) + float(df111['Valor'].values[0].replace(",",".")),
                                             float(row.values[3]), float(df11['Valor'].values[0].replace(",",".")) + float(df111['Valor'].values[0].replace(",",".")) == float(row.values[3])]))
                elif df11.empty != True and df111.empty == True:
                    print(float(df11['Valor'].values[0].replace(",",".")))
                    print(row.values[3])
                    compara_writer.writerow(localize_floats([cod_ibge, f1[0], unidade, row.values[0].upper(), float(df11['Valor'].values[0].replace(",",".")),
                                             float(row.values[3]), float(df11['Valor'].values[0].replace(",",".")) == float(row.values[3])]))
                    print(localize_floats([cod_ibge, f1[0], unidade, row.values[0].upper(), float(df11['Valor'].values[0].replace(",",".")),
                                             float(row.values[3]), float(df11['Valor'].values[0].replace(",",".")) == float(row.values[3])]))

                if df11.empty == True:
                    compara_writer.writerow(localize_floats([cod_ibge, f1[0], unidade, row.values[0].upper(), 0.0, float(row.values[3]), 0.0 == float(row.values[3])]))
                    print(localize_floats([cod_ibge, f1[0], unidade, key + " - " + row.values[0].upper(), 0.0, float(row.values[3]), 0.0 == float(row.values[3])]))



if __name__=="__main__":
    main()

