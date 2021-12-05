from itemadapter import ItemAdapter
from .items import BusItem, CompItem
import pymongo

class CompsScraperPipeline:
    def __init__(self, mongo_uri='mongodb://localhost:27017/', mongo_db='comps_data'):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, BusItem):
            return self.handleHisBusiness(item, spider)
        self.db.comp_info.insert_one(ItemAdapter(item).asdict())
        return item

    def handleHisBusiness(self, item, spider):
        self.db.bus_info.insert_one(ItemAdapter(item).asdict())
        return item



