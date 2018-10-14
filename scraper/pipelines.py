# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class MagentoPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    # TODO 3rd iteration: Save data to MongoDB
    def process_item(self, item, spider):
        if item["item_id"] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
