import scrapy


class NewsArticle(scrapy.Item):
    url = scrapy.Field()
    source = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
