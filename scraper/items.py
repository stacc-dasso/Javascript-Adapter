# -*- coding: utf-8 -*-

from scrapy import Item, Field


class MagentoItem(Item):
    name = Field()
    timestamp = Field()
    currency = Field()
    price = Field()
    shop_id = Field()
    item_id = Field()
