import os

def data_index(path):
    files=os.listdir(path)
    #balpatpath = path + "\\" + tipo
    x1 = 0
    y1 = 0
    for file in files:
        if file.endswith('.txt'):
            x1 = x1 + 1
            x2 = 0
            f = open(path+"\\"+file, "r", encoding="utf8", errors='ignore')
            f1 = f.readlines()
            index = file.split("_")
            for x in f1:
                if x.find("Procedência") != -1:
                    output = open(path + "\\" + "index.txt", "a")
                    output.write(index[0] + "  " + x)
                    y1 = y1 + 1
                    x2 = 1
            if x2 == 0:
                print(file)

    print(x1, " ", y1)


path = r"C:\Users\schmall\Documents\FGV\Tese\Balanços_PI\CAPA"

data_index(path)