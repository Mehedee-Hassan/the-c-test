from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import newspaper
import webscrapping.test2.writeFileToDisk


global filename

newsURL = "/news/"

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):
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
                    # And add it to our collection of links:
                    self.links = self.links + [newUrl]

    # This is a new function that we are creating to get links
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

            # print("links =",self.links)

            return htmlString, self.links

        else:
            return "", []


# And finally here is our spider. It takes in an URL, a word to find,
# and the number of pages to search through before giving up
def spider(url, word, maxPages, domain, maxprocess, dontVisist):
    pagesToVisit = [url]
    numberVisited = 0
    foundWord = False
    # The main loop. Create a LinkParser and get all the links on the page.
    # Also search the page for the word or string
    # In our getLinks function we return the web page
    # (this is useful for searching for the word)
    # and we return a set of links from that web page
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
                # print("links=",links)
                # print(data)



                if newsURL in url:

                    filename += 1
                    webscrapping.test2.writeFileToDisk.writeFile(data,filename)



                # largest amount of links to process at a time
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
            pagesToVisit = list(filter(lambda x: "/gallery/" not in x, pagesToVisit))

    if foundWord:
        print("The word", word, "was found at", url)
    else:
        print("Word never found")



filename  = 0

spider("http://en.prothom-alo.com/"
       , "sdf"
       , 100000
       , "http://en.prothom-alo.com"
       , 10000
       )
