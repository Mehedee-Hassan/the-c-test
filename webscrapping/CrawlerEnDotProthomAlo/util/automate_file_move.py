import os, itertools
import filecmp
import re

path = "J:/___testdata/bangladesh"

f1 = os.listdir(path)

files = sorted(f1,  key=lambda x: (int(re.sub('\D','',x)),x))

print(files)


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




    if test == "g":
        p2 = destination+"guess/"+ file
        os.rename(p1, p2)
    elif test == "y":

        p2 = destination + file
        os.rename(p1, p2)
