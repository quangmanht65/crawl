# items.py
import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

""" Dùng với ItemLoader """
# remove dots
def remove_dot(value):
    return value.replace('.', '')

# strip spaces in header
def remove_space(value):
    return value.strip()

class ShopeeProduct(scrapy.Item):
    title = scrapy.Field(input_processor = MapCompose(remove_tags, remove_space), output_processor = TakeFirst())
    price = scrapy.Field(remove_tags, remove_dot, output_processor = TakeFirst())

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    price_sale = scrapy.Field()
    sold = scrapy.Field()