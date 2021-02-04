from Download_pdf import DownloaderBot # Importa a classe que criei com o metodo para fazer os downloads
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os.path
import pdb

def main():
    downloader = DownloaderBot(url="https://www.tce.pi.gov.br/fiscalizado/pesquisa-de-processos/")
    downloader.downloaderTcePiaui()
    
    print("Exit 0")
    
if __name__ == '__main__':
    main()


