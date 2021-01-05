from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_crawler.items import Article


class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Kevin_Bacon']

    rules = [
        Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)
    ]

    custom_settings = {
        'FEED_URI': 'articles.xlsx',
        'FEED_FORMAT': 'xlsx'
    }

    def parse_info(self, response):
        return Article(
            title=response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get(),
            url=response.url,
            last_updated=response.xpath('//li[@id="footer-info-lastmod"]/text()').get(),
        )
