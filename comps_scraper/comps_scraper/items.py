import scrapy


class CompItem(scrapy.Item):
    comp_name = scrapy.Field()
    cvr_number = scrapy.Field()
    address = scrapy.Field()
    postal_code = scrapy.Field()
    city = scrapy.Field()
    business_type = scrapy.Field()
    advert_protection = scrapy.Field()
    status = scrapy.Field()


class BusItem(scrapy.Item):
    comp_name = scrapy.Field()
    municipality = scrapy.Field()
    act_code = scrapy.Field()
    act_code_desc = scrapy.Field()
    objects = scrapy.Field()











