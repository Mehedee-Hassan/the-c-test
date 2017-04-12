import multiprocessing as mp
import time

from scrapy import signals
from scrapy.crawler import CrawlerProcess, Crawler
from webscrapping.test1.spider.datablogger import DatabloggerSpider





class CustomCrawler(object):

    def crawl(self, spider):
        crawled_items = []

        def add_item(item):
            crawled_items.append(item)

        process = CrawlerProcess()

        crawler = Crawler(spider, self.settings)
        crawler.signals.connect(add_item, signals.item_scraped)
        process.crawl(crawler)

        process.start()

        return crawled_items





def crawl():
    def _crawl(queue):
        crawler = CustomCrawler()
        # Assume we have a spider class called: WebSpider
        res = crawler.crawl(DatabloggerSpider)
        queue.put(res)

    q = mp.Queue()
    p = mp.Process(target=_crawl, args=(q))
    p.start()
    res = q.get()
    p.join()

    return res







while True:

    items = crawl()
    print (items)


    time.sleep(3600)

    if len(items) == 0:
        break

