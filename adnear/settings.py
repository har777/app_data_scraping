BOT_NAME = 'adnear'

SPIDER_MODULES = ['adnear.spiders']
NEWSPIDER_MODULE = 'adnear.spiders'


ITEM_PIPELINES = [
  'scrapy_mongodb.MongoDBPipeline',
]

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'adnear'
MONGODB_COLLECTION = 'items'