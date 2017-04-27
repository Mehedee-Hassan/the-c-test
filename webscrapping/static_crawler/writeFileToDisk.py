

import newspaper
import threading
from webscrapping.static_crawler.newspaper_lib_modify import modified_datePicker

def writeInThread(__filename, contentHtml, g_url):
    print(__filename)

    newsArticle = newspaper.Article(url="")
    newsArticle.set_html(contentHtml)

    newsArticle.parse()

    __path = "J:/___testdata_crime_sure2"

    date_text = newsArticle.publish_date


    print(date_text)


    text = str(date_text)
    text = text + "\n" + (newsArticle.title)
    text = text + "\n" + (newsArticle.text)


    __filename = __path+"/" + str(__filename) + ".txt"

    print(__filename)
    file = open(str(__filename), 'w')
    file.write(text)
    file.close()
    print("--done--")


def writeFile(contentHtml, __filename,url=""):
    print("===writefile===")


    t = threading.Thread(target=writeInThread ,args=(contentHtml,__filename,url))
    t.start()

























