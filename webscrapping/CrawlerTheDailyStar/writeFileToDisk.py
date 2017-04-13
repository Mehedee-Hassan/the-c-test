

import newspaper
import threading
from webscrapping.CrawlerEnDotProthomAlo.newspaper_lib_modify import modified_datePicker

def writeInThread(__filename, contentHtml, g_url):
    print(__filename)

    newsArticle = newspaper.Article(url="")
    newsArticle.set_html(contentHtml)

    newsArticle.parse()


    date_text = newsArticle.publish_date
    if date_text == None:

        date_text = modified_datePicker.get_publishing_date(url="", doc=newsArticle.clean_doc)
        print("date = ", date_text)



    text = str(date_text)
    text = text + "\n" + (newsArticle.title)
    text = text + "\n" + (newsArticle.text)


    if "/sports/" in g_url:
        __filename = "J:/___testdata/sports/" + str(__filename) + ".txt"
    elif "/bangladesh/" in g_url:
        __filename = "J:/___testdata/bangladesh/" + str(__filename) + ".txt"

    elif "/international/" in g_url:
        __filename = "J:/___testdata/international/" + str(__filename) + ".txt"
    elif "/economy/" in g_url:
        __filename = "J:/___testdata/economy/" + str(__filename) + ".txt"
    elif "/entertainment/" in g_url:
        __filename = "J:/___testdata/entertainment/" + str(__filename) + ".txt"
    elif "/lifestyle/" in g_url:
        __filename = "J:/___testdata/lifestyle/" + str(__filename) + ".txt"
    elif "/science-technology/" in g_url:
        __filename = "J:/___testdata/science-technology/" + str(__filename) + ".txt"
    elif "/youth/" in g_url:
        __filename = "J:/___testdata/youth/" + str(__filename) + ".txt"
    else:
        __filename = "J:/___testdata/others/" + str(__filename) + ".txt"

    print(__filename)
    file = open(str(__filename), 'w')
    file.write(text)
    file.close()


def writeFile(contentHtml, __filename,url=""):
    print("===writefile===")


    t = threading.Thread(target=writeInThread ,args=(contentHtml,__filename,url))
    t.start()

























