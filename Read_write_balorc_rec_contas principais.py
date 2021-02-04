import pandas
import string
import math
import csv
import os
from unicodedata import normalize


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def containsNumber(line):
    res = False
    numero = 0
    if any(i.isdigit() for i in str(line)):
        res = True
        line = str(line).split(" ")
        for l in line:
            if any(k.isdigit() for k in l):
                l = l.replace(".", "")
                l = l.replace(",", "")
                l = l[:-2] + "." + l[-2:]
                try:
                    numero = float(l)
                except:
                    numero = 0
    return res, numero


def buscaKeyParts(diretorio, file, key):
    df = pandas.read_csv(diretorio + file, names=list(range(0, 10)))
    mask = df.applymap(lambda x: key.upper() in remover_acentos(str(x).upper()))
    # print(mask)
    df1 = df[mask.any(axis=1)]
    print(df1)
    i = 0
    j = 0
    resultado = [0, 0, 0, 0, 0, 0]
    if df1.empty == False:
        for (columnName, columnData) in df1.iteritems():
            if key.upper() in remover_acentos(str(columnData.values[0]).upper()):
                j = 1
            print('Colunm Name : ', columnName)
            print('Column Contents : ', columnData.values)
            if j == 1 and columnData.values[0] and (
                    isinstance(columnData.values[0], float) and math.isnan(columnData.values[0])) == False:
                containnumber1, containnumber2 = containsNumber(columnData.values[0])
                print('contain number : ', containnumber1, containnumber2)
                if containnumber1 == True and i < 6:
                    resultado[i] = containnumber2
                    i += 1
    return resultado


