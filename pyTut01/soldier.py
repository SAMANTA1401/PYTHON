# oh soldier Pretified my Folder

# path , dictionary file , format

# def soldier("C://", "harry.txt", "jpg")
import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1

soldier(r"D:\testing", r"C:\Users\lenovo\PycharmProjects\pyTut01\testing.txt",".png")


