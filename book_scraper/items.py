# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    
    Name = scrapy.Field()
    URL = scrapy.Field()
    Price = scrapy.Field()
    Available_books = scrapy.Field()
    Product_description = scrapy.Field()
    Upc = scrapy.Field()