from scrapy.item import Item,Field
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
import json

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings



class MyItem(Item):

    title=Field()
    content = Field()
    url = Field()




class MySpider(BaseSpider):
    """Tfile:/D:/google_drive/MSc%20Research/implement/nlp%20python/classification/classification1/_test_scrapy1/test1/Main.pyhis spider crawls the website example.com."""
    # The name is the unique identifier for this spider.
    name = 'myspider'
    # These URLs are the initial requests performed by the spider.
    start_urls = [
        'http://www.thedailystar.net/'
    ]

    # The default callback for the start urls is `parse`.
    # This method must return either items or requests.
    def parse(self, response):
        # Instance selector in order to query the html document.
        sel = Selector(response)
        # Instance our item. The item class have a dict-like interface.
        item = MyItem()
        # The method `extract()` always returns a list. So we extract the
        # first value with [0]. This is not needed when using the item loaders.
        # We can use a XPath rule to extract information from the html.
        item['title'] = sel.xpath('//h1/text()').extract()[0]
        # Or we can use a CSS expression as well.
        item['content'] = sel.css('p::text').extract()[0]
        item['url'] = response.url
        # Finally return the scraped item.
        return item





class MyPipeline(object):
    def process_item(self, item, spider):
        results.append(dict(item))

results = []
def spider_closed(spider):
    print( results)

# set up spider
spider = MySpider(domain='http://www.thedailystar.net/')

# set up settings
settings = get_project_settings()
settings.overrides['ITEM_PIPELINES'] = {'__main__.MyPipeline': 1}
settings.overrides['FEED_FORMAT'] = 'json'
settings.overrides['FEED_URI'] = 'result.json'


# set up crawler
crawler = Crawler(settings)
crawler.signals.connect(spider_closed, signal=signals.spider_closed)
crawler.configure()


crawler.crawl(spider)

# start crawling
crawler.start()
log.start()
reactor.run()