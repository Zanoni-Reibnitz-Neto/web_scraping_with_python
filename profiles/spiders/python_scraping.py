import scrapy


class PythonScrapingSpider(scrapy.Spider):
    name = 'pythonscraping'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/cookies/profile.php']

    def make_requests_from_url(self, url):
        request = super(PythonScrapingSpider, self).make_requests_from_url(url)
        request.cookies['username'] = 'Ryan!!!'
        request.cookies['loggedin'] = 'password'
        return request

    def parse(self, response):
        return {'text': response.xpath('//body/text()').get()}
