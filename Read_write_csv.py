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
                if "," in l:
                    l = l.replace(".", "")
                    l = l.replace(",", ".")
                else:
                    l = l.replace(".", "")
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
    resultado = [0, 0]
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
                if containnumber1 == True and i < 2:
                    resultado[i] = containnumber2
                    i += 1
    return resultado


def main():
    diretorio = "C:\\Users\\schmall\\Documents\\FGV\\Tese\\Balanços_PI\\BALPAT\\ORIG\\RESULT\\"
    files = os.listdir(diretorio)
    csv_files = [f for f in files if f.endswith('.csv')]
    files2 = [d for d in csv_files if 'tables' in d]
    #files2 = ['007180_10.BALPAT-2272018 (DFAM III)-pdf-page-4-tables.csv']
    new = ""

    ativo_circulante = [" ", " "]
    caixa_equivalentes = [" ", " "]
    creditos_a_c_prazo = [" ", " "]
    investimentos_aplic_temp_c_prazo = [" ", " "]
    estoques = [" ", " "]
    vpd_pagas_antecipadamente = [" ", " "]
    demais_creditos_val_c_prazo = [" ", " "]
    tot_ativo_circulante = [" ", " "]
    ativo_nao_circulantes = [" ", " "]
    imobilizado = [" ", " "]
    investimentos = [" ", " "]
    intangivel = [" ", " "]
    tot_ativo_n_circulante = [" ", " "]
    passivo_circulante = [" ", " "]
    obrigacoes_trabalhistas = [" ", " "]
    emprest_fin_c_prazo = [" ", " "]
    fornecedores_cont_pagar_c_prazo = [" ", " "]
    obrig_fiscais_c_prazo = [" ", " "]
    obrig_repart_outros_entes = [" ", " "]
    provisoes_c_prazo = [" ", " "]
    demais_obrig_c_prazo = [" ", " "]
    total_passivo_circulante = [" ", " "]
    passivo_n_circulante = [" ", " "]
    obrigacoes_trabalhistas_l = [" ", " "]
    emprest_fin_l_prazo = [" ", " "]
    fornecedores_cont_pagar_l_prazo = [" ", " "]
    obrig_fiscais_l_prazo = [" ", " "]
    provisoes_l_prazo = [" ", " "]
    demais_obrig_l_prazo = [" ", " "]
    result_difer = [" ", " "]
    total_passivo_n_circulante = [" ", " "]
    patrimonio_liquido = [" ", " "]
    patrimonio_social_cap_social = [" ", " "]
    adiantamento_fut_aum_cap = [" ", " "]
    reservas_capital = [" ", " "]
    ajustes_aval_patrim = [" ", " "]
    reservas_lucros = [" ", " "]
    demais_reservas = [" ", " "]
    result_acumulados = [" ", " "]
    total_p_l = [" ", " "]
    total_passivo_p_l = [" ", " "]
    ativo_financeiro = [" ", " "]
    ativo_permanente = [" ", " "]
    passivo_financeiro = [" ", " "]
    passivo_permanente = [" ", " "]

    for file in files2:
        print(file)
        file_parts = file.split(".")

        if file_parts[0] != new:

            with open(diretorio + new + "_tratado.csv", mode='a+') as balpat_file:
                balpat_writer = csv.writer(balpat_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

                if ativo_circulante[0] == 0 and ativo_circulante[1] == 0:
                    balpat_writer.writerow(['ATIVO CIRCULANTE', ativo_circulante[0], ativo_circulante[1]])

                if caixa_equivalentes[0] == 0 and caixa_equivalentes[1] == 0:
                    balpat_writer.writerow(
                            ['CAIXA E EQUIVALENTES DE CAIXA', caixa_equivalentes[0], caixa_equivalentes[1]])

                if creditos_a_c_prazo[0] == 0 and creditos_a_c_prazo[1] == 0:
                    balpat_writer.writerow(['CREDITOS A CURTO PRAZO', creditos_a_c_prazo[0], creditos_a_c_prazo[1]])

                if investimentos_aplic_temp_c_prazo[0] == 0 and investimentos_aplic_temp_c_prazo[1] == 0:
                    balpat_writer.writerow(
                            ['INVESTIMENTOS E APLICACOES TEMPORARIAS A CURTO PRAZO', investimentos_aplic_temp_c_prazo[0],
                             investimentos_aplic_temp_c_prazo[1]])

                if estoques[0] == 0 and estoques[1] == 0:
                    balpat_writer.writerow(['ESTOQUES', estoques[0], estoques[1]])

                if vpd_pagas_antecipadamente[0] == 0 and vpd_pagas_antecipadamente[1] == 0:
                    balpat_writer.writerow(
                            ['VPD PAGAS ANTECIPADAMENTE', vpd_pagas_antecipadamente[0], vpd_pagas_antecipadamente[1]])

                if demais_creditos_val_c_prazo[0] == 0 and demais_creditos_val_c_prazo[1] == 0:
                    balpat_writer.writerow(['DEMAIS CREDITOS E VALORES A CURTO PRAZO', demais_creditos_val_c_prazo[0],
                                                demais_creditos_val_c_prazo[1]])

                if tot_ativo_circulante[0] == 0 and tot_ativo_circulante[1] == 0:
                    balpat_writer.writerow(
                        ['TOTAL DO ATIVO CIRCULANTE', tot_ativo_circulante[0], tot_ativo_circulante[1]])

                if ativo_nao_circulantes[0] == 0 and ativo_nao_circulantes[1] == 0:
                    balpat_writer.writerow(['ATIVO NAO CIRCULANTE', ativo_nao_circulantes[0], ativo_nao_circulantes[1]])

                if imobilizado[0] == 0 and imobilizado[1] == 0:
                    balpat_writer.writerow(['IMOBILIZADO', imobilizado[0], imobilizado[1]])

                if investimentos[0] == 0 and investimentos[1] == 0:
                    balpat_writer.writerow(['INVESTIMENTOS', investimentos[0], investimentos[1]])

                if intangivel[0] == 0 and intangivel[1] == 0:
                    balpat_writer.writerow(['INTANGIVEL', intangivel[0], intangivel[1]])

                if tot_ativo_n_circulante[0] == 0 and tot_ativo_n_circulante[1] == 0:
                    balpat_writer.writerow(
                            ['TOTAL DO ATIVO NAO CIRCULANTE', tot_ativo_n_circulante[0], tot_ativo_n_circulante[1]])

                if passivo_circulante[0] == 0 and passivo_circulante[1] == 0:
                    balpat_writer.writerow(['PASSIVO CIRCULANTE', passivo_circulante[0], passivo_circulante[1]])

                if obrigacoes_trabalhistas[0] == 0 and obrigacoes_trabalhistas[1] == 0:
                    balpat_writer.writerow(
                            ['Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Pagar a Curto Prazo',
                             obrigacoes_trabalhistas[0], obrigacoes_trabalhistas[1]])

                if obrigacoes_trabalhistas[0] == 0 and obrigacoes_trabalhistas[1] == 0:
                    balpat_writer.writerow(['Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Pagar a Curto Prazo', obrigacoes_trabalhistas[0],
                                                obrigacoes_trabalhistas[1]])

                if emprest_fin_c_prazo[0] == 0 and emprest_fin_c_prazo[1] == 0:
                    balpat_writer.writerow(
                            ['Emprestimos e Financiamentos a Curto Prazo', emprest_fin_c_prazo[0], emprest_fin_c_prazo[1]])

                if fornecedores_cont_pagar_c_prazo[0] == 0 and fornecedores_cont_pagar_c_prazo[1] == 0:
                    balpat_writer.writerow(
                            ['Fornecedores e Contas a Pagar a Curto Prazo', fornecedores_cont_pagar_c_prazo[0],
                             fornecedores_cont_pagar_c_prazo[1]])

                if obrig_fiscais_c_prazo[0] == 0 and obrig_fiscais_c_prazo[1] == 0:
                    balpat_writer.writerow(
                            ['Obrigacoes Fiscais a Curto Prazo', obrig_fiscais_c_prazo[0], obrig_fiscais_c_prazo[1]])

                if obrig_repart_outros_entes[0] == 0 and obrig_repart_outros_entes[1] == 0:
                    balpat_writer.writerow(['Obrigacoes de Reparticoes e Outros Entes', obrig_repart_outros_entes[0],
                                                obrig_repart_outros_entes[1]])

                if provisoes_c_prazo[0] == 0 and provisoes_c_prazo[1] == 0:
                    balpat_writer.writerow(['Provisoes a Curto Prazo', provisoes_c_prazo[0], provisoes_c_prazo[1]])

                if demais_obrig_c_prazo[0] == 0 and demais_obrig_c_prazo[1] == 0:
                    balpat_writer.writerow(
                            ['Demais Obrigacoes a Curto Prazo', demais_obrig_c_prazo[0], demais_obrig_c_prazo[1]])

                if total_passivo_circulante[0] == 0 and total_passivo_circulante[1] == 0:
                    balpat_writer.writerow(
                            ['TOTAL DO PASSIVO CIRCULANTE', total_passivo_circulante[0], total_passivo_circulante[1]])

                if passivo_n_circulante[0] == 0 and passivo_n_circulante[1] == 0:
                    balpat_writer.writerow(['PASSIVO NAO CIRCULANTE', passivo_n_circulante[0], passivo_n_circulante[1]])

                if obrigacoes_trabalhistas_l[0] == 0 and obrigacoes_trabalhistas_l[1] == 0:
                    balpat_writer.writerow(['Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Longo Prazo',
                                                obrigacoes_trabalhistas_l[0], obrigacoes_trabalhistas_l[1]])

                if emprest_fin_l_prazo[0] == 0 and emprest_fin_l_prazo[1] == 0:
                    balpat_writer.writerow(
                            ['Emprestimos e Financiamentos a Longo Prazo', emprest_fin_l_prazo[0], emprest_fin_l_prazo[1]])

                if fornecedores_cont_pagar_l_prazo[0] == 0 and fornecedores_cont_pagar_l_prazo[1] == 0:
                    balpat_writer.writerow(
                            ['Fornecedores e Contas a Pagar a Longo Prazo', fornecedores_cont_pagar_l_prazo[0],
                             fornecedores_cont_pagar_l_prazo[1]])

                if obrig_fiscais_l_prazo[0] == 0 and obrig_fiscais_l_prazo[1] == 0:
                    balpat_writer.writerow(
                            ['Obrigacoes Fiscais a Longo Prazo', obrig_fiscais_l_prazo[0], obrig_fiscais_l_prazo[1]])

                if provisoes_l_prazo[0] == 0 and provisoes_l_prazo[1] == 0:
                    balpat_writer.writerow(['Provisoes a Longo Prazo', provisoes_l_prazo[0], provisoes_l_prazo[1]])

                if demais_obrig_l_prazo[0] == 0 and demais_obrig_l_prazo[1] == 0:
                    balpat_writer.writerow(
                            ['Demais Obrigacoes a Longo Prazo', demais_obrig_l_prazo[0], demais_obrig_l_prazo[1]])

                if result_difer[0] == 0 and result_difer[1] == 0:
                    balpat_writer.writerow(['Resultado Diferido', result_difer[0], result_difer[1]])

                if total_passivo_n_circulante[0] == 0 and total_passivo_n_circulante[1] == 0:
                    balpat_writer.writerow(['TOTAL DO PASSIVO NAO CIRCULANTE', total_passivo_n_circulante[0],
                                                total_passivo_n_circulante[1]])

                if patrimonio_liquido[0] == 0 and patrimonio_liquido[1] == 0:
                    balpat_writer.writerow(['PATRIMONIO LIQUIDO', patrimonio_liquido[0], patrimonio_liquido[1]])

                if patrimonio_social_cap_social[0] == 0 and patrimonio_social_cap_social[1] == 0:
                    balpat_writer.writerow(['PATRIMONIO SOCIAL E CAPITAL SOCIAL', patrimonio_social_cap_social[0],
                                                patrimonio_social_cap_social[1]])

                if adiantamento_fut_aum_cap[0] == 0 and adiantamento_fut_aum_cap[1] == 0:
                    balpat_writer.writerow(['ADIANTAMENTO PARA FUTURO AUMENTO DE CAPITAL', adiantamento_fut_aum_cap[0],
                                                adiantamento_fut_aum_cap[1]])

                if reservas_capital[0] == 0 and reservas_capital[1] == 0:
                    balpat_writer.writerow(['RESERVAS DE CAPITAL', reservas_capital[0], reservas_capital[1]])

                if ajustes_aval_patrim[0] == 0 and ajustes_aval_patrim[1] == 0:
                    balpat_writer.writerow(
                            ['AJUSTES DE AVALIACAO PATRIMONIAL', ajustes_aval_patrim[0], ajustes_aval_patrim[1]])

                if reservas_lucros[0] == 0 and reservas_lucros[1] == 0:
                    balpat_writer.writerow(['RESERVAS DE LUCROS', reservas_lucros[0], reservas_lucros[1]])

                if demais_reservas[0] == 0 and demais_reservas[1] == 0:
                    balpat_writer.writerow(['DEMAIS RESERVAS', demais_reservas[0], demais_reservas[1]])

                if result_acumulados[0] == 0 and result_acumulados[1] == 0:
                    balpat_writer.writerow(['RESULTADOS ACUMULADOS', result_acumulados[0], result_acumulados[1]])

                if total_p_l[0] == 0 and total_p_l[1] == 0:
                    balpat_writer.writerow(['TOTAL DO PATRIMONIO LIQUIDO', total_p_l[0], total_p_l[1]])

                if total_passivo_p_l[0] == 0 and total_passivo_p_l[1] == 0:
                    balpat_writer.writerow(
                            ['TOTAL DO PASSIVO E DO PATRIMONIO LIQUIDO', total_passivo_p_l[0], total_passivo_p_l[1]])

                if ativo_financeiro[0] == 0 and ativo_financeiro[1] == 0:
                    balpat_writer.writerow(['ATIVO FINANCEIRO', ativo_financeiro[0], ativo_financeiro[1]])

                if ativo_permanente[0] == 0 and ativo_permanente[1] == 0:
                    balpat_writer.writerow(['ATIVO PERMANENTE', ativo_permanente[0], ativo_permanente[1]])

                if passivo_financeiro[0] == 0 and passivo_financeiro[1] == 0:
                    balpat_writer.writerow(['PASSIVO FINANCEIRO', passivo_financeiro[0], passivo_financeiro[1]])

                if passivo_permanente[0] == 0 and passivo_permanente[1] == 0:
                    balpat_writer.writerow(['PASSIVO PERMANENTE', passivo_permanente[0], passivo_permanente[1]])


            new = file_parts[0]
            with open(diretorio + file_parts[0] + "_tratado.csv", mode='w+') as balpat_file:
                balpat_writer = csv.writer(balpat_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
                balpat_writer.writerow(["Key", "ano corrente", "ano anterior"])

                ativo_circulante = buscaKeyParts(diretorio, file, 'ATIVO CIRCULANTE')
                print("ativo_circulante", ativo_circulante)
                if ativo_circulante[0] != 0 or ativo_circulante[1] != 0:
                    balpat_writer.writerow(['ATIVO CIRCULANTE', ativo_circulante[0], ativo_circulante[1]])

                caixa_equivalentes = buscaKeyParts(diretorio, file, 'CAIXA E EQUIVALENTES DE CAIXA')
                print("caixa_equivalentes", caixa_equivalentes)
                if caixa_equivalentes[0] != 0 or caixa_equivalentes[1] != 0:
                    balpat_writer.writerow(
                        ['CAIXA E EQUIVALENTES DE CAIXA', caixa_equivalentes[0], caixa_equivalentes[1]])

                creditos_a_c_prazo = buscaKeyParts(diretorio, file, 'CREDITOS A CURTO PRAZO')
                print("creditos_a_c_prazo", creditos_a_c_prazo)
                if creditos_a_c_prazo[0] != 0 or creditos_a_c_prazo[1] != 0:
                    balpat_writer.writerow(['CREDITOS A CURTO PRAZO', creditos_a_c_prazo[0], creditos_a_c_prazo[1]])

                investimentos_aplic_temp_c_prazo = buscaKeyParts(diretorio, file,
                                                                 'INVESTIMENTOS E APLICACOES TEMPORARIAS A CURTO PRAZO')
                print("investimentos_aplic_temp_c_prazo", investimentos_aplic_temp_c_prazo)
                if investimentos_aplic_temp_c_prazo[0] != 0 or investimentos_aplic_temp_c_prazo[1] != 0:
                    balpat_writer.writerow(
                        ['INVESTIMENTOS E APLICACOES TEMPORARIAS A CURTO PRAZO', investimentos_aplic_temp_c_prazo[0],
                         investimentos_aplic_temp_c_prazo[1]])

                estoques = buscaKeyParts(diretorio, file, 'ESTOQUES')
                print("estoques", estoques)
                if estoques[0] != 0 or estoques[1] != 0:
                    balpat_writer.writerow(['ESTOQUES', estoques[0], estoques[1]])

                vpd_pagas_antecipadamente = buscaKeyParts(diretorio, file, 'VPD PAGAS ANTECIPADAMENTE')
                print("vpd_pagas_antecipadamente", vpd_pagas_antecipadamente)
                if vpd_pagas_antecipadamente[0] != 0 or vpd_pagas_antecipadamente[1] != 0:
                    balpat_writer.writerow(
                        ['VPD PAGAS ANTECIPADAMENTE', vpd_pagas_antecipadamente[0], vpd_pagas_antecipadamente[1]])

                demais_creditos_val_c_prazo = buscaKeyParts(diretorio, file, 'DEMAIS CREDITOS E VALORES A CURTO PRAZO')
                print("demais_creditos_val_c_prazo", demais_creditos_val_c_prazo)
                if demais_creditos_val_c_prazo[0] != 0 or demais_creditos_val_c_prazo[1] != 0:
                    balpat_writer.writerow(['DEMAIS CREDITOS E VALORES A CURTO PRAZO', demais_creditos_val_c_prazo[0],
                                            demais_creditos_val_c_prazo[1]])

                tot_ativo_circulante = buscaKeyParts(diretorio, file, 'TOTAL DO ATIVO CIRCULANTE')
                print("tot_ativo_circulante", tot_ativo_circulante)
                if tot_ativo_circulante[0] != 0 or tot_ativo_circulante[1] != 0:
                    balpat_writer.writerow(
                        ['TOTAL DO ATIVO CIRCULANTE', tot_ativo_circulante[0], tot_ativo_circulante[1]])

                ativo_nao_circulantes = buscaKeyParts(diretorio, file, 'ATIVO NAO CIRCULANTE')
                print("ativo_nao_circulantes", ativo_nao_circulantes)
                if ativo_nao_circulantes[0] != 0 or ativo_nao_circulantes[1] != 0:
                    balpat_writer.writerow(['ATIVO NAO CIRCULANTE', ativo_nao_circulantes[0], ativo_nao_circulantes[1]])

                imobilizado = buscaKeyParts(diretorio, file, 'IMOBILIZADO')
                print("imobilizado", imobilizado)
                if imobilizado[0] != 0 or imobilizado[1] != 0:
                    balpat_writer.writerow(['IMOBILIZADO', imobilizado[0], imobilizado[1]])

                investimentos = buscaKeyParts(diretorio, file, 'INVESTIMENTOS')
                print("investimentos", investimentos)
                if investimentos[0] != 0 or investimentos[1] != 0:
                    balpat_writer.writerow(['INVESTIMENTOS', investimentos[0], investimentos[1]])

                intangivel = buscaKeyParts(diretorio, file, 'INTANGIVEL')
                print("intangivel", intangivel)
                if intangivel[0] != 0 or intangivel[1] != 0:
                    balpat_writer.writerow(['INTANGIVEL', intangivel[0], intangivel[1]])

                tot_ativo_n_circulante = buscaKeyParts(diretorio, file, 'TOTAL DO ATIVO NAO CIRCULANTE')
                print("tot_ativo_n_circulante", tot_ativo_n_circulante)
                if tot_ativo_n_circulante[0] != 0 or tot_ativo_n_circulante[1] != 0:
                    balpat_writer.writerow(
                        ['TOTAL DO ATIVO NAO CIRCULANTE', tot_ativo_n_circulante[0], tot_ativo_n_circulante[1]])

                passivo_circulante = buscaKeyParts(diretorio, file, 'PASSIVO CIRCULANTE')
                print("passivo_circulante", passivo_circulante)
                if passivo_circulante[0] != 0 or passivo_circulante[1] != 0:
                    balpat_writer.writerow(['PASSIVO CIRCULANTE', passivo_circulante[0], passivo_circulante[1]])

                obrigacoes_trabalhistas = buscaKeyParts(diretorio, file,
                                                        'Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Pagar a Curto Prazo')
                print("obrigacoes_trabalhistas", obrigacoes_trabalhistas)
                if obrigacoes_trabalhistas[0] != 0 or obrigacoes_trabalhistas[1] != 0:
                    balpat_writer.writerow(
                        ['Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Pagar a Curto Prazo',
                         obrigacoes_trabalhistas[0], obrigacoes_trabalhistas[1]])

                if obrigacoes_trabalhistas[0] == 0 and obrigacoes_trabalhistas[1] == 0:
                    obrigacoes_trabalhistas = buscaKeyParts(diretorio, file, 'Obrigacoes Trabalhistas, Previdenciarias')
                    print("obrigacoes_trabalhistas", obrigacoes_trabalhistas)
                    if obrigacoes_trabalhistas[0] != 0 or obrigacoes_trabalhistas[1] != 0:
                        balpat_writer.writerow(['Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Pagar a Curto Prazo', obrigacoes_trabalhistas[0],
                                                obrigacoes_trabalhistas[1]])

                emprest_fin_c_prazo = buscaKeyParts(diretorio, file, 'Emprestimos e Financiamentos a Curto Prazo')
                print("emprest_fin_c_prazo", emprest_fin_c_prazo)
                if emprest_fin_c_prazo[0] != 0 or emprest_fin_c_prazo[1] != 0:
                    balpat_writer.writerow(
                        ['Emprestimos e Financiamentos a Curto Prazo', emprest_fin_c_prazo[0], emprest_fin_c_prazo[1]])

                fornecedores_cont_pagar_c_prazo = buscaKeyParts(diretorio, file,
                                                                'Fornecedores e Contas a Pagar a Curto Prazo')
                print("fornecedores_cont_pagar_c_prazo", fornecedores_cont_pagar_c_prazo)
                if fornecedores_cont_pagar_c_prazo[0] != 0 or fornecedores_cont_pagar_c_prazo[1] != 0:
                    balpat_writer.writerow(
                        ['Fornecedores e Contas a Pagar a Curto Prazo', fornecedores_cont_pagar_c_prazo[0],
                         fornecedores_cont_pagar_c_prazo[1]])

                obrig_fiscais_c_prazo = buscaKeyParts(diretorio, file, 'Obrigacoes Fiscais a Curto Prazo')
                print("obrig_fiscais_c_prazo", obrig_fiscais_c_prazo)
                if obrig_fiscais_c_prazo[0] != 0 or obrig_fiscais_c_prazo[1] != 0:
                    balpat_writer.writerow(
                        ['Obrigacoes Fiscais a Curto Prazo', obrig_fiscais_c_prazo[0], obrig_fiscais_c_prazo[1]])

                obrig_repart_outros_entes = buscaKeyParts(diretorio, file, 'Obrigacoes de Reparticoes e Outros Entes')
                print("obrig_repart_outros_entes", obrig_repart_outros_entes)
                if obrig_repart_outros_entes[0] != 0 or obrig_repart_outros_entes[1] != 0:
                    balpat_writer.writerow(['Obrigacoes de Reparticoes e Outros Entes', obrig_repart_outros_entes[0],
                                            obrig_repart_outros_entes[1]])

                provisoes_c_prazo = buscaKeyParts(diretorio, file, 'Provisoes a Curto Prazo')
                print("provisoes_c_prazo", provisoes_c_prazo)
                if provisoes_c_prazo[0] != 0 or provisoes_c_prazo[1] != 0:
                    balpat_writer.writerow(['Provisoes a Curto Prazo', provisoes_c_prazo[0], provisoes_c_prazo[1]])

                demais_obrig_c_prazo = buscaKeyParts(diretorio, file, 'Demais Obrigacoes a Curto Prazo')
                print("demais_obrig_c_prazo", demais_obrig_c_prazo)
                if demais_obrig_c_prazo[0] != 0 or demais_obrig_c_prazo[1] != 0:
                    balpat_writer.writerow(
                        ['Demais Obrigacoes a Curto Prazo', demais_obrig_c_prazo[0], demais_obrig_c_prazo[1]])

                total_passivo_circulante = buscaKeyParts(diretorio, file, 'TOTAL DO PASSIVO CIRCULANTE')
                print("total_passivo_circulante", total_passivo_circulante)
                if total_passivo_circulante[0] != 0 or total_passivo_circulante[1] != 0:
                    balpat_writer.writerow(
                        ['TOTAL DO PASSIVO CIRCULANTE', total_passivo_circulante[0], total_passivo_circulante[1]])

                passivo_n_circulante = buscaKeyParts(diretorio, file, 'PASSIVO NAO CIRCULANTE')
                print("passivo_n_circulante", passivo_n_circulante)
                if passivo_n_circulante[0] != 0 or passivo_n_circulante[1] != 0:
                    balpat_writer.writerow(['PASSIVO NAO CIRCULANTE', passivo_n_circulante[0], passivo_n_circulante[1]])

                obrigacoes_trabalhistas_l = buscaKeyParts(diretorio, file,
                                                          'Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Longo Prazo')
                print("obrigacoes_trabalhistas_l", obrigacoes_trabalhistas_l)
                if obrigacoes_trabalhistas_l[0] != 0 or obrigacoes_trabalhistas_l[1] != 0:
                    balpat_writer.writerow(['Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Longo Prazo',
                                            obrigacoes_trabalhistas_l[0], obrigacoes_trabalhistas_l[1]])

                emprest_fin_l_prazo = buscaKeyParts(diretorio, file, 'Emprestimos e Financiamentos a Longo Prazo')
                print("emprest_fin_l_prazo", emprest_fin_l_prazo)
                if emprest_fin_l_prazo[0] != 0 or emprest_fin_l_prazo[1] != 0:
                    balpat_writer.writerow(
                        ['Emprestimos e Financiamentos a Longo Prazo', emprest_fin_l_prazo[0], emprest_fin_l_prazo[1]])

                fornecedores_cont_pagar_l_prazo = buscaKeyParts(diretorio, file,
                                                                'Fornecedores e Contas a Pagar a Longo Prazo')
                print("fornecedores_cont_pagar_l_prazo", fornecedores_cont_pagar_l_prazo)
                if fornecedores_cont_pagar_l_prazo[0] != 0 or fornecedores_cont_pagar_l_prazo[1] != 0:
                    balpat_writer.writerow(
                        ['Fornecedores e Contas a Pagar a Longo Prazo', fornecedores_cont_pagar_l_prazo[0],
                         fornecedores_cont_pagar_l_prazo[1]])

                obrig_fiscais_l_prazo = buscaKeyParts(diretorio, file, 'Obrigacoes Fiscais a Longo Prazo')
                print("obrig_fiscais_l_prazo", obrig_fiscais_l_prazo)
                if obrig_fiscais_l_prazo[0] != 0 or obrig_fiscais_l_prazo[1] != 0:
                    balpat_writer.writerow(
                        ['Obrigacoes Fiscais a Longo Prazo', obrig_fiscais_l_prazo[0], obrig_fiscais_l_prazo[1]])

                provisoes_l_prazo = buscaKeyParts(diretorio, file, 'Provisoes a Longo Prazo')
                print("provisoes_l_prazo", provisoes_l_prazo)
                if provisoes_l_prazo[0] != 0 or provisoes_l_prazo[1] != 0:
                    balpat_writer.writerow(['Provisoes a Longo Prazo', provisoes_l_prazo[0], provisoes_l_prazo[1]])

                demais_obrig_l_prazo = buscaKeyParts(diretorio, file, 'Demais Obrigacoes a Longo Prazo')
                print("demais_obrig_l_prazo", demais_obrig_l_prazo)
                if demais_obrig_l_prazo[0] != 0 or demais_obrig_l_prazo[1] != 0:
                    balpat_writer.writerow(
                        ['Demais Obrigacoes a Longo Prazo', demais_obrig_l_prazo[0], demais_obrig_l_prazo[1]])

                result_difer = buscaKeyParts(diretorio, file, 'Resultado Diferido')
                print("result_difer", result_difer)
                if result_difer[0] != 0 or result_difer[1] != 0:
                    balpat_writer.writerow(['Resultado Diferido', result_difer[0], result_difer[1]])

                total_passivo_n_circulante = buscaKeyParts(diretorio, file, 'TOTAL DO PASSIVO NAO CIRCULANTE')
                print("total_passivo_n_circulante", total_passivo_n_circulante)
                if total_passivo_n_circulante[0] != 0 or total_passivo_n_circulante[1] != 0:
                    balpat_writer.writerow(['TOTAL DO PASSIVO NAO CIRCULANTE', total_passivo_n_circulante[0],
                                            total_passivo_n_circulante[1]])

                patrimonio_liquido = buscaKeyParts(diretorio, file, 'PATRIMONIO LIQUIDO')
                print("patrimonio_liquido", patrimonio_liquido)
                if patrimonio_liquido[0] != 0 or patrimonio_liquido[1] != 0:
                    balpat_writer.writerow(['PATRIMONIO LIQUIDO', patrimonio_liquido[0], patrimonio_liquido[1]])

                patrimonio_social_cap_social = buscaKeyParts(diretorio, file, 'PATRIMONIO SOCIAL E CAPITAL SOCIAL')
                print("patrimonio_social_cap_social", patrimonio_social_cap_social)
                if patrimonio_social_cap_social[0] != 0 or patrimonio_social_cap_social[1] != 0:
                    balpat_writer.writerow(['PATRIMONIO SOCIAL E CAPITAL SOCIAL', patrimonio_social_cap_social[0],
                                            patrimonio_social_cap_social[1]])

                adiantamento_fut_aum_cap = buscaKeyParts(diretorio, file, 'ADIANTAMENTO PARA FUTURO AUMENTO DE CAPITAL')
                print("adiantamento_fut_aum_cap", adiantamento_fut_aum_cap)
                if adiantamento_fut_aum_cap[0] != 0 or adiantamento_fut_aum_cap[1] != 0:
                    balpat_writer.writerow(['ADIANTAMENTO PARA FUTURO AUMENTO DE CAPITAL', adiantamento_fut_aum_cap[0],
                                            adiantamento_fut_aum_cap[1]])

                reservas_capital = buscaKeyParts(diretorio, file, 'RESERVAS DE CAPITAL')
                print("reservas_capital", reservas_capital)
                if reservas_capital[0] != 0 or reservas_capital[1] != 0:
                    balpat_writer.writerow(['RESERVAS DE CAPITAL', reservas_capital[0], reservas_capital[1]])

                ajustes_aval_patrim = buscaKeyParts(diretorio, file, 'AJUSTES DE AVALIACAO PATRIMONIAL')
                print("ajustes_aval_patrim", ajustes_aval_patrim)
                if ajustes_aval_patrim[0] != 0 or ajustes_aval_patrim[1] != 0:
                    balpat_writer.writerow(
                        ['AJUSTES DE AVALIACAO PATRIMONIAL', ajustes_aval_patrim[0], ajustes_aval_patrim[1]])

                reservas_lucros = buscaKeyParts(diretorio, file, 'RESERVAS DE LUCROS')
                print("reservas_lucros", reservas_lucros)
                if reservas_lucros[0] != 0 or reservas_lucros[1] != 0:
                    balpat_writer.writerow(['RESERVAS DE LUCROS', reservas_lucros[0], reservas_lucros[1]])

                demais_reservas = buscaKeyParts(diretorio, file, 'DEMAIS RESERVAS')
                print("demais_reservas", demais_reservas)
                if demais_reservas[0] != 0 or demais_reservas[1] != 0:
                    balpat_writer.writerow(['DEMAIS RESERVAS', demais_reservas[0], demais_reservas[1]])

                result_acumulados = buscaKeyParts(diretorio, file, 'RESULTADOS ACUMULADOS')
                print("result_acumulados", result_acumulados)
                if result_acumulados[0] != 0 or result_acumulados[1] != 0:
                    balpat_writer.writerow(['RESULTADOS ACUMULADOS', result_acumulados[0], result_acumulados[1]])

                total_p_l = buscaKeyParts(diretorio, file, 'TOTAL DO PATRIMONIO LIQUIDO')
                print("total_p_l", total_p_l)
                if total_p_l[0] != 0 or total_p_l[1] != 0:
                    balpat_writer.writerow(['TOTAL DO PATRIMONIO LIQUIDO', total_p_l[0], total_p_l[1]])

                total_passivo_p_l = buscaKeyParts(diretorio, file, 'TOTAL DO PASSIVO E DO PATRIMONIO LIQUIDO')
                print("total_passivo_p_l", total_passivo_p_l)
                if total_passivo_p_l[0] != 0 or total_passivo_p_l[1] != 0:
                    balpat_writer.writerow(
                        ['TOTAL DO PASSIVO E DO PATRIMONIO LIQUIDO', total_passivo_p_l[0], total_passivo_p_l[1]])

                ativo_financeiro = buscaKeyParts(diretorio, file, 'ATIVO FINANCEIRO')
                print("ativo_financeiro", ativo_financeiro)
                if ativo_financeiro[0] != 0 or ativo_financeiro[1] != 0:
                    balpat_writer.writerow(['ATIVO FINANCEIRO', ativo_financeiro[0], ativo_financeiro[1]])

                ativo_permanente = buscaKeyParts(diretorio, file, 'ATIVO PERMANENTE')
                print("ativo_permanente", ativo_permanente)
                if ativo_permanente[0] != 0 or ativo_permanente[1] != 0:
                    balpat_writer.writerow(['ATIVO PERMANENTE', ativo_permanente[0], ativo_permanente[1]])

                passivo_financeiro = buscaKeyParts(diretorio, file, 'PASSIVO FINANCEIRO')
                print("passivo_financeiro", passivo_financeiro)
                if passivo_financeiro[0] != 0 or passivo_financeiro[1] != 0:
                    balpat_writer.writerow(['PASSIVO FINANCEIRO', passivo_financeiro[0], passivo_financeiro[1]])

                passivo_permanente = buscaKeyParts(diretorio, file, 'PASSIVO PERMANENTE')
                print("ativo_permanente", passivo_permanente)
                if passivo_permanente[0] != 0 or passivo_permanente[1] != 0:
                    balpat_writer.writerow(['PASSIVO PERMANENTE', passivo_permanente[0], passivo_permanente[1]])

        else:
            with open(diretorio + file_parts[0] + "_tratado.csv", mode='a+') as balpat_file:
                balpat_writer = csv.writer(balpat_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

                if ativo_circulante[0] == 0 and ativo_circulante[1] == 0:
                    ativo_circulante = buscaKeyParts(diretorio, file, 'ATIVO CIRCULANTE')
                    print("ativo_circulante", ativo_circulante)
                    if ativo_circulante[0] != 0 or ativo_circulante[1] != 0:
                        balpat_writer.writerow(['ATIVO CIRCULANTE', ativo_circulante[0], ativo_circulante[1]])

                if caixa_equivalentes[0] == 0 and caixa_equivalentes[1] == 0:
                    caixa_equivalentes = buscaKeyParts(diretorio, file, 'CAIXA E EQUIVALENTES DE CAIXA')
                    print("caixa_equivalentes", caixa_equivalentes)
                    if caixa_equivalentes[0] != 0 or caixa_equivalentes[1] != 0:
                        balpat_writer.writerow(
                            ['CAIXA E EQUIVALENTES DE CAIXA', caixa_equivalentes[0], caixa_equivalentes[1]])

                if creditos_a_c_prazo[0] == 0 and creditos_a_c_prazo[1] == 0:
                    creditos_a_c_prazo = buscaKeyParts(diretorio, file, 'CREDITOS A CURTO PRAZO')
                    print("creditos_a_c_prazo", creditos_a_c_prazo)
                    if creditos_a_c_prazo[0] != 0 or creditos_a_c_prazo[1] != 0:
                        balpat_writer.writerow(['CREDITOS A CURTO PRAZO', creditos_a_c_prazo[0], creditos_a_c_prazo[1]])

                if investimentos_aplic_temp_c_prazo[0] == 0 and investimentos_aplic_temp_c_prazo[1] == 0:
                    investimentos_aplic_temp_c_prazo = buscaKeyParts(diretorio, file,
                                                                     'INVESTIMENTOS E APLICACOES TEMPORARIAS A CURTO PRAZO')
                    print("investimentos_aplic_temp_c_prazo", investimentos_aplic_temp_c_prazo)
                    if investimentos_aplic_temp_c_prazo[0] != 0 or investimentos_aplic_temp_c_prazo[1] != 0:
                        balpat_writer.writerow(
                            ['INVESTIMENTOS E APLICACOES TEMPORARIAS A CURTO PRAZO', investimentos_aplic_temp_c_prazo[0],
                             investimentos_aplic_temp_c_prazo[1]])

                if estoques[0] == 0 and estoques[1] == 0:
                    estoques = buscaKeyParts(diretorio, file, 'ESTOQUES')
                    print("estoques", estoques)
                    if estoques[0] != 0 or estoques[1] != 0:
                        balpat_writer.writerow(['ESTOQUES', estoques[0], estoques[1]])

                if vpd_pagas_antecipadamente[0] == 0 and vpd_pagas_antecipadamente[1] == 0:
                    vpd_pagas_antecipadamente = buscaKeyParts(diretorio, file, 'VPD PAGAS ANTECIPADAMENTE')
                    print("vpd_pagas_antecipadamente", vpd_pagas_antecipadamente)
                    if vpd_pagas_antecipadamente[0] != 0 or vpd_pagas_antecipadamente[1] != 0:
                        balpat_writer.writerow(
                            ['VPD PAGAS ANTECIPADAMENTE', vpd_pagas_antecipadamente[0], vpd_pagas_antecipadamente[1]])

                if demais_creditos_val_c_prazo[0] == 0 and demais_creditos_val_c_prazo[1] == 0:
                    demais_creditos_val_c_prazo = buscaKeyParts(diretorio, file, 'DEMAIS CREDITOS E VALORES A CURTO PRAZO')
                    print("demais_creditos_val_c_prazo", demais_creditos_val_c_prazo)
                    if demais_creditos_val_c_prazo[0] != 0 or demais_creditos_val_c_prazo[1] != 0:
                        balpat_writer.writerow(['DEMAIS CREDITOS E VALORES A CURTO PRAZO', demais_creditos_val_c_prazo[0],
                                                demais_creditos_val_c_prazo[1]])

                if tot_ativo_circulante[0] == 0 and tot_ativo_circulante[1] == 0:
                    tot_ativo_circulante = buscaKeyParts(diretorio, file, 'TOTAL DO ATIVO CIRCULANTE')
                    print("tot_ativo_circulante", tot_ativo_circulante)
                    if tot_ativo_circulante[0] != 0 or tot_ativo_circulante[1] != 0:
                        balpat_writer.writerow(
                            ['TOTAL DO ATIVO CIRCULANTE', tot_ativo_circulante[0], tot_ativo_circulante[1]])

                if ativo_nao_circulantes[0] == 0 and ativo_nao_circulantes[1] == 0:
                    ativo_nao_circulantes = buscaKeyParts(diretorio, file, 'ATIVO NAO CIRCULANTE')
                    print("ativo_nao_circulantes", ativo_nao_circulantes)
                    if ativo_nao_circulantes[0] != 0 or ativo_nao_circulantes[1] != 0:
                        balpat_writer.writerow(['ATIVO NAO CIRCULANTE', ativo_nao_circulantes[0], ativo_nao_circulantes[1]])

                if imobilizado[0] == 0 and imobilizado[1] == 0:
                    imobilizado = buscaKeyParts(diretorio, file, 'IMOBILIZADO')
                    print("imobilizado", imobilizado)
                    if imobilizado[0] != 0 or imobilizado[1] != 0:
                        balpat_writer.writerow(['IMOBILIZADO', imobilizado[0], imobilizado[1]])

                if investimentos[0] == 0 and investimentos[1] == 0:
                    investimentos = buscaKeyParts(diretorio, file, 'INVESTIMENTOS')
                    print("investimentos", investimentos)
                    if investimentos[0] != 0 or investimentos[1] != 0:
                        balpat_writer.writerow(['INVESTIMENTOS', investimentos[0], investimentos[1]])

                if intangivel[0] == 0 and intangivel[1] == 0:
                    intangivel = buscaKeyParts(diretorio, file, 'INTANGIVEL')
                    print("intangivel", intangivel)
                    if intangivel[0] != 0 or intangivel[1] != 0:
                        balpat_writer.writerow(['INTANGIVEL', intangivel[0], intangivel[1]])

                if tot_ativo_n_circulante[0] == 0 and tot_ativo_n_circulante[1] == 0:
                    tot_ativo_n_circulante = buscaKeyParts(diretorio, file, 'TOTAL DO ATIVO NAO CIRCULANTE')
                    print("tot_ativo_n_circulante", tot_ativo_n_circulante)
                    if tot_ativo_n_circulante[0] != 0 or tot_ativo_n_circulante[1] != 0:
                        balpat_writer.writerow(
                            ['TOTAL DO ATIVO NAO CIRCULANTE', tot_ativo_n_circulante[0], tot_ativo_n_circulante[1]])

                if passivo_circulante[0] == 0 and passivo_circulante[1] == 0:
                    passivo_circulante = buscaKeyParts(diretorio, file, 'PASSIVO CIRCULANTE')
                    print("passivo_circulante", passivo_circulante)
                    if passivo_circulante[0] != 0 or passivo_circulante[1] != 0:
                        balpat_writer.writerow(['PASSIVO CIRCULANTE', passivo_circulante[0], passivo_circulante[1]])

                if obrigacoes_trabalhistas[0] == 0 and obrigacoes_trabalhistas[1] == 0:
                    obrigacoes_trabalhistas = buscaKeyParts(diretorio, file,
                                                            'Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Pagar a Curto Prazo')
                    print("obrigacoes_trabalhistas", obrigacoes_trabalhistas)
                    if obrigacoes_trabalhistas[0] != 0 or obrigacoes_trabalhistas[1] != 0:
                        balpat_writer.writerow(
                            ['Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Pagar a Curto Prazo',
                             obrigacoes_trabalhistas[0], obrigacoes_trabalhistas[1]])

                if obrigacoes_trabalhistas[0] == 0 and obrigacoes_trabalhistas[1] == 0:
                    obrigacoes_trabalhistas = buscaKeyParts(diretorio, file, 'Obrigacoes Trabalhistas, Previdenciarias')
                    print("obrigacoes_trabalhistas", obrigacoes_trabalhistas)
                    if obrigacoes_trabalhistas[0] != 0 or obrigacoes_trabalhistas[1] != 0:
                        balpat_writer.writerow(['Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Pagar a Curto Prazo', obrigacoes_trabalhistas[0],
                                                obrigacoes_trabalhistas[1]])

                if emprest_fin_c_prazo[0] == 0 and emprest_fin_c_prazo[1] == 0:
                    emprest_fin_c_prazo = buscaKeyParts(diretorio, file, 'Emprestimos e Financiamentos a Curto Prazo')
                    print("emprest_fin_c_prazo", emprest_fin_c_prazo)
                    if emprest_fin_c_prazo[0] != 0 or emprest_fin_c_prazo[1] != 0:
                        balpat_writer.writerow(
                            ['Emprestimos e Financiamentos a Curto Prazo', emprest_fin_c_prazo[0], emprest_fin_c_prazo[1]])

                if fornecedores_cont_pagar_c_prazo[0] == 0 and fornecedores_cont_pagar_c_prazo[1] == 0:
                    fornecedores_cont_pagar_c_prazo = buscaKeyParts(diretorio, file,
                                                                    'Fornecedores e Contas a Pagar a Curto Prazo')
                    print("fornecedores_cont_pagar_c_prazo", fornecedores_cont_pagar_c_prazo)
                    if fornecedores_cont_pagar_c_prazo[0] != 0 or fornecedores_cont_pagar_c_prazo[1] != 0:
                        balpat_writer.writerow(
                            ['Fornecedores e Contas a Pagar a Curto Prazo', fornecedores_cont_pagar_c_prazo[0],
                             fornecedores_cont_pagar_c_prazo[1]])

                if obrig_fiscais_c_prazo[0] == 0 and obrig_fiscais_c_prazo[1] == 0:
                    obrig_fiscais_c_prazo = buscaKeyParts(diretorio, file, 'Obrigacoes Fiscais a Curto Prazo')
                    print("obrig_fiscais_c_prazo", obrig_fiscais_c_prazo)
                    if obrig_fiscais_c_prazo[0] != 0 or obrig_fiscais_c_prazo[1] != 0:
                        balpat_writer.writerow(
                            ['Obrigacoes Fiscais a Curto Prazo', obrig_fiscais_c_prazo[0], obrig_fiscais_c_prazo[1]])

                if obrig_repart_outros_entes[0] == 0 and obrig_repart_outros_entes[1] == 0:
                    obrig_repart_outros_entes = buscaKeyParts(diretorio, file, 'Obrigacoes de Reparticoes e Outros Entes')
                    print("obrig_repart_outros_entes", obrig_repart_outros_entes)
                    if obrig_repart_outros_entes[0] != 0 or obrig_repart_outros_entes[1] != 0:
                        balpat_writer.writerow(['Obrigacoes de Reparticoes e Outros Entes', obrig_repart_outros_entes[0],
                                                obrig_repart_outros_entes[1]])

                if provisoes_c_prazo[0] == 0 and provisoes_c_prazo[1] == 0:
                    provisoes_c_prazo = buscaKeyParts(diretorio, file, 'Provisoes a Curto Prazo')
                    print("provisoes_c_prazo", provisoes_c_prazo)
                    if provisoes_c_prazo[0] != 0 or provisoes_c_prazo[1] != 0:
                        balpat_writer.writerow(['Provisoes a Curto Prazo', provisoes_c_prazo[0], provisoes_c_prazo[1]])

                if demais_obrig_c_prazo[0] == 0 and demais_obrig_c_prazo[1] == 0:
                    demais_obrig_c_prazo = buscaKeyParts(diretorio, file, 'Demais Obrigacoes a Curto Prazo')
                    print("demais_obrig_c_prazo", demais_obrig_c_prazo)
                    if demais_obrig_c_prazo[0] != 0 or demais_obrig_c_prazo[1] != 0:
                        balpat_writer.writerow(
                            ['Demais Obrigacoes a Curto Prazo', demais_obrig_c_prazo[0], demais_obrig_c_prazo[1]])

                if total_passivo_circulante[0] == 0 and total_passivo_circulante[1] == 0:
                    total_passivo_circulante = buscaKeyParts(diretorio, file, 'TOTAL DO PASSIVO CIRCULANTE')
                    print("total_passivo_circulante", total_passivo_circulante)
                    if total_passivo_circulante[0] != 0 or total_passivo_circulante[1] != 0:
                        balpat_writer.writerow(
                            ['TOTAL DO PASSIVO CIRCULANTE', total_passivo_circulante[0], total_passivo_circulante[1]])

                if passivo_n_circulante[0] == 0 and passivo_n_circulante[1] == 0:
                    passivo_n_circulante = buscaKeyParts(diretorio, file, 'PASSIVO NAO CIRCULANTE')
                    print("passivo_n_circulante", passivo_n_circulante)
                    if passivo_n_circulante[0] != 0 or passivo_n_circulante[1] != 0:
                        balpat_writer.writerow(['PASSIVO NAO CIRCULANTE', passivo_n_circulante[0], passivo_n_circulante[1]])

                if obrigacoes_trabalhistas_l[0] == 0 and obrigacoes_trabalhistas_l[1] == 0:
                    obrigacoes_trabalhistas_l = buscaKeyParts(diretorio, file,
                                                              'Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Longo Prazo')
                    print("obrigacoes_trabalhistas_l", obrigacoes_trabalhistas_l)
                    if obrigacoes_trabalhistas_l[0] != 0 or obrigacoes_trabalhistas_l[1] != 0:
                        balpat_writer.writerow(['Obrigacoes Trabalhistas, Previdenciarias e Assistenciais a Longo Prazo',
                                                obrigacoes_trabalhistas_l[0], obrigacoes_trabalhistas_l[1]])

                if emprest_fin_l_prazo[0] == 0 and emprest_fin_l_prazo[1] == 0:
                    emprest_fin_l_prazo = buscaKeyParts(diretorio, file, 'Emprestimos e Financiamentos a Longo Prazo')
                    print("emprest_fin_l_prazo", emprest_fin_l_prazo)
                    if emprest_fin_l_prazo[0] != 0 or emprest_fin_l_prazo[1] != 0:
                        balpat_writer.writerow(
                            ['Emprestimos e Financiamentos a Longo Prazo', emprest_fin_l_prazo[0], emprest_fin_l_prazo[1]])

                if fornecedores_cont_pagar_l_prazo[0] == 0 and fornecedores_cont_pagar_l_prazo[1] == 0:
                    fornecedores_cont_pagar_l_prazo = buscaKeyParts(diretorio, file,
                                                                    'Fornecedores e Contas a Pagar a Longo Prazo')
                    print("fornecedores_cont_pagar_l_prazo", fornecedores_cont_pagar_l_prazo)
                    if fornecedores_cont_pagar_l_prazo[0] != 0 or fornecedores_cont_pagar_l_prazo[1] != 0:
                        balpat_writer.writerow(
                            ['Fornecedores e Contas a Pagar a Longo Prazo', fornecedores_cont_pagar_l_prazo[0],
                             fornecedores_cont_pagar_l_prazo[1]])

                if obrig_fiscais_l_prazo[0] == 0 and obrig_fiscais_l_prazo[1] == 0:
                    obrig_fiscais_l_prazo = buscaKeyParts(diretorio, file, 'Obrigacoes Fiscais a Longo Prazo')
                    print("obrig_fiscais_l_prazo", obrig_fiscais_l_prazo)
                    if obrig_fiscais_l_prazo[0] != 0 or obrig_fiscais_l_prazo[1] != 0:
                        balpat_writer.writerow(
                            ['Obrigacoes Fiscais a Longo Prazo', obrig_fiscais_l_prazo[0], obrig_fiscais_l_prazo[1]])

                if provisoes_l_prazo[0] == 0 and provisoes_l_prazo[1] == 0:
                    provisoes_l_prazo = buscaKeyParts(diretorio, file, 'Provisoes a Longo Prazo')
                    print("provisoes_l_prazo", provisoes_l_prazo)
                    if provisoes_l_prazo[0] != 0 or provisoes_l_prazo[1] != 0:
                        balpat_writer.writerow(['Provisoes a Longo Prazo', provisoes_l_prazo[0], provisoes_l_prazo[1]])

                if demais_obrig_l_prazo[0] == 0 and demais_obrig_l_prazo[1] == 0:
                    demais_obrig_l_prazo = buscaKeyParts(diretorio, file, 'Demais Obrigacoes a Longo Prazo')
                    print("demais_obrig_l_prazo", demais_obrig_l_prazo)
                    if demais_obrig_l_prazo[0] != 0 or demais_obrig_l_prazo[1] != 0:
                        balpat_writer.writerow(
                            ['Demais Obrigacoes a Longo Prazo', demais_obrig_l_prazo[0], demais_obrig_l_prazo[1]])

                if result_difer[0] == 0 and result_difer[1] == 0:
                    result_difer = buscaKeyParts(diretorio, file, 'Resultado Diferido')
                    print("result_difer", result_difer)
                    if result_difer[0] != 0 or result_difer[1] != 0:
                        balpat_writer.writerow(['Resultado Diferido', result_difer[0], result_difer[1]])

                if total_passivo_n_circulante[0] == 0 and total_passivo_n_circulante[1] == 0:
                    total_passivo_n_circulante = buscaKeyParts(diretorio, file, 'TOTAL DO PASSIVO NAO CIRCULANTE')
                    print("total_passivo_n_circulante", total_passivo_n_circulante)
                    if total_passivo_n_circulante[0] != 0 or total_passivo_n_circulante[1] != 0:
                        balpat_writer.writerow(['TOTAL DO PASSIVO NAO CIRCULANTE', total_passivo_n_circulante[0],
                                                total_passivo_n_circulante[1]])

                if patrimonio_liquido[0] == 0 and patrimonio_liquido[1] == 0:
                    patrimonio_liquido = buscaKeyParts(diretorio, file, 'PATRIMONIO LIQUIDO')
                    print("patrimonio_liquido", patrimonio_liquido)
                    if patrimonio_liquido[0] != 0 or patrimonio_liquido[1] != 0:
                        balpat_writer.writerow(['PATRIMONIO LIQUIDO', patrimonio_liquido[0], patrimonio_liquido[1]])

                if patrimonio_social_cap_social[0] == 0 and patrimonio_social_cap_social[1] == 0:
                    patrimonio_social_cap_social = buscaKeyParts(diretorio, file, 'PATRIMONIO SOCIAL E CAPITAL SOCIAL')
                    print("patrimonio_social_cap_social", patrimonio_social_cap_social)
                    if patrimonio_social_cap_social[0] != 0 or patrimonio_social_cap_social[1] != 0:
                        balpat_writer.writerow(['PATRIMONIO SOCIAL E CAPITAL SOCIAL', patrimonio_social_cap_social[0],
                                                patrimonio_social_cap_social[1]])

                if adiantamento_fut_aum_cap[0] == 0 and adiantamento_fut_aum_cap[1] == 0:
                    adiantamento_fut_aum_cap = buscaKeyParts(diretorio, file, 'ADIANTAMENTO PARA FUTURO AUMENTO DE CAPITAL')
                    print("adiantamento_fut_aum_cap", adiantamento_fut_aum_cap)
                    if adiantamento_fut_aum_cap[0] != 0 or adiantamento_fut_aum_cap[1] != 0:
                        balpat_writer.writerow(['ADIANTAMENTO PARA FUTURO AUMENTO DE CAPITAL', adiantamento_fut_aum_cap[0],
                                                adiantamento_fut_aum_cap[1]])

                if reservas_capital[0] == 0 and reservas_capital[1] == 0:
                    reservas_capital = buscaKeyParts(diretorio, file, 'RESERVAS DE CAPITAL')
                    print("reservas_capital", reservas_capital)
                    if reservas_capital[0] != 0 or reservas_capital[1] != 0:
                        balpat_writer.writerow(['RESERVAS DE CAPITAL', reservas_capital[0], reservas_capital[1]])

                if ajustes_aval_patrim[0] == 0 and ajustes_aval_patrim[1] == 0:
                    ajustes_aval_patrim = buscaKeyParts(diretorio, file, 'AJUSTES DE AVALIACAO PATRIMONIAL')
                    print("ajustes_aval_patrim", ajustes_aval_patrim)
                    if ajustes_aval_patrim[0] != 0 or ajustes_aval_patrim[1] != 0:
                        balpat_writer.writerow(
                            ['AJUSTES DE AVALIACAO PATRIMONIAL', ajustes_aval_patrim[0], ajustes_aval_patrim[1]])

                if reservas_lucros[0] == 0 and reservas_lucros[1] == 0:
                    reservas_lucros = buscaKeyParts(diretorio, file, 'RESERVAS DE LUCROS')
                    print("reservas_lucros", reservas_lucros)
                    if reservas_lucros[0] != 0 or reservas_lucros[1] != 0:
                        balpat_writer.writerow(['RESERVAS DE LUCROS', reservas_lucros[0], reservas_lucros[1]])

                if demais_reservas[0] == 0 and demais_reservas[1] == 0:
                    demais_reservas = buscaKeyParts(diretorio, file, 'DEMAIS RESERVAS')
                    print("demais_reservas", demais_reservas)
                    if demais_reservas[0] != 0 or demais_reservas[1] != 0:
                        balpat_writer.writerow(['DEMAIS RESERVAS', demais_reservas[0], demais_reservas[1]])

                if result_acumulados[0] == 0 and result_acumulados[1] == 0:
                    result_acumulados = buscaKeyParts(diretorio, file, 'RESULTADOS ACUMULADOS')
                    print("result_acumulados", result_acumulados)
                    if result_acumulados[0] != 0 or result_acumulados[1] != 0:
                        balpat_writer.writerow(['RESULTADOS ACUMULADOS', result_acumulados[0], result_acumulados[1]])

                if total_p_l[0] == 0 and total_p_l[1] == 0:
                    total_p_l = buscaKeyParts(diretorio, file, 'TOTAL DO PATRIMONIO LIQUIDO')
                    print("total_p_l", total_p_l)
                    if total_p_l[0] != 0 or total_p_l[1] != 0:
                        balpat_writer.writerow(['TOTAL DO PATRIMONIO LIQUIDO', total_p_l[0], total_p_l[1]])

                if total_passivo_p_l[0] == 0 and total_passivo_p_l[1] == 0:
                    total_passivo_p_l = buscaKeyParts(diretorio, file, 'TOTAL DO PASSIVO E DO PATRIMONIO LIQUIDO')
                    print("total_passivo_p_l", total_passivo_p_l)
                    if total_passivo_p_l[0] != 0 or total_passivo_p_l[1] != 0:
                        balpat_writer.writerow(
                            ['TOTAL DO PASSIVO E DO PATRIMONIO LIQUIDO', total_passivo_p_l[0], total_passivo_p_l[1]])

                if ativo_financeiro[0] == 0 and ativo_financeiro[1] == 0:
                    ativo_financeiro = buscaKeyParts(diretorio, file, 'ATIVO FINANCEIRO')
                    print("ativo_financeiro", ativo_financeiro)
                    if ativo_financeiro[0] != 0 or ativo_financeiro[1] != 0:
                        balpat_writer.writerow(['ATIVO FINANCEIRO', ativo_financeiro[0], ativo_financeiro[1]])

                if ativo_permanente[0] == 0 and ativo_permanente[1] == 0:
                    ativo_permanente = buscaKeyParts(diretorio, file, 'ATIVO PERMANENTE')
                    print("ativo_permanente", ativo_permanente)
                    if ativo_permanente[0] != 0 or ativo_permanente[1] != 0:
                        balpat_writer.writerow(['ATIVO PERMANENTE', ativo_permanente[0], ativo_permanente[1]])

                if passivo_financeiro[0] == 0 and passivo_financeiro[1] == 0:
                    passivo_financeiro = buscaKeyParts(diretorio, file, 'PASSIVO FINANCEIRO')
                    print("passivo_financeiro", passivo_financeiro)
                    if passivo_financeiro[0] != 0 or passivo_financeiro[1] != 0:
                        balpat_writer.writerow(['PASSIVO FINANCEIRO', passivo_financeiro[0], passivo_financeiro[1]])

                if passivo_permanente[0] == 0 and passivo_permanente[1] == 0:
                    passivo_permanente = buscaKeyParts(diretorio, file, 'PASSIVO PERMANENTE')
                    print("ativo_permanente", passivo_permanente)
                    if passivo_permanente[0] != 0 or passivo_permanente[1] != 0:
                        balpat_writer.writerow(['PASSIVO PERMANENTE', passivo_permanente[0], passivo_permanente[1]])


if __name__ == "__main__":
    main()
