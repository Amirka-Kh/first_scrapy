# c_item = ItemLoader(item=CompItem(), selector=response)
#
# c_item.add_value('comp_name', c_name)
# c_item.add_css('cvr_number', '.stamdata .cvrreg::text')
# c_item.add_css('address', '.stamdata .dataraekker:nth-child(2) .datatitler+ .col-sm-6::text')
# c_item.add_css('postal_code', '.stamdata .dataraekker:nth-child(3) .datatitler+ .col-sm-6::text')
# c_item.add_css('city', '.stamdata .dataraekker:nth-child(3) .datatitler+ .col-sm-6::text')
# c_item.add_css('business_type', '.stamdata .dataraekker:nth-child(5) .datatitler+ .col-sm-6::text')
# c_item.add_css('advert_protection', '.stamdata .dataraekker:nth-child(6) .datatitler+ .col-sm-6::text')
# c_item.add_css('status', '.stamdata .dataraekker:nth-child(7) .datatitler+ .col-sm-6::text')
#
# yield c_item.load_item()


# comp_name = scrapy.Field(input_processor=Identity())
# cvr_number = scrapy.Field(input_processor=MapCompose(rm_space), output_processor=TakeFirst())
# address = scrapy.Field(input_processor=MapCompose(rm_space), output_processor=TakeFirst())
# postal_code = scrapy.Field(input_processor=MapCompose(take_1st), output_processor=TakeFirst())
# city = scrapy.Field(input_processor=MapCompose(take_2nd), output_process=TakeFirst())
# business_type = scrapy.Field(input_processor=MapCompose(rm_space), output_process=TakeFirst())
# advert_protection = scrapy.Field(input_processor=Compose(take_1st), output_process=TakeFirst())
# status = scrapy.Field(input_processor=MapCompose(rm_space), output_process=TakeFirst())


# for logging
# self.logger.info('parse_data function called on %s', response.url)

# def create_dict(value):
#     pwr_to_bnd = rm_space(value.css('.dataraekker:nth-child(1) .col-sm-8'))
#     mngr_sec = value.css('.dataraekker:nth-child(2) .col-sm-8')
#     m_name = mngr_sec.css('br+ a::text')
#     m_addr = mngr_sec.css('br::text')
#     m_postal_city = mngr_sec.css('br::text')
#     m_postal_city = m_postal_city.split(' ')
#     m_postal = m_postal_city[0]
#     m_city = take_2nd(m_postal_city)
#     country = mngr_sec.css('br::text')
#     item = {
#         'pwr_to_bnd': pwr_to_bnd,
#         'm_name': m_name,
#         'm_addr': m_addr,
#         'm_postal': m_postal,
#         'm_city': m_city,
#         'country': country
#     }
#     return item