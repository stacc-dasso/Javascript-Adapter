# -*- coding: utf-8 -*-
import re

from scrapy import Item, Field
from scrapy.loader.processors import MapCompose


def parse_currency(xpath_output):
    xpath_output = xpath_output.strip()
    if "€" in xpath_output:
        return "euro"
    elif "$" in xpath_output:
        return "dollar"
    return xpath_output[0]


class MagentoItem(Item):
    name = Field()
    timestamp = Field()
    currency = Field(input_processor=MapCompose(parse_currency))
    price = Field(input_processor=MapCompose(lambda x: x.strip()[1:]))
    shop_id = Field()
    item_id = Field(input_processor=MapCompose(lambda x: re.search("/product/(\d+?)/form_key/", x).group(1)))
