

import newspaper
import threading
from webscrapping.static_crawler.newspaper_lib_modify import modified_datePicker

def writeInThread(__filename, contentHtml, g_url):
    print(__filename)

    newsArticle = newspaper.Article(url="")
    newsArticle.set_html(contentHtml)

    newsArticle.parse()

    # __path = "J:/___testdata_not_crime_sure4_utf8"
    __path = "J:/___accident_not_crime_data/"

    date_text = newsArticle.publish_date


    print(date_text)


    text = str(date_text)
    text = text + "\n" + (newsArticle.title)
    text = text + "\n" + (newsArticle.text)


    __filename = __path+"/" + str(__filename) + ".txt"

    print(__filename)
    file = open(str(__filename), 'w+',encoding="UTF8")
    file.write(text)
    file.close()
    print("--done--")


def writeFile(contentHtml, __filename,url=""):
    print("===writefile===")


    t = threading.Thread(target=writeInThread ,args=(__filename,contentHtml,url))
    t.start()

























