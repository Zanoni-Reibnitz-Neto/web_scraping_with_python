class NewsScraperPipeline:
    def process_item(self, item, spider):
        item.author = item.author.replace(', CNN', '')
        # item.text = 
        return item
