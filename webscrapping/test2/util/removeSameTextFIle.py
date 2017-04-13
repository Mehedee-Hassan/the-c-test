import os, itertools
import filecmp

path = "J:/___testdata/lifestyle"
files = os.listdir(path)
a=0
for file1, file2 in itertools.combinations(files, 2):
    a=a+1
    try:
        p1 = path + "/" + file1
        p2 = path + "/" + file2


        test = filecmp.cmp(p1,p2)

        if test:
            os.remove(p2)
            print("removed")
            print(p1, p2)

        if a > 100 :
            print("= ")


    except:
        a =0

        print("exception")
