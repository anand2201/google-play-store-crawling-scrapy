# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy



# class GplaystorecrwlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    pass
#******************From Here*******************
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

#from scrapy.item import Item, Field
import scrapy

class GplaystorecrwlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = Field()
#  count=range(1,11)
#  for c in count: \
    print "__________ik item________"
    Link = scrapy.Field()
    Item_name = scrapy.Field()
    Updated = scrapy.Field()
    Author = scrapy.Field()
    Filesize = scrapy.Field()
    Downloads = scrapy.Field()
    Version = scrapy.Field()
    Compatibility = scrapy.Field()
    Content_rating = scrapy.Field()
    Author_link = scrapy.Field()
##    Author_link_test = scrapy.Field()
    Genre = scrapy.Field()
    Price = scrapy.Field()
    Rating_value = scrapy.Field()
    Review_number = scrapy.Field()
    Description = scrapy.Field()
    IAP = scrapy.Field()
    Developer_badge = scrapy.Field()
    Physical_address = scrapy.Field()
    Video_URL = scrapy.Field()
    Developer_ID = scrapy.Field()
#    if c==5:
#      break

