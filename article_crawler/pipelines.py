from datetime import datetime

from scrapy.exceptions import DropItem

from article_crawler.items import Article


class CheckItemPipeline:
    def process_item(self, article: Article, spider):
        if not article['title'] or not article['url'] or not article['last_updated']:
            raise DropItem('Missing at least one field')
        return article


class CleanDatePipeline:
    def process_item(self, article: Article, spider):
        last_updated = article['last_updated'].replace('This page was last edited on', '').strip()
        article['last_updated'] = datetime.strptime(last_updated, '%d %B %Y, at %H:%M')
        return article
