# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import time

from scrapy import Item, Field


class MagentoItem(Item):
    name = Field()
    timestamp = str(int(time.time()))
    currency = Field()
    price = Field()
    shop_id = "magento"
    item_id = Field()

