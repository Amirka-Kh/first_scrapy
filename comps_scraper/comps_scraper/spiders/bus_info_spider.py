import scrapy
from ..items import BusItem
from .mytools import rm_space, take_2nd, take_1st
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(name)s] %(levelname)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='all_log_info.log')

logger = logging.getLogger('bus_info_logger')

class BusSpider(scrapy.Spider):
    name = "business"
    page = 2  # for pagination
    start_urls = [
        'https://datacvr.virk.dk/data/visninger?soeg=&oprettet=null&ophoert=null&branche=&type=undefined&language=da'
    ]

    def parse(self, response):
        #logger.info('Parse function called on %s', response.url)
        for comp_page in response.css('.virk a::attr(href)'):
            if comp_page is not None:
                yield response.follow(comp_page, callback=self.parse_data)

        next_page = "https://datacvr.virk.dk/data/visninger?page=" + str(
            BusSpider.page) + "&branche=&language=da&ophoert=null&oprettet=null&soeg=&type=undefined"
        print(next_page)
        if BusSpider.page < 103:
            BusSpider.page += 1
            yield response.follow(next_page, callback=self.parse)

    def parse_data(self, response):
        c_name = response.css('h1.enhedsnavn::text').get()

        bus_info = response.css('#collapse_-Flere-Stamdata .accordion-inner')
        b_item = BusItem()

        b_item['comp_name'] = c_name
        b_item['municipality'] = rm_space(bus_info.css('.dataraekker:nth-child(1) .col-sm-8::text').get())
        b_item['act_code'] = take_1st(bus_info.css('.dataraekker:nth-child(2) .col-sm-8::text').get())
        b_item['act_code_desc'] = take_2nd(bus_info.css('.dataraekker:nth-child(2) .col-sm-8::text').get())
        b_item['objects'] = rm_space(bus_info.css('.dataraekker:nth-child(3) .col-sm-8::text').get())

        yield b_item
