# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class AdnearItem(Item):
    #region = Field()
    #rating = Field()
    #rating_number = Field()
    title = Field()
    category = Field()
    pricing = Field()
    rank = Field()
    pass
