import scrapy
from ..items import CompItem
from .mytools import rm_space, take_2nd, take_1st
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(name)s] %(levelname)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='all_log_info.log')

logger = logging.getLogger('comp_logger')

class InfosSpider(scrapy.Spider):
    name = "companies"
    page = 2  # for pagination
    start_urls = [
        'https://datacvr.virk.dk/data/visninger?soeg=&oprettet=null&ophoert=null&branche=&type=undefined&language=da'
    ]

    def parse(self, response):
        logger.info('Parse function called on %s', response.url)
        for comp_page in response.css('.virk a::attr(href)').getall():
            if comp_page is not None:
                response.follow(comp_page, callback=self.parse_data)

        next_page = "https://datacvr.virk.dk/data/visninger?page=" + str(InfosSpider.page) + "&branche=&language=da&ophoert=null&oprettet=null&soeg=&type=undefined"
        print(next_page)
        if InfosSpider.page < 103:
            InfosSpider.page += 1
            yield response.follow(next_page, callback=self.parse)

    def parse_data(self, response):
        c_name = response.css('h1.enhedsnavn::text').get()

        c_item = CompItem()

        c_item['comp_name'] = c_name
        c_item['cvr_number'] = rm_space(response.css('.stamdata .cvrreg::text').get())
        c_item['address'] = rm_space(response.css('.stamdata .dataraekker:nth-child(2) .datatitler+ .col-sm-6::text').get())
        c_item['postal_code'] = take_1st(response.css('.stamdata .dataraekker:nth-child(3) .datatitler+ .col-sm-6::text').get())
        c_item['city'] = take_2nd(response.css('.stamdata .dataraekker:nth-child(3) .datatitler+ .col-sm-6::text').get())
        c_item['business_type'] = rm_space(response.css('.stamdata .dataraekker:nth-child(5) .datatitler+ .col-sm-6::text').get())
        c_item['advert_protection'] = take_1st(response.css('.stamdata .dataraekker:nth-child(6) .datatitler+ .col-sm-6::text').get())
        c_item['status'] = rm_space(response.css('.stamdata .dataraekker:nth-child(7) .datatitler+ .col-sm-6::text').get())

        yield c_item
