import re
import time

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import XPathItemLoader, ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from scrapy.selector import HtmlXPathSelector, Selector
from scrapy.spiders import CrawlSpider, Rule

from scraper.items import MagentoItem


class MagentoLoader(ItemLoader):
    default_item_class = MagentoItem
    default_input_processor = MapCompose(lambda s: re.sub("\s+", " ", s.strip()))
    default_output_processor = TakeFirst()


class MagentoSpider(CrawlSpider):
    name = "magento"
    allowed_domains = ["local.magento"]
    start_urls = [
        # "http://local.magento/women.html",
        # "http://local.magento/men.html",
        # "http://local.magento/accessories.html",
        # "http://local.magento/home-decor.html",
        # "http://local.magento/sale.html",
        # "http://local.magento/vip.html"
        "http://local.magento/lafayette-convertible-dress.html",
        "http://local.magento/vip/rolls-travel-wallet.html",
        "http://local.magento/sale/home-decor/park-row-throw.html"
    ]

    # rules = [
    #     Rule(LinkExtractor(restrict_xpaths="//div[@class='pager fl']/a"), follow=True, callback="parse_info")
    # ]

    def parse(self, response):
        loader = MagentoLoader(response=response)

        loader.add_xpath("name", "//div[@class='product-essential']//div[@class='product-name']/span/text()")
        loader.add_xpath("currency", "//div[@class='product-essential']//span[@class='regular-price']/span[@class='price']/text() | //p[@class='special-price']/span[@class='price']/text()")
        loader.add_xpath("price", "//div[@class='product-essential']//span[@class='regular-price']/span[@class='price']/text() | //p[@class='special-price']/span[@class='price']/text()")
        loader.add_xpath("item_id", "//div[@class='product-essential']//form/@action")
        loader.add_value("timestamp", str(int(time.time())))
        loader.add_value("shop_id", "magento")
        return loader.load_item()
