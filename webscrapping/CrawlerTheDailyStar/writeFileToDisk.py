

import newspaper
import threading
from webscrapping.CrawlerEnDotProthomAlo.newspaper_lib_modify import modified_datePicker





def writeInThread(__filename, contentHtml, g_url):
    print(__filename)
    base_path = "J:/__theDailyStar"

    newsArticle = newspaper.Article(url="")
    newsArticle.set_html(contentHtml)

    newsArticle.parse()


    date_text = newsArticle.publish_date
    if date_text == None:

        date_text = modified_datePicker.get_publishing_date(url="", doc=newsArticle.clean_doc)
        print("date = ", date_text)



    text = str(newsArticle.publish_date)
    text = text + "\n" + (newsArticle.title)
    text = text + "\n" + (newsArticle.text)


    if "/sports/" in g_url:
        __filename = base_path+"/sports/" + str(__filename) + ".txt"
    elif "/country/" in g_url:
        __filename = base_path+"/country/" + str(__filename) + ".txt"
    elif "/world/" in g_url:
        __filename = base_path+"/world/" + str(__filename) + ".txt"
    elif "/lifestyle/" in g_url:
        __filename = base_path+"/lifestyle/" + str(__filename) + ".txt"
    elif "/science/" in g_url:
        __filename = base_path+"/science/" + str(__filename) + ".txt"
    elif "/health/" in g_url:
        __filename = base_path+"/health/" + str(__filename) + ".txt"
    elif "/arts-entertainment/" in g_url:
        __filename = base_path+"/arts-entertainment/" + str(__filename) + ".txt"
    elif "/business/" in g_url:
        __filename = base_path+"/business/" + str(__filename) + ".txt"


    elif "/frontpage/" in g_url:
        __filename = base_path+"/frontpage/" + str(__filename) + ".txt"


    elif "/op-ed/" in g_url:
        __filename = base_path+"/op-ed/" + str(__filename) + ".txt"


    elif "/bytes/" in g_url:
        __filename = base_path+"/bytes/" + str(__filename) + ".txt"


    elif "/backpage/" in g_url:
        __filename = base_path+"/backpage/" + str(__filename) + ".txt"



    elif "/environment/" in g_url:
        __filename = base_path+"/environment/" + str(__filename) + ".txt"


    else:
        __filename = base_path+ "/others/" + str(__filename) + ".txt"

    print(__filename)
    file = open(str(__filename), 'w')
    file.write(text)
    file.close()


def writeFile(contentHtml, __filename,url=""):
    print("===writefile===")


    t = threading.Thread(target=writeInThread ,args=(contentHtml,__filename,url))
    t.start()

























