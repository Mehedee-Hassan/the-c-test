from scrapy import signals
from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.settings import Settings
import multiprocessing as mp

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





def crawl ():
    def _crawl(queue):
        crawler = CustomCrawler()
        res = crawler.crawl(WebSpider)
        queue.put(res)


    q.mp.Queue()
    process = mp.Process(target=_crawl ,args(q))
    process.start()

    res = q.get()
    p.join()


    return res




