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
    diretorio = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALORC\\ORIG\\RESULT2_despesas\\"
    files = os.listdir(diretorio)
    csv_files = [f for f in files if f.endswith('.csv')]
    files2 = [d for d in csv_files if 'tables' in d]
    new = ""

    despesas_correntes = [" ", " ", " ", " ", " ", " "]
    pessoal_encargos_sociais = [" ", " ", " ", " ", " ", " "]
    juros_encargos_divida = [" ", " ", " ", " ", " ", " "]
    outras_despesas_correntes = [" ", " ", " ", " ", " ", " "]
    despesas_capital = [" ", " ", " ", " ", " ", " "]
    investimentos = [" ", " ", " ", " ", " ", " "]
    inversoes_financeiras = [" ", " ", " ", " ", " ", " "]
    amortizacao_divida = [" ", " ", " ", " ", " ", " "]
    reserva_contingencia = [" ", " ", " ", " ", " ", " "]
    reserva_rpps = [" ", " ", " ", " ", " ", " "]
    subtotal_despesas = [" ", " ", " ", " ", " ", " "]
    amortizacao_divida_refinanciamento = [" ", " ", " ", " ", " ", " "]
    subtotal_refinanciamento_d = [" ", " ", " ", " ", " ", " "]


    for file in files2:
        print(file)
        file_parts = file.split(".")

        if file_parts[0] != new:

            with open(diretorio + new + "_tratado.csv", mode='a+') as balorc_file:
                balorc_writer = csv.writer(balorc_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

                if despesas_correntes[0] == 0 and despesas_correntes[1] == 0:
                    balorc_writer.writerow(['DESPESAS CORRENTES', despesas_correntes[0], despesas_correntes[1], despesas_correntes[2], despesas_correntes[3], despesas_correntes[4], despesas_correntes[5]])

                if pessoal_encargos_sociais[0] == 0 and pessoal_encargos_sociais[1] == 0:
                    balorc_writer.writerow(['PESSOAL E ENCARGOS SOCIAIS', pessoal_encargos_sociais[0], pessoal_encargos_sociais[1], pessoal_encargos_sociais[2], pessoal_encargos_sociais[3], pessoal_encargos_sociais[4], pessoal_encargos_sociais[5]])

                if juros_encargos_divida[0] == 0 and juros_encargos_divida[1] == 0:
                    balorc_writer.writerow(['JUROS E ENCARGOS DA DIVIDA', juros_encargos_divida[0], juros_encargos_divida[1], juros_encargos_divida[2], juros_encargos_divida[3], juros_encargos_divida[4], juros_encargos_divida[5]])

                if outras_despesas_correntes[0] == 0 and outras_despesas_correntes[1] == 0:
                    balorc_writer.writerow(['OUTRAS DESPESAS CORRENTES', outras_despesas_correntes[0], outras_despesas_correntes[1], outras_despesas_correntes[2], outras_despesas_correntes[3], outras_despesas_correntes[4], outras_despesas_correntes[5]])

                if despesas_capital[0] == 0 and despesas_capital[1] == 0:
                    balorc_writer.writerow(['DESPESAS DE CAPITAL', despesas_capital[0], despesas_capital[1], despesas_capital[2], despesas_capital[3], despesas_capital[4], despesas_capital[5]])

                if investimentos[0] == 0 and investimentos[1] == 0:
                    balorc_writer.writerow(['INVESTIMENTOS', investimentos[0], investimentos[1], investimentos[2], investimentos[3], investimentos[4], investimentos[5]])

                if inversoes_financeiras[0] == 0 and inversoes_financeiras[1] == 0:
                    balorc_writer.writerow(
                            ['INVERSOES FINANCEIRAS', inversoes_financeiras[0], inversoes_financeiras[1], inversoes_financeiras[2], inversoes_financeiras[3], inversoes_financeiras[4], inversoes_financeiras[5]])

                if amortizacao_divida[0] == 0 and amortizacao_divida[1] == 0:
                    balorc_writer.writerow(['AMORTIZACAO DA DIVIDA', amortizacao_divida[0], amortizacao_divida[1], amortizacao_divida[2], amortizacao_divida[3], amortizacao_divida[4], amortizacao_divida[5]])

                if reserva_contingencia[0] == 0 and reserva_contingencia[1] == 0:
                    balorc_writer.writerow(['RESERVA DE CONTINGENCIA', reserva_contingencia[0], reserva_contingencia[1], reserva_contingencia[2], reserva_contingencia[3], reserva_contingencia[4], reserva_contingencia[5]])

                if reserva_rpps[0] == 0 and reserva_rpps[1] == 0:
                    balorc_writer.writerow(['RESERVA DO RPPS', reserva_rpps[0], reserva_rpps[1], reserva_rpps[2], reserva_rpps[3], reserva_rpps[4], reserva_rpps[5]])

                if subtotal_despesas[0] == 0 and subtotal_despesas[1] == 0:
                    balorc_writer.writerow(['SUBTOTAL DAS DESPESAS', subtotal_despesas[0], subtotal_despesas[1], subtotal_despesas[2], subtotal_despesas[3], subtotal_despesas[4], subtotal_despesas[5]])

                if amortizacao_divida_refinanciamento[0] == 0 and amortizacao_divida_refinanciamento[1] == 0:
                    balorc_writer.writerow(
                            ['AMORTIZACAO DA DIVIDA - REFINANCIAMENTO', amortizacao_divida_refinanciamento[0], amortizacao_divida_refinanciamento[1], amortizacao_divida_refinanciamento[2], amortizacao_divida_refinanciamento[3], amortizacao_divida_refinanciamento[4], amortizacao_divida_refinanciamento[5]])

                if subtotal_refinanciamento_d[0] == 0 and subtotal_refinanciamento_d[1] == 0:
                    balorc_writer.writerow(['SUBTOTAL COM REFINANCIAMENTO (XV)', subtotal_refinanciamento_d[0], subtotal_refinanciamento_d[1], subtotal_refinanciamento_d[2], subtotal_refinanciamento_d[3], subtotal_refinanciamento_d[4], subtotal_refinanciamento_d[5]])


            new = file_parts[0]
            with open(diretorio + file_parts[0] + "_tratado.csv", mode='w+') as balorc_file:
                balorc_writer = csv.writer(balorc_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
                balorc_writer.writerow(["Key", "1", "2", "3", "4", "5", "6"])

                despesas_correntes = buscaKeyParts(diretorio, file, 'DESPESAS CORRENTES')
                print("despesas_correntes", despesas_correntes)
                if despesas_correntes[0] != 0 or despesas_correntes[1] != 0:
                    balorc_writer.writerow(['DESPESAS CORRENTES', despesas_correntes[0], despesas_correntes[1], despesas_correntes[2], despesas_correntes[3], despesas_correntes[4], despesas_correntes[5]])

                pessoal_encargos_sociais = buscaKeyParts(diretorio, file, 'PESSOAL E ENCARGOS SOCIAIS')
                print("pessoal_encargos_sociais", pessoal_encargos_sociais)
                if pessoal_encargos_sociais[0] != 0 or pessoal_encargos_sociais[1] != 0:
                    balorc_writer.writerow(['PESSOAL E ENCARGOS SOCIAIS', pessoal_encargos_sociais[0], pessoal_encargos_sociais[1], pessoal_encargos_sociais[2], pessoal_encargos_sociais[3], pessoal_encargos_sociais[4], pessoal_encargos_sociais[5]])

                juros_encargos_divida = buscaKeyParts(diretorio, file, 'JUROS E ENCARGOS DA DIVIDA')
                print("juros_encargos_divida", juros_encargos_divida)
                if juros_encargos_divida[0] != 0 or juros_encargos_divida[1] != 0:
                    balorc_writer.writerow(['JUROS E ENCARGOS DA DIVIDA', juros_encargos_divida[0], juros_encargos_divida[1], juros_encargos_divida[2], juros_encargos_divida[3], juros_encargos_divida[4], juros_encargos_divida[5]])

                outras_despesas_correntes = buscaKeyParts(diretorio, file, 'OUTRAS DESPESAS CORRENTES')
                print("outras_despesas_correntes", outras_despesas_correntes)
                if outras_despesas_correntes[0] != 0 or outras_despesas_correntes[1] != 0:
                    balorc_writer.writerow(['OUTRAS DESPESAS CORRENTES', outras_despesas_correntes[0], outras_despesas_correntes[1], outras_despesas_correntes[2], outras_despesas_correntes[3], outras_despesas_correntes[4], outras_despesas_correntes[5]])

                despesas_capital = buscaKeyParts(diretorio, file, 'DESPESAS DE CAPITAL')
                print("despesas_capital", despesas_capital)
                if despesas_capital[0] != 0 or despesas_capital[1] != 0:
                    balorc_writer.writerow(['DESPESAS DE CAPITAL', despesas_capital[0], despesas_capital[1], despesas_capital[2], despesas_capital[3], despesas_capital[4], despesas_capital[5]])

                investimentos = buscaKeyParts(diretorio, file, 'INVESTIMENTOS')
                print("investimentos", investimentos)
                if investimentos[0] != 0 or investimentos[1] != 0:
                    balorc_writer.writerow(['INVESTIMENTOS', investimentos[0], investimentos[1], investimentos[2], investimentos[3], investimentos[4], investimentos[5]])

                inversoes_financeiras = buscaKeyParts(diretorio, file, 'INVERSOES FINANCEIRAS')
                print("inversoes_financeiras", inversoes_financeiras)
                if inversoes_financeiras[0] != 0 or inversoes_financeiras[1] != 0:
                    balorc_writer.writerow(
                        ['INVERSOES FINANCEIRAS', inversoes_financeiras[0], inversoes_financeiras[1], inversoes_financeiras[2], inversoes_financeiras[3], inversoes_financeiras[4], inversoes_financeiras[5]])

                amortizacao_divida = buscaKeyParts(diretorio, file, 'AMORTIZACAO DA DIVIDA')
                print("amortizacao_divida", amortizacao_divida)
                if amortizacao_divida[0] != 0 or amortizacao_divida[1] != 0:
                    balorc_writer.writerow(['AMORTIZACAO DA DIVIDA', amortizacao_divida[0], amortizacao_divida[1], amortizacao_divida[2], amortizacao_divida[3], amortizacao_divida[4], amortizacao_divida[5]])

                reserva_contingencia = buscaKeyParts(diretorio, file, 'RESERVA DE CONTINGENCIA')
                print("reserva_contingencia", reserva_contingencia)
                if reserva_contingencia[0] != 0 or reserva_contingencia[1] != 0:
                    balorc_writer.writerow(['RESERVA DE CONTINGENCIA', reserva_contingencia[0], reserva_contingencia[1], reserva_contingencia[2], reserva_contingencia[3], reserva_contingencia[4], reserva_contingencia[5]])

                reserva_rpps = buscaKeyParts(diretorio, file, 'RESERVA DO RPPS')
                print("reserva_rpps", reserva_rpps)
                if reserva_rpps[0] != 0 or reserva_rpps[1] != 0:
                    balorc_writer.writerow(['RESERVA DO RPPS', reserva_rpps[0], reserva_rpps[1], reserva_rpps[2], reserva_rpps[3], reserva_rpps[4], reserva_rpps[5]])

                subtotal_despesas = buscaKeyParts(diretorio, file, 'SUBTOTAL DAS DESPESAS')
                print("subtotal_despesas", subtotal_despesas)
                if subtotal_despesas[0] != 0 or subtotal_despesas[1] != 0:
                    balorc_writer.writerow(['SUBTOTAL DAS DESPESAS', subtotal_despesas[0], subtotal_despesas[1], subtotal_despesas[2], subtotal_despesas[3], subtotal_despesas[4], subtotal_despesas[5]])

                amortizacao_divida_refinanciamento = buscaKeyParts(diretorio, file, 'AMORTIZACAO DA DIVIDA - REFINANCIAMENTO')
                print("amortizacao_divida_refinanciamento", amortizacao_divida_refinanciamento)
                if amortizacao_divida_refinanciamento[0] != 0 or amortizacao_divida_refinanciamento[1] != 0:
                    balorc_writer.writerow(
                        ['AMORTIZACAO DA DIVIDA - REFINANCIAMENTO', amortizacao_divida_refinanciamento[0], amortizacao_divida_refinanciamento[1], amortizacao_divida_refinanciamento[2], amortizacao_divida_refinanciamento[3], amortizacao_divida_refinanciamento[4], amortizacao_divida_refinanciamento[5]])

                subtotal_refinanciamento_d = buscaKeyParts(diretorio, file, 'SUBTOTAL COM REFINANCIAMENTO (XV)')
                print("subtotal_refinanciamento_d", subtotal_refinanciamento_d)
                if subtotal_refinanciamento_d[0] != 0 or subtotal_refinanciamento_d[1] != 0:
                    balorc_writer.writerow(['SUBTOTAL COM REFINANCIAMENTO (XV)', subtotal_refinanciamento_d[0], subtotal_refinanciamento_d[1], subtotal_refinanciamento_d[2], subtotal_refinanciamento_d[3], subtotal_refinanciamento_d[4], subtotal_refinanciamento_d[5]])

        else:
            with open(diretorio + file_parts[0] + "_tratado.csv", mode='a+') as balorc_file:
                balorc_writer = csv.writer(balorc_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

                if despesas_correntes[0] == 0 and despesas_correntes[1] == 0:
                    despesas_correntes = buscaKeyParts(diretorio, file, 'DESPESAS CORRENTES')
                    print("despesas_correntes", despesas_correntes)
                    if despesas_correntes[0] != 0 or despesas_correntes[1] != 0:
                        balorc_writer.writerow(['DESPESAS CORRENTES', despesas_correntes[0], despesas_correntes[1], despesas_correntes[2], despesas_correntes[3], despesas_correntes[4], despesas_correntes[5]])

                if pessoal_encargos_sociais[0] == 0 and pessoal_encargos_sociais[1] == 0:
                    pessoal_encargos_sociais = buscaKeyParts(diretorio, file, 'PESSOAL E ENCARGOS SOCIAIS')
                    print("pessoal_encargos_sociais", pessoal_encargos_sociais)
                    if pessoal_encargos_sociais[0] != 0 or pessoal_encargos_sociais[1] != 0:
                        balorc_writer.writerow(['PESSOAL E ENCARGOS SOCIAIS', pessoal_encargos_sociais[0], pessoal_encargos_sociais[1], pessoal_encargos_sociais[2], pessoal_encargos_sociais[3], pessoal_encargos_sociais[4], pessoal_encargos_sociais[5]])

                if juros_encargos_divida[0] == 0 and juros_encargos_divida[1] == 0:
                    juros_encargos_divida = buscaKeyParts(diretorio, file, 'JUROS E ENCARGOS DA DIVIDA')
                    print("juros_encargos_divida", juros_encargos_divida)
                    if juros_encargos_divida[0] != 0 or juros_encargos_divida[1] != 0:
                        balorc_writer.writerow(['JUROS E ENCARGOS DA DIVIDA', juros_encargos_divida[0], juros_encargos_divida[1], juros_encargos_divida[2], juros_encargos_divida[3], juros_encargos_divida[4], juros_encargos_divida[5]])

                if outras_despesas_correntes[0] == 0 and outras_despesas_correntes[1] == 0:
                    outras_despesas_correntes = buscaKeyParts(diretorio, file, 'OUTRAS DESPESAS CORRENTES')
                    print("outras_despesas_correntes", outras_despesas_correntes)
                    if outras_despesas_correntes[0] != 0 or outras_despesas_correntes[1] != 0:
                        balorc_writer.writerow(['OUTRAS DESPESAS CORRENTES', outras_despesas_correntes[0], outras_despesas_correntes[1], outras_despesas_correntes[2], outras_despesas_correntes[3], outras_despesas_correntes[4], outras_despesas_correntes[5]])

                if despesas_capital[0] == 0 and despesas_capital[1] == 0:
                    despesas_capital = buscaKeyParts(diretorio, file, 'DESPESAS DE CAPITAL')
                    print("despesas_capital", despesas_capital)
                    if despesas_capital[0] != 0 or despesas_capital[1] != 0:
                        balorc_writer.writerow(['DESPESAS DE CAPITAL', despesas_capital[0], despesas_capital[1], despesas_capital[2], despesas_capital[3], despesas_capital[4], despesas_capital[5]])

                if investimentos[0] == 0 and investimentos[1] == 0:
                    investimentos = buscaKeyParts(diretorio, file, 'INVESTIMENTOS')
                    print("investimentos", investimentos)
                    if investimentos[0] != 0 or investimentos[1] != 0:
                        balorc_writer.writerow(['INVESTIMENTOS', investimentos[0], investimentos[1], investimentos[2], investimentos[3], investimentos[4], investimentos[5]])

                if inversoes_financeiras[0] == 0 and inversoes_financeiras[1] == 0:
                    inversoes_financeiras = buscaKeyParts(diretorio, file, 'INVERSOES FINANCEIRAS')
                    print("inversoes_financeiras", inversoes_financeiras)
                    if inversoes_financeiras[0] != 0 or inversoes_financeiras[1] != 0:
                        balorc_writer.writerow(
                            ['INVERSOES FINANCEIRAS', inversoes_financeiras[0], inversoes_financeiras[1], inversoes_financeiras[2], inversoes_financeiras[3], inversoes_financeiras[4], inversoes_financeiras[5]])

                if amortizacao_divida[0] == 0 and amortizacao_divida[1] == 0:
                    amortizacao_divida = buscaKeyParts(diretorio, file, 'AMORTIZACAO DA DIVIDA')
                    print("amortizacao_divida", amortizacao_divida)
                    if amortizacao_divida[0] != 0 or amortizacao_divida[1] != 0:
                        balorc_writer.writerow(['AMORTIZACAO DA DIVIDA', amortizacao_divida[0], amortizacao_divida[1], amortizacao_divida[2], amortizacao_divida[3], amortizacao_divida[4], amortizacao_divida[5]])

                if reserva_contingencia[0] == 0 and reserva_contingencia[1] == 0:
                    reserva_contingencia = buscaKeyParts(diretorio, file, 'RESERVA DE CONTINGENCIA')
                    print("reserva_contingencia", reserva_contingencia)
                    if reserva_contingencia[0] != 0 or reserva_contingencia[1] != 0:
                        balorc_writer.writerow(['RESERVA DE CONTINGENCIA', reserva_contingencia[0], reserva_contingencia[1], reserva_contingencia[2], reserva_contingencia[3], reserva_contingencia[4], reserva_contingencia[5]])

                if reserva_rpps[0] == 0 and reserva_rpps[1] == 0:
                    reserva_rpps = buscaKeyParts(diretorio, file, 'RESERVA DO RPPS')
                    print("reserva_rpps", reserva_rpps)
                    if reserva_rpps[0] != 0 or reserva_rpps[1] != 0:
                        balorc_writer.writerow(['RESERVA DO RPPS', reserva_rpps[0], reserva_rpps[1], reserva_rpps[2], reserva_rpps[3], reserva_rpps[4], reserva_rpps[5]])

                if subtotal_despesas[0] == 0 and subtotal_despesas[1] == 0:
                    subtotal_despesas = buscaKeyParts(diretorio, file, 'SUBTOTAL DAS DESPESAS')
                    print("subtotal_despesas", subtotal_despesas)
                    if subtotal_despesas[0] != 0 or subtotal_despesas[1] != 0:
                        balorc_writer.writerow(['SUBTOTAL DAS DESPESAS', subtotal_despesas[0], subtotal_despesas[1], subtotal_despesas[2], subtotal_despesas[3], subtotal_despesas[4], subtotal_despesas[5]])

                if amortizacao_divida_refinanciamento[0] == 0 and amortizacao_divida_refinanciamento[1] == 0:
                    amortizacao_divida_refinanciamento = buscaKeyParts(diretorio, file, 'REFINANCIAMENTO DA DIVIDA - REFINANCIAMENTO')
                    print("amortizacao_divida_refinanciamento", amortizacao_divida_refinanciamento)
                    if amortizacao_divida_refinanciamento[0] != 0 or amortizacao_divida_refinanciamento[1] != 0:
                        balorc_writer.writerow(
                            ['REFINANCIAMENTO DA DIVIDA - REFINANCIAMENTO', amortizacao_divida_refinanciamento[0], amortizacao_divida_refinanciamento[1], amortizacao_divida_refinanciamento[2], amortizacao_divida_refinanciamento[3], amortizacao_divida_refinanciamento[4], amortizacao_divida_refinanciamento[5]])

                if subtotal_refinanciamento_d[0] == 0 and subtotal_refinanciamento_d[1] == 0:
                    subtotal_refinanciamento_d = buscaKeyParts(diretorio, file, 'SUBTOTAL COM REFINANCIAMENTO (XV)')
                    print("subtotal_refinanciamento_d", subtotal_refinanciamento_d)
                    if subtotal_refinanciamento_d[0] != 0 or subtotal_refinanciamento_d[1] != 0:
                        balorc_writer.writerow(['SUBTOTAL COM REFINANCIAMENTO (XV)', subtotal_refinanciamento_d[0], subtotal_refinanciamento_d[1], subtotal_refinanciamento_d[2], subtotal_refinanciamento_d[3], subtotal_refinanciamento_d[4], subtotal_refinanciamento_d[5]])



if __name__ == "__main__":
    main()
