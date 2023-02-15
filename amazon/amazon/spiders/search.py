import scrapy


class SearchSpider(scrapy.Spider):
    name = "search"
    allowed_domains = ["www.amazon.in"]
    start_urls = ["http://www.amazon.in/"]

    def parse(self, response):
        yield {
            "Content": response
        }
