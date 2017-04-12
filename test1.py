import os,re

class Test:
    a = 0
    t = "this is empty"

    def __init__(self,a,t):
        self.a = a
        self.t = t


    def split_text(self,text):
        words = re.split("[^\wÃ¤Ã¶Ã¼Ã„Ã–ÃœÃŸ]*",text)
        return words


def main():
    test = Test(1,"a")

    print(test.a)

    temp = test
    temp.a = 11


    print(test.a)

    words = test.split_text("this,is A text.M.B.A")

    for w in words:
        print(w+" ")



main()