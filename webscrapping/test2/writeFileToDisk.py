

import  newspaper

def writeFile(coneteHtml,filename):
    newsArticle = newspaper.Article()
    newsArticle.set_html(coneteHtml)

    newsArticle.parse()

    text = newsArticle.publish_date
    text = text+"\n"+newsArticle.title
    text = text+"\n"+newsArticle.text


    file = open(str(filename) ,'w')
    file.write(text)
    file.close()

