def main():
    diretorio = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\ORIG\\RESULTS2_receitas_contas_principais\\"
    files = os.listdir(diretorio)
    csv_files = [f for f in files if f.endswith('.csv')]
    files2 = [d for d in csv_files if 'tables' in d]
    new = ""

    receitas_correntes = [" ", " ", " ", " ", " ", " "]
    receita_tributaria = [" ", " ", " ", " ", " ", " "]
    receita_contribuicoes = [" ", " ", " ", " ", " ", " "]
    receita_patrimonial = [" ", " ", " ", " ", " ", " "]
    transferencias_correntes = [" ", " ", " ", " ", " ", " "]
    outras_receitas_correntes = [" ", " ", " ", " ", " ", " "]
    receitas_capital = [" ", " ", " ", " ", " ", " "]
    operacoes_credito = [" ", " ", " ", " ", " ", " "]
    alienacao_bens = [" ", " ", " ", " ", " ", " "]
    transferencia_capital = [" ", " ", " ", " ", " ", " "]
    outras_receitas_capital = [" ", " ", " ", " ", " ", " "]
    subtotal_receitas = [" ", " ", " ", " ", " ", " "]
    subtotal_refinanciamento = [" ", " ", " ", " ", " ", " "]
    total = [" ", " ", " ", " ", " ", " "]
    saldos_ex_anteriores = [" ", " ", " ", " ", " ", " "]


    for file in files2:
        print(file)
        file_parts = file.split(".")

        with open(diretorio + new + "_tratado.csv", mode='a+') as balorc_file:
            balorc_writer = csv.writer(balorc_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

            if receitas_correntes[0] == 0 and receitas_correntes[1] == 0:
                balorc_writer.writerow(['RECEITAS CORRENTES', receitas_correntes[0], receitas_correntes[1], receitas_correntes[2], receitas_correntes[3]])

            if receita_tributaria[0] == 0 and receita_tributaria[1] == 0:
                balorc_writer.writerow(
                        ['RECEITA TRIBUTARIA', receita_tributaria[0], receita_tributaria[1], receita_tributaria[2], receita_tributaria[3]])

            if receita_contribuicoes[0] == 0 and receita_contribuicoes[1] == 0:
                balorc_writer.writerow(
                        ['RECEITA DE CONTRIBUICOES', receita_contribuicoes[0], receita_contribuicoes[1], receita_contribuicoes[2], receita_contribuicoes[3]])

            if receita_patrimonial[0] == 0 and receita_patrimonial[1] == 0:
                balorc_writer.writerow(['RECEITA PATRIMONIAL', receita_patrimonial[0], receita_patrimonial[1], receita_patrimonial[2], receita_patrimonial[3]])

            if transferencias_correntes[0] == 0 and transferencias_correntes[1] == 0:
                balorc_writer.writerow(['TRANSFERENCIAS CORRENTES', transferencias_correntes[0], transferencias_correntes[1], transferencias_correntes[2], transferencias_correntes[3]])

            if outras_receitas_correntes[0] == 0 and outras_receitas_correntes[1] == 0:
                balorc_writer.writerow(['Outras Receitas Correntes', outras_receitas_correntes[0], outras_receitas_correntes[1], outras_receitas_correntes[2], outras_receitas_correntes[3]])

            if receitas_capital[0] == 0 and receitas_capital[1] == 0:
                balorc_writer.writerow(
                        ['RECEITAS DE CAPITAL', receitas_capital[0], receitas_capital[1], receitas_capital[2], receitas_capital[3]])

            if operacoes_credito[0] == 0 and operacoes_credito[1] == 0:
                balorc_writer.writerow(
                        ['OPERACOES DE CREDITO', operacoes_credito[0], operacoes_credito[1], operacoes_credito[2], operacoes_credito[3]])

            if alienacao_bens[0] == 0 and alienacao_bens[1] == 0:
                balorc_writer.writerow(
                        ['ALIENACAO DE BENS', alienacao_bens[0], alienacao_bens[1], alienacao_bens[2], alienacao_bens[3]])

            if transferencia_capital[0] == 0 and transferencia_capital[1] == 0:
                balorc_writer.writerow(
                        ['TRANFERENCIAS DE CAPITAL', transferencia_capital[0], transferencia_capital[1], transferencia_capital[2], transferencia_capital[3]])

            if outras_receitas_capital[0] == 0 and outras_receitas_capital[1] == 0:
                balorc_writer.writerow(
                        ['OUTRAS RECEITAS DE CAPITAL', outras_receitas_capital[0], outras_receitas_capital[1], outras_receitas_capital[2], outras_receitas_capital[3]])

            if subtotal_receitas[0] == 0 and subtotal_receitas[1] == 0:
                balorc_writer.writerow(['SUBTOTAL DAS RECEITAS', subtotal_receitas[0], subtotal_receitas[1], subtotal_receitas[2], subtotal_receitas[3]])

            if subtotal_refinanciamento[0] == 0 and subtotal_refinanciamento[1] == 0:
                balorc_writer.writerow(
                        ['SUBTOTAL COM REFINANCIAMENTO', subtotal_refinanciamento[0], subtotal_refinanciamento[1], subtotal_refinanciamento[2], subtotal_refinanciamento[3]])

            if total[0] == 0 and total[1] == 0:
                balorc_writer.writerow(['TOTAL (', total[0], total[1], total[2], total[3]])

            if saldos_ex_anteriores[0] == 0 and saldos_ex_anteriores[1] == 0:
                balorc_writer.writerow(
                        ['SALDOS DE EXERCICIOS ANTERIORES', saldos_ex_anteriores[0], saldos_ex_anteriores[1], saldos_ex_anteriores[2], saldos_ex_anteriores[3]])


        new = file_parts[0]
        with open(diretorio + file_parts[0] + "_tratado.csv", mode='w+') as balorc_file:
            balorc_writer = csv.writer(balorc_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
            balorc_writer.writerow(["Key", "1", "2", "3", "4", "5", "6"])

            receitas_correntes = buscaKeyParts(diretorio, file, 'RECEITAS CORRENTES')
            print("receitas_correntes", receitas_correntes)
            if receitas_correntes[0] != 0 or receitas_correntes[1] != 0:
                balorc_writer.writerow(['RECEITAS CORRENTES', receitas_correntes[0], receitas_correntes[1], receitas_correntes[2], receitas_correntes[3]])

            receita_tributaria = buscaKeyParts(diretorio, file, 'RECEITA TRIBUTARIA')
            print("receita_tributaria", receita_tributaria)
            if receita_tributaria[0] != 0 or receita_tributaria[1] != 0:
                balorc_writer.writerow(
                    ['RECEITA TRIBUTARIA', receita_tributaria[0], receita_tributaria[1], receita_tributaria[2], receita_tributaria[3]])

            receita_contribuicoes = buscaKeyParts(diretorio, file, 'RECEITA DE CONTRIBUICOES')
            print("receita_contribuicoes", receita_contribuicoes)
            if receita_contribuicoes[0] != 0 or receita_contribuicoes[1] != 0:
                balorc_writer.writerow(
                    ['RECEITA DE CONTRIBUICOES', receita_contribuicoes[0], receita_contribuicoes[1], receita_contribuicoes[2], receita_contribuicoes[3]])

            receita_patrimonial = buscaKeyParts(diretorio, file, 'RECEITA PATRIMONIAL')
            print("receita_patrimonial", receita_patrimonial)
            if receita_patrimonial[0] != 0 or receita_patrimonial[1] != 0:
                balorc_writer.writerow(['RECEITA PATRIMONIAL', receita_patrimonial[0], receita_patrimonial[1], receita_patrimonial[2], receita_patrimonial[3]])

            transferencias_correntes = buscaKeyParts(diretorio, file, 'TRANSFERENCIAS CORRENTES')
            print("transferencias_correntes", transferencias_correntes)
            if transferencias_correntes[0] != 0 or transferencias_correntes[1] != 0:
                balorc_writer.writerow(['TRANSFERENCIAS CORRENTES', transferencias_correntes[0], transferencias_correntes[1], transferencias_correntes[2], transferencias_correntes[3]])

            outras_receitas_correntes = buscaKeyParts(diretorio, file, 'OUTRAS RECEITAS CORRENTES')
            print("outras_receitas_correntes", outras_receitas_correntes)
            if outras_receitas_correntes[0] != 0 or outras_receitas_correntes[1] != 0:
                balorc_writer.writerow(['OUTRAS RECEITAS CORRENTES', outras_receitas_correntes[0], outras_receitas_correntes[1], outras_receitas_correntes[2], outras_receitas_correntes[3]])

            receitas_capital = buscaKeyParts(diretorio, file, 'RECEITAS DE CAPITAL')
            print("receitas_capital", receitas_capital)
            if receitas_capital[0] != 0 or receitas_capital[1] != 0:
                balorc_writer.writerow(
                    ['RECEITAS DE CAPITAL', receitas_capital[0], receitas_capital[1], receitas_capital[2], receitas_capital[3]])

            operacoes_credito = buscaKeyParts(diretorio, file, 'OPERACOES DE CREDITO')
            print("operacoes_credito", operacoes_credito)
            if operacoes_credito[0] != 0 or operacoes_credito[1] != 0:
                balorc_writer.writerow(
                    ['OPERACOES DE CREDITO', operacoes_credito[0], operacoes_credito[1], operacoes_credito[2], operacoes_credito[3]])

            alienacao_bens = buscaKeyParts(diretorio, file, 'ALIENACAO DE BENS')
            print("alienacao_bens", alienacao_bens)
            if alienacao_bens[0] != 0 or alienacao_bens[1] != 0:
                balorc_writer.writerow(
                    ['ALIENACAO DE BENS', alienacao_bens[0], alienacao_bens[1], alienacao_bens[2], alienacao_bens[3]])

            transferencia_capital = buscaKeyParts(diretorio, file, 'TRANSFERENCIAS DE CAPITAL')
            print("transferencia_capital", transferencia_capital)
            if transferencia_capital[0] != 0 or transferencia_capital[1] != 0:
                balorc_writer.writerow(
                    ['TRANFERENCIAS DE CAPITAL', transferencia_capital[0], transferencia_capital[1], transferencia_capital[2], transferencia_capital[3]])

            outras_receitas_capital = buscaKeyParts(diretorio, file, 'OUTRAS RECEITAS DE CAPITAL')
            print("outras_receitas_capital", outras_receitas_capital)
            if outras_receitas_capital[0] != 0 or outras_receitas_capital[1] != 0:
                balorc_writer.writerow(
                    ['OUTRAS RECEITAS DE CAPITAL', outras_receitas_capital[0], outras_receitas_capital[1], outras_receitas_capital[2], outras_receitas_capital[3]])

            subtotal_receitas = buscaKeyParts(diretorio, file,
                                                      'SUBTOTAL DAS RECEITAS')
            print("subtotal_receitas", subtotal_receitas)
            if subtotal_receitas[0] != 0 or subtotal_receitas[1] != 0:
                balorc_writer.writerow(['SUBTOTAL DAS RECEITAS', subtotal_receitas[0], subtotal_receitas[1], subtotal_receitas[2], subtotal_receitas[3]])

            subtotal_refinanciamento = buscaKeyParts(diretorio, file,
                                                                'SUBTOTAL COM REFINANCIAMENTO')
            print("subtotal_refinanciamento", subtotal_refinanciamento)
            if subtotal_refinanciamento[0] != 0 or subtotal_refinanciamento[1] != 0:
                balorc_writer.writerow(
                    ['SUBTOTAL COM REFINANCIAMENTO', subtotal_refinanciamento[0], subtotal_refinanciamento[1], subtotal_refinanciamento[2], subtotal_refinanciamento[3]])

            total = buscaKeyParts(diretorio, file, 'TOTAL (')
            print("total", total)
            if total[0] != 0 or total[1] != 0:
                balorc_writer.writerow(['TOTAL (', total[0], total[1], total[2], total[3]])

            saldos_ex_anteriores = buscaKeyParts(diretorio, file, 'SALDOS DE EXERCICIOS ANTERIORES')
            print("saldos_ex_anteriores", saldos_ex_anteriores)
            if saldos_ex_anteriores[0] != 0 or saldos_ex_anteriores[1] != 0:
                balorc_writer.writerow(
                    ['SALDOS DE EXERCICIOS ANTERIORES', saldos_ex_anteriores[0], saldos_ex_anteriores[1], saldos_ex_anteriores[2], saldos_ex_anteriores[3]])






if __name__ == "__main__":
    main()
