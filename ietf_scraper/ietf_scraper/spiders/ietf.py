import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        css_title = response.css('span.title::text').get()
        xpath_title = response.xpath('//span[@class="title"]/text()').get()
        return {'css_title': css_title, 'xpath_title': xpath_title}
