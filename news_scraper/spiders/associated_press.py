import json

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from news_scraper.items import NewsArticle


class AssociatedPressSpider(CrawlSpider):
    name = 'associated_press'
    allowed_domains = ['apnews.com']
    start_urls = ['http://apnews.com/']
    rules = [Rule(LinkExtractor(allow=r'\/[a-zA-Z0-9]{32}'), callback='parse_item', follow=True)]

    def parse_item(self, response):
        article = NewsArticle()
        # <script data-rh="true">
        article['url'] = response.url
        article['source'] = 'Associated Press'
        jsonData = json.loads(response.xpath('//script[@data-rh="true"]/text()').get())
        article['title'] = jsonData['headline']
        article['description'] = jsonData['description']
        article['date'] = jsonData['datePublished']
        article['author'] = jsonData['author'][0]
        article['text'] = response.xpath('//div[@class="Article"]/p/text()').getall()
        return article
