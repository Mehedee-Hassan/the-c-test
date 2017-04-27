from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import newspaper
import webscrapping.CrawlerEnDotProthomAlo.writeFileToDisk

import time

newsURL = "/news/"

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):
    __filename_global = 0

    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        # We are looking for the begining of a link. Links normally look
        # like <a href="www.someurl.com"></a>
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # We are grabbing the new URL. We are also adding the
                    # base URL to it. For example:
                    # www.netinstructions.com is the base and
                    # somepage.html is the new URL (a relative URL)
                    #
                    # We combine a relative URL with the base URL to create
                    # an absolute URL like:
                    # www.netinstructions.com/somepage.html


                    # print ("== value ",value)

                    if "http://" in value or "https://" in value or "www." in value:
                        newUrl = value
                    else:
                        newUrl = parse.urljoin(self.baseUrl, value)

                    # print("== new url ", newUrl)
                    # And add it to our collection of links_crime:
                    self.links = self.links + [newUrl]

    # This is a new function that we are creating to get links_crime
    # that our spider() function will call
    def getLinks(self, url):
        self.links = []
        # Remember the base URL which will be important when creating
        # absolute URLs
        self.baseUrl = url
        # Use the urlopen function from the standard Python 3 library
        response = urlopen(url)
        # Make sure that we are looking at HTML and not other things that
        # are floating around on the internet (such as
        # JavaScript files, CSS, or .PDFs for example)

        print("==getlinks", str(response.getheader('Content-Type')))

        if 'text/html' in str(response.getheader('Content-Type')):

            htmlBytes = response.read()

            # Note that feed() handles Strings well, but not bytes
            # (A change from Python 2.x to Python 3.x)

            htmlString = htmlBytes.decode("utf-8")
            # print("html=",htmlBytes)



            self.feed(htmlString)

            # print("links_crime =",self.links_crime)

            return htmlString, self.links

        else:
            return "", []





__filename_global = 0



# And finally here is our spider. It takes in an URL, a word to find,
# and the number of pages to search through before giving up
def spider(url,  maxPages, domain, maxprocess, dontVisist):
    pagesToVisit = [url]
    numberVisited = 0
    foundWord = False
    # The main loop. Create a LinkParser and get all the links_crime on the page.
    # Also search the page for the word or string
    # In our getLinks function we return the web page
    # (this is useful for searching for the word)
    # and we return a set of links_crime from that web page
    # (this is useful for where to go next)

    numberVisited = 0
    visitedPages = []

    while numberVisited < maxPages and pagesToVisit != []:

        numberVisited = numberVisited + 1

        # Start from the beginning of our collection of pages to visit:

        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]

        print("link==", len(pagesToVisit))

        if domain in url and url not in visitedPages and dontVisist not in url:

            try:
                print(numberVisited, "Visiting:", url)
                parser = LinkParser()

                data, links = parser.getLinks(url)
                # print("links_crime=",links_crime)
                # print(data)



                if "/news/" in url and "/bangladesh/" in url:
                    global __filename_global

                    print("here ", __filename_global)
                    __filename_global =__filename_global+ 1

                    webscrapping.CrawlerEnDotProthomAlo.writeFileToDisk.writeFile(__filename_global,data,url)


                else:
                    print("no news")

                # largest amount of links_crime to process at a time
                if len(pagesToVisit) < maxprocess:
                    pagesToVisit = pagesToVisit + links

                    # else:
                    #     pagesToVisit = list(filter(lambda x: "/news/" in x, pagesToVisit))

                    # if data.find(word)>-1:
                    #     foundWord = True
                    #     # Add the pages that we visited to the end of our collection
                    #     # of pages to visit:
                    #
                    #
                    #     print(" **Success!**")

            except:
                print(" **Failed!**")


            visitedPages.append(url)

            # foundWord =False
        else:
            pagesToVisit = list(filter(lambda x: x != url, pagesToVisit))
            pagesToVisit = list (filter (lambda x: "/bangladesh/" in x or "/search/" in x ,pagesToVisit))
            pagesToVisit = list(filter(lambda x: "/gallery/" not in x, pagesToVisit))


        time.sleep(1)

    if foundWord:
        print("The word", "was found at", url)
    else:
        print("Word never found")



list_of_lisnk = [
    "http://en.prothom-alo.com/search/?start=0&q=crime&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=crime&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=crime&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=crime&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=40&q=crime&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=50&q=crime&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=murder&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=murder&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=murder&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=robbery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=robbery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=robbery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=robbery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=abduction&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=abduction&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=abduction&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=rape&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=rape&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=rape&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=rape&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=40&q=rape&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=thief&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=thief&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=thief&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=thief&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=40&q=thief&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=kill&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=kill&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=kill&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=kill&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=40&q=kill&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=bombing&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=bombing&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=bombing&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=bombing&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=bribery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=bribery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=bribery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=bribery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=40&q=bribery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=blackmail&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=blackmail&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=blackmail&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=40&q=blackmail&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=assault&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=assault&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=assault&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=assault&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=40&q=assault&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=assassination&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=corruption&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=corruption&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=30&q=corruption&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=40&q=corruption&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=cybercrime&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=cybercrime&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=drunk+driver&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=drunk+driver&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=espionage&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=forgery&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=fraud&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=fraud&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=genocide&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=hijacking&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=hijacking&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=hijacking&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=kidnapping&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=kidnapping&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=riot&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=smuggling&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=smuggling&page_id=&content=",
        "http://en.prothom-alo.com/search/?start=0&q=terrorism&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=terrorism&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=vandalism&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=vandalism&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=slander&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=slander&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=looting&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=burglary&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=child+abuse&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=child+abuse&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=eve+teasing&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=eve+teasing&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=20&q=eve+teasing&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=domestic+violence&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=domestic+violence&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=embezzlement&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=0&q=homicide&page_id=&content=",
    "http://en.prothom-alo.com/search/?start=10&q=homicide&page_id=&content="
]


for link in list_of_lisnk:

    spider(
        link
        # "http://en.prothom-alo.com/search/?start=0&q=crime+murder&page_id=&content="
           # , "sdf"
           , 500000
           , "http://en.prothom-alo.com"
           , 10000
           ,
           "http://en.prothom-alo.com/photos"
           )

    time.sleep(60)
