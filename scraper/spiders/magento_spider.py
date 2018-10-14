import re
import time

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import XPathItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from scrapy.selector import HtmlXPathSelector, Selector
from scrapy.spiders import CrawlSpider, Rule

from scraper.items import MagentoItem


class MagentoLoader(XPathItemLoader):
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
        item = MagentoItem()
        product = Selector(response).xpath("//div[@class='product-essential']")

        item["name"] = product.xpath("//div[@class='product-name']/span/text()").extract_first()
        item["timestamp"] = str(int(time.time()))
        item["shop_id"] = "magento"

        price = product.xpath("//span[@class='regular-price']/span[@class='price']/text() | //p[@class='special-price']/span[@class='price']/text()").extract_first()
        price = price.strip()
        if "€" in price:
            item["currency"] = "euro"
        elif "$" in price:
            item["currency"] = "dollar"
        else:
            item["currency"] = price[0]
        item["price"] = price[1:]

        item_id = product.xpath("form/@action").extract_first()
        item["item_id"] = re.search("/product/(\d+?)/form_key/", item_id).group(1)
        yield item
