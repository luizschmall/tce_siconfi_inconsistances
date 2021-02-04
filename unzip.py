import zipfile
import os

def un_zipfiles(path, tipo):
    files=os.listdir(path)
    balpatpath = path + "\\" + tipo
    for file in files:
        if file.endswith('.zip'):
            filePath=path+"\\"+file
            zip_file = zipfile.ZipFile(filePath)
            id_file = file.split("_")
            x = 0
            for names in zip_file.namelist():
                if (names.find(tipo) != -1):
                    zip_file.extract(names,balpatpath)
                    os.rename(balpatpath+"\\"+names, balpatpath+"\\"+id_file[0]+"_"+names)
                    x = 1
            if x == 0:
                print(tipo + " em Zip_file "+id_file[0]+" não existe")
            zip_file.close()


path = r"C:\Users\schmall\Documents\FGV\Tese\Balanços_PI"

un_zipfiles(path, "BALPAT")
un_zipfiles(path, "CAPA")
un_zipfiles(path, "RELRP")
un_zipfiles(path, "DEMFC")
un_zipfiles(path, "DDA")
un_zipfiles(path, "DEMDF")
un_zipfiles(path, "DEMDFI")
un_zipfiles(path, "DEMVP")
un_zipfiles(path, "COMPDAR")
un_zipfiles(path, "COMPROA")
un_zipfiles(path, "BALORC")
un_zipfiles(path, "BALFIN")
