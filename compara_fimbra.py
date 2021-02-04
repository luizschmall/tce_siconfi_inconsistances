import pandas
import csv
import os
import glob
from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def main():
    diretorio = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALPAT\\ORIG\\RESULT\\2018_tratado\\"
    i = 0
    files = glob.glob(diretorio + "*tratado.csv")
    #files = ["C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALPAT\\ORIG\\RESULT\\2017_tratado\\006867_10_tratado.csv"]
    print(diretorio + "INDEX.csv")
    index_cod = pandas.read_csv(diretorio + "INDEX.csv", sep = ';', encoding='latin1')
    print(index_cod)
    finbra = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALPAT\\SICONFI\\2018_finbra_mod.csv"
    finbra_df = pandas.read_csv(finbra, sep= ';', encoding='latin1')
    print(finbra_df)

    with open("C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALPAT\\SICONFI\\2018_compara.csv", mode = 'w+') as compara_file:
        compara_writer = csv.writer(compara_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

        compara_writer.writerow(["cod_ibge", "cidade", "key", "valor_finbra", "valor_tce","compara"])

        for file in files:
            i += 1
            print(i, file)
            f1 = file.split("\\")
            f1 = f1[11].split("_")
            print(f1[0], f1[1])
            df_file = pandas.read_csv(file, sep = ';', encoding='latin1')
            cod_ibge = index_cod[index_cod['Index'] == int(f1[0])]
            cod_ibge = cod_ibge['cod_ibge'].values[0]
            finbra_file = finbra_df[finbra_df['Cod_IBGE'] == cod_ibge]
            print(finbra_file)

            for index, row in df_file.iterrows():
                print(row.values[0])

                if row.values[0].upper() == 'ATIVO CIRCULANTE':
                    key = "1.1.0.0.0.00.00"

                if row.values[0].upper() == 'CAIXA E EQUIVALENTES DE CAIXA':
                    key = "1.1.1.0.0.00.00"

                if row.values[0].upper() == 'CREDITOS A CURTO PRAZO':
                    key = "1.1.2.0.0.00.00"

                if row.values[0].upper() == 'INVESTIMENTOS E APLICACOES TEMPORARIAS A CURTO PRAZO':
                    key = "1.1.4.0.0.00.00"

                if row.values[0].upper() == 'ESTOQUES':
                    key = "1.1.5.0.0.00.00"

                if row.values[0].upper() == 'VPD PAGAS ANTECIPADAMENTE':
                    key = "1.1.9.0.0.00.00"

                if row.values[0].upper() == 'DEMAIS CREDITOS E VALORES A CURTO PRAZO':
                    key = "1.1.3.0.0.00.00"

                if row.values[0].upper() == 'TOTAL DO ATIVO CIRCULANTE':
                    key = "1.1.0.0.0.00.00"

                if row.values[0].upper() == 'ATIVO NAO CIRCULANTE':
                    key = "1.2.0.0.0.00.00"

                if row.values[0].upper() == 'IMOBILIZADO':
                    key = "1.2.3.0.0.00.00"

                if row.values[0].upper() == 'INVESTIMENTOS':
                    key = "1.2.2.0.0.00.00"

                if row.values[0].upper() == 'INTANGIVEL':
                    key = "1.2.4.0.0.00.00"

                if row.values[0].upper() == 'TOTAL DO ATIVO NAO CIRCULANTE':
                    key = "1.2.0.0.0.00.00"

                if row.values[0].upper() == 'PASSIVO CIRCULANTE':
                    key = "2.1.0.0.0.00.00"

                if row.values[0].upper() == 'Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Pagar a Curto Prazo'.upper():
                    key = "2.1.1.0.0.00.00"

                if row.values[0].upper() == 'Emprestimos e Financiamentos a Curto Prazo'.upper():
                    key = "2.1.2.0.0.00.00"

                if row.values[0].upper() == 'Fornecedores e Contas a Pagar a Curto Prazo'.upper():
                    key = "2.1.3.0.0.00.00"

                if row.values[0].upper() == 'Obrigacoes Fiscais a Curto Prazo'.upper():
                    key = "2.1.4.0.0.00.00"

                if row.values[0].upper() == 'Obrigacoes de Reparticoes e Outros Entes'.upper():
                    key = "2.1.5.0.0.00.00"

                if row.values[0].upper() == 'Provisoes a Curto Prazo'.upper():
                    key = "2.1.7.0.0.00.00"

                if row.values[0].upper() == 'Demais Obrigacoes a Curto Prazo'.upper():
                    key = "2.1.8.0.0.00.00"

                if row.values[0].upper() == 'TOTAL DO PASSIVO CIRCULANTE':
                    key = "2.1.0.0.0.00.00"

                if row.values[0].upper() == 'PASSIVO NAO CIRCULANTE':
                    key = "2.2.0.0.0.00.00"

                if row.values[0].upper() == 'Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Longo Prazo'.upper():
                    key = "2.2.1.0.0.00.00"

                if row.values[0].upper() == 'Emprestimos e Financiamentos a Longo Prazo'.upper():
                    key = "2.2.2.0.0.00.00"

                if row.values[0].upper() == 'Fornecedores e Contas a Pagar a Longo Prazo'.upper():
                    key = "2.2.3.0.0.00.00"

                if row.values[0].upper() == 'Obrigacoes Fiscais a Longo Prazo'.upper():
                    key = "2.2.4.0.0.00.00"

                if row.values[0].upper() == 'Provisoes a Longo Prazo'.upper():
                    key = "2.2.7.0.0.00.00"

                if row.values[0].upper() == 'Demais Obrigacoes a Longo Prazo'.upper():
                    key = "2.2.8.0.0.00.00"

                if row.values[0].upper() == 'Resultado Diferido'.upper():
                    key = "2.2.9.0.0.00.00"

                if row.values[0].upper() == 'TOTAL DO PASSIVO NAO CIRCULANTE':
                    key = "2.2.0.0.0.00.00"

                if row.values[0].upper() == 'PATRIMONIO LIQUIDO':
                    key = "2.3.0.0.0.00.00"

                if row.values[0].upper() == 'PATRIMONIO SOCIAL E CAPITAL SOCIAL':
                    key = "2.3.1.0.0.00.00"

                if row.values[0].upper() == 'ADIANTAMENTO PARA FUTURO AUMENTO DE CAPITAL':
                    key = "2.2.8.4.0.00.00"

#                if row.values[0].upper() == 'RESERVAS DE CAPITAL':
#                    key = "2.3.5.0.0.00.00"

                if row.values[0].upper() == 'AJUSTES DE AVALIACAO PATRIMONIAL':
                    key = "2.3.4.0.0.00.00"

                if row.values[0].upper() == 'RESERVAS DE LUCROS':
                    key = "2.3.5.0.0.00.00"

                if row.values[0].upper() == 'DEMAIS RESERVAS':
                    key = "2.3.6.0.0.00.00"

                if row.values[0].upper() == 'RESULTADOS ACUMULADOS':
                    key = "2.3.7.0.0.00.00"

                if row.values[0].upper() == 'TOTAL DO PATRIMONIO LIQUIDO':
                    key = "2.3.0.0.0.00.00"


                if row.values[0].upper() == 'TOTAL DO PASSIVO E DO PATRIMONIO LIQUIDO':
                    key = "2.0.0.0.0.00.00"

                if row.values[0].upper() == 'ATIVO FINANCEIRO':
                    key = "ATIVO FINANCEIRO"

                if row.values[0].upper() == 'ATIVO PERMANENTE':
                    key = "ATIVO PERMANENTE"

                if row.values[0].upper() == 'PASSIVO FINANCEIRO':
                    key = "PASSIVO FINANCEIRO"

                if row.values[0].upper() == 'PASSIVO PERMANENTE':
                    key = "PASSIVO PERMANENTE"

                mask = finbra_file.applymap(lambda x: key in remover_acentos(str(x).upper()))
                df1 = finbra_file[mask.any(axis=1)]
                print(df1)
                if df1.empty != True:
                    compara_writer.writerow([cod_ibge, df1['Instituição'].values[0], key + " - " + row.values[0].upper(), float(df1['Valor'].values[0].replace(",",".")), row.values[1], float(df1['Valor'].values[0].replace(",",".")) == row.values[1]])
                    print(cod_ibge, df1['Instituição'].values[0], key + " - " + row.values[0].upper(), float(df1['Valor'].values[0].replace(",",".")), row.values[1], float(df1['Valor'].values[0].replace(",",".")) == row.values[1])



if __name__=="__main__":
    main()

