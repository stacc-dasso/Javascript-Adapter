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


def parse_price(xpath_output):
    return xpath_output.strip()[1:]


def parse_item_id(xpath_output):
    return re.search("/product/(\d+?)/form_key/", xpath_output).group(1)


class MagentoItem(Item):
    name = Field()
    timestamp = Field()
    currency = Field(input_processor=MapCompose(parse_currency))
    price = Field(input_processor=MapCompose(parse_price))
    shop_id = Field()
    item_id = Field(input_processor=MapCompose(parse_item_id))
