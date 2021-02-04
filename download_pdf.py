from bs4 import BeautifulSoup
from selenium import webdriver
import requests

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

class DownloaderBot():

    def __init__(self, url):

        self.__url = url  # Atributo privado que recebe a url contendo a lista de links de PDF para download
        print("Downloader object initialezed!")

    def set_url(self, value):
        self.__url = value

    def get_url(self):
        return self.__url

    def downloaderTceRS(self):
        # pdb.set_trace()

        cont = 0

        driver = webdriver.Chrome()
        driver.get("http://dados.tce.rs.gov.br/dados/municipal/recebimentos/2018.html")

        page_source = driver.page_source

        print(page_source)

        soup = BeautifulSoup(page_source, "html.parser")

        print(soup)

        driver.quit()

        x2 = 0

        for link in soup.findAll("a"):
            print(link.get('href'))

            if link.get("href").find("dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2018/") > 0:
                if link.get("href").find(".csv") > 0:
                    save_path = r"C:\Users\schmall\Documents\FGV\Tese\Balanços_RS\dados - despesas - 2018\\" + link.get('href').split('/')[7]

                    download_url(link.get('href'), save_path, chunk_size=128)

        #             options = webdriver.ChromeOptions()
        #
        #             preferences = {
        #                 "download.default_directory": r"C:\Users\schmall\Documents\FGV\Tese\Balanços_RS\dados",
        #                 "download.prompt_for_download": False,
        #                 "download.directory_upgrade": True
        #             }
        #             options.add_experimental_option("prefs", preferences)
        #
        #             driver3 = webdriver.Chrome(chrome_options=options)
        #             driver3.get(link.get('href'))
        #
        #
        #             time.sleep(5)
        #
        #             url_do_pdf = driver3.current_url  # pega a URL do PDF, que é o que queríamos desde o inicio!
        #
        #             print(url_do_pdf)
        #
        #             x1 = 0
        #             x2 = x2 + 1
        #             if x2 > 5:
        #                 while x1 == 0:
        #                     count = 0
        #                     li = os.listdir(r"C:\Users\schmall\Documents\FGV\Tese\Balanços_RS\dados")
        #                     for x1 in li:
        #                         if x1.endswith(".crdownload"):
        #                             count = count + 1
        #                     if count == 0:
        #                         x1 = 1
        #                         x2 = 0
        #                     else:
        #                         x1 = 0
        #                 driver3.quit()
        #
        # # testa botao proximo APÓS baixar todos os PDFs da primeira página!
        # pagina_exibe_links_pdf_driver = webdriver.Chrome()
        # pagina_exibe_links_pdf_driver.get(self.__url)
        #
        # try:
        #     botao_proximo = pagina_exibe_links_pdf_driver.find_element_by_link_text("Próximo →")
        #     # Necessidade de fazer downloads nas próximas páginas
        #     botao_proximo.click()
        #     proxima_pagina = pagina_exibe_links_pdf_driver.current_url
        #     self.__url = proxima_pagina  # Atualiza a página do link dos downloads no objeto!
        #     pagina_exibe_links_pdf_driver.quit()  # Pode fechar o driver, pois já temos a proxima página para reiniciar o loop!
        # except NoSuchElementException as exception:  # Atingiu a última página da navegação! Acabou o trabalho!
        #     proxima_pagina_existe = False  # Não entrará na próxima iteração do loop!
