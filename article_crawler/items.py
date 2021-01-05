import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    last_updated = scrapy.Field()
