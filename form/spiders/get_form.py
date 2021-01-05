import scrapy


def generate_start_urls():
    names = ['Alice', 'Bob', 'Charles']
    quests = ['to seek the grail', 'to learn Python', 'to scrape the web']
    return [
        f'https://pythonscraping.com/linkedin/formAction.php?name={names[i]}&quest={quests[i]}&color=blue'
        for i in range(len(names))
    ]


class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['pythonscraping.com']
    start_urls = generate_start_urls()

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
