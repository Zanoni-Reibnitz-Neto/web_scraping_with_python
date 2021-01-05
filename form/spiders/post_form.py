import scrapy
from scrapy.http import FormRequest


class PostFormSpider(scrapy.Spider):
    name = 'post_form'
    allowed_domains = ['pythonscraping.com']

    def start_requests(self):
        names = ['Alice', 'Bob', 'Charles']
        quests = ['to seek the grail', 'to learn Python', 'to scrape the web']
        return [
            FormRequest(
                'http://pythonscraping.com/linkedin/formAction2.php',
                formdata={'name': names[i], 'quest': quests[i], 'color': 'blue'},
                callback=self.parse
            ) for i in range(len(names))
        ]

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
