import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        name = response.xpath('//span[@class="author-name"]/text()').get()
        company = response.xpath('//span[@class="author-company"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        address = response.xpath('//span[@class="address"]/text()').get()
        return {
            'name': name,
            'company': company,
            'date': date,
            'title': title,
            'address': address,
        }
