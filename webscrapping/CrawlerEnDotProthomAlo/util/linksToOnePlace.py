import os

def main():

    __path = "J:/thenewage/ncrime/all/New folder/dailystar"
    __file_extension = ".txt"
    __fileToWrite_name = "__OneFile_on_new_line4.txt"

    files = os.listdir(__path)

    linkAdded = []


    fileToWrite = open(__path+"/"+__fileToWrite_name,"w")


    for file_name in files :

        if __file_extension in file_name:
            with open(__path+"/"+file_name,"r") as f:
                for link_as_line in f:
                    if link_as_line not in linkAdded:
                        if "http" in link_as_line or "www" in link_as_line:
                            print(file_name)
                            fileToWrite.write(link_as_line)
                            linkAdded.append(link_as_line)


    fileToWrite.close()



if __name__=="__main__":
  main()