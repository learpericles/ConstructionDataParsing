import json
import codecs


class ConstructionCrawlerPipeline(object):
    def __init__(self):
        self.file = codecs.open('urls.json', 'w', encoding='utf-8') #a for addition a new data
        self.file.write("[")

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.write("]")
        self.file.close()

