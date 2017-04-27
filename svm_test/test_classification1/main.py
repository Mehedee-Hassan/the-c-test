import html
import pprint
import re
from html.parser import HTMLParser
from threading import Thread

import newspaper
import numpy
import sklearn.svm
import os

import sys
from sklearn.feature_extraction.text import TfidfVectorizer,ENGLISH_STOP_WORDS

def read_data(path):
    files = os.listdir(path)

    p1 = path+"/"
    data = []


    for file in files:


        reader = open(p1+file ,"r")

        text = reader.read()

        data.append(text)

        reader.close()

    return data


def read_from_disk_training():

    root_path_current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    root_path_current_dir += "\\data\\"

    data_with_label = []

    print(root_path_current_dir)

    for root, subdirs, files in os.walk(root_path_current_dir):
        print("root = ", root)
        current_subdir  = root.split(os.sep)[-1]

        for file in files:
            path = root_path_current_dir +current_subdir+"\\"+ file

            if current_subdir == "crime":

                # print("s = ", root.split(os.sep)[-1], "f = ", file)

                reader = open(path, "r")

                text = reader.readlines()[1:]
                text = ''.join(text)

                data_with_label.append((text,"crime"))
                reader.close()

            elif current_subdir == "ncrime":
                # print("s = ", root.split(os.sep)[-1], "f = ", file)

                reader = open(path, "r")

                text = reader.readlines()[1:]
                text = ''.join(text)

                data_with_label.append((text,"ncrime"))
                reader.close()



    return data_with_label


def get_custom_stop_words():

    return ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once'
        , 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do'
        , 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am'
        , 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are'
        , 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself'
        , 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had'
        , 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in'
        , 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can'
        , 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only'
        , 'myself', 'which', 'those', 'i', 'after'
        , 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a'
        , 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'

        # location names
        ,'Bangladesh','dhaka','bangladesh','barisal',
            'barguna',            'barisal',            'bhola',            'jhalokati',
            'patuakhali',            'pirojpur',            'chittagong',            'bandarban',
            'brahmanbaria',            'chandpur',            'chittagong',            'comilla',
            'cox\'s bazar',            'feni',            'khagrachhari',            'lakshmipur',
            'noakhali',            'rangamati',            'dhaka',            'faridpur',
            'gazipur',            'gopalganj',            'jamalpur',            'kishoregonj',
            'madaripur',            'manikganj',            'munshiganj',            'mymensingh',
            'narayanganj',            'narsingdi',            'netrakona',            'rajbari',
            'shariatpur',            'sherpur',            'tangail'
            ]




def train(data_to_train):


    my_words = get_custom_stop_words()


    my_stop_words = ENGLISH_STOP_WORDS.union(my_words)


    vectorizer = TfidfVectorizer(min_df=1,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf =True,
                                 stop_words = set(my_stop_words))


    x_data = [text[0] for text in data_to_train]

    # print (data_to_train[0])

    train_x = vectorizer.fit_transform(x_data)
    train_x_label = [label[1] for label in data_to_train]

    svmModel = sklearn.svm.SVC(kernel="linear")

    svmModel.fit(train_x,train_x_label)

    return svmModel,vectorizer


def read_test_file(model,vectorizer):

    root_path_current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    root_path_current_dir += "\\test_data\\test_data\\"

    files = os.listdir(root_path_current_dir)

    test = []
    for file in files:
        p1 = root_path_current_dir+file
        if os.path.isfile(p1):
            print("test file = ",file)

            reader = open(p1,"r")

            text = reader.read()
            test.append(text)

            predict([text], model, vectorizer,file)

            reader.close()


    # return test

    # for t in test:
    #     predict([t],model,vectorizer)


non_crime_data=[]

def predict(data,model,vectorizerTfIdf,file):

    test_x = vectorizerTfIdf.transform(data)
    result = model.predict(test_x)

    if result[0] == 'ncrime':
        non_crime_data.append(str(file))

    print (result)



def download_test():

    _current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

    links = [
        "http://www.thedailystar.net/country/death-buffalos-caused-rotten-grass-sunamganj-haor-1397368"
    ]
    __path = _current_dir+"\\test_data\\test_data\\"

    file_name_incr = 0

    for link in links:
        txt_title = __path+str(file_name_incr) + ".txt"

        print(txt_title)


        reader = open(txt_title,"w+",encoding='UTF8')

        a = newspaper.Article(link)
        a.download()
        a.parse()

        reader.write(a.title+"\n"+a.text)

        reader.close()
        file_name_incr+=1

def Main():


    __path = "/data/crime"

    numpy.set_printoptions(threshold=numpy.nan)
    data_as_array = read_from_disk_training()

    model ,vectorizer =train(data_as_array)

    downalod_thread = Thread(target=download_test,args=())

    # download_test()

    file_read_thread = Thread(target=read_test_file,args=(model,vectorizer))

    downalod_thread.start()
    downalod_thread.join()



    file_read_thread.start()
    file_read_thread.join()

    # data_to_Test = read_test_file()
    print(non_crime_data)


if __name__ == "__main__":
    Main()



