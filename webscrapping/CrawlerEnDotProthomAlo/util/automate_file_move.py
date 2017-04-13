import os, itertools
import filecmp


path = "J:/___testdata/bangladesh"

files = os.listdir(path)

destination = "J:/___testdata/_crime/"

for file in files:

    p1 =path+"/"+file
    f  = open(p1,"r")
    c = f.read()
    print("\n####file name :", file)
    print("==============================start file===================================")
    print(c)
    print("================================end file===================================")

    f.close()

    test = input("crime ?Y/N")



    if test == "y":
        p2 = destination + file
        os.rename(p1,p2)

    elif test == "g":
        p2 = destination+"guess/"+ file
        os.rename(p1, p2)
