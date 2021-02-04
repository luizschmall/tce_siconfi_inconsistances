from download_pdf import DownloaderBot  # Importa a classe que criei com o metodo para fazer os downloads


def main():
    downloader = DownloaderBot(url="http://dados.tce.rs.gov.br/dados/municipal/recebimentos/2018.html")
    downloader.downloaderTceRS()

    print("Exit 0")


if __name__ == '__main__':
    main()


