from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from construction_crawler.items import UrlItem

class LinkSpyder(CrawlSpider):
    name = "link"
    allowed_domains = ["monitoring.rosfirm.ru"]
    start_urls = ["http://monitoring.rosfirm.ru"]

    extractor = LinkExtractor(allow=(), unique=True)
    #rules = (Rule(extractor, callback='parse_item'),)

    def parse(self, response):
        links = self.extractor.extract_links(response)
        links = response.xpath('//a[contains(@href, "chart")]/@href').extract()
        for link in links:
            link = link.replace("chart", "table")
            item = UrlItem()
            item["url"] = link
            yield item
