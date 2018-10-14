import re

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
    start_urls = ["http://local.magento/"]

    rules = [
        #TODO: Setup rule for link redirect
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pager fl']/a"), follow=True, callback="parse_info")
    ]

    # def parse(self, response):
    #     hxs = HtmlXPathSelector(response)
    #
    #     loader = MagentoLoader(MagentoItem(), hxs)
    #     loader.add_xpath('name', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[1]/div/h3/a')
    #     loader.add_xpath('price', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[1]/div/div[1]/span/span')
    #     return loader.load_item()

    def parse_info(self, response):
        products = Selector(response).xpath("//div[@class='widget-products']")

        for product in products:
            item = MagentoItem()
            item['name'] = product.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            item['price'] = product.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
