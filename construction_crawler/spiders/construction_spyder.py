from scrapy.spiders import CrawlSpider
from construction_crawler.items import TimeSeriesItem
import json

class ConstructionSpyder(CrawlSpider):
    name = "construction"
    DOMAIN = "http://monitoring.rosfirm.ru"
    allowed_domains = ["monitoring.rosfirm.ru"]

    links = []

    with open('urls.json') as json_data:
        d = json.load(json_data)

        for data in d:
            url = DOMAIN + data["url"]
            links.append(url)
            print url

    start_urls = links

    def parse(self, response):
        table = response.css("table.center")
        name = response.css('a[style="font-weight:bold"]::text').extract_first()

        for column in table.xpath("//tr[@valign=$val]", val="top"):
            item = TimeSeriesItem()
            item["name"] = name[1:-1]

            for i, data in enumerate(column.css("td::text").extract()):
                if (i == 0):
                    item["date"] = data.strip()

                if (i == 1):
                    item["value"] = data.strip()

            print item