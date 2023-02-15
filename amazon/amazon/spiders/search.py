import scrapy
from scrapy_selenium import SeleniumRequest

class SearchSpider(scrapy.Spider):
    name = "search"
    # allowed_domains = ["www.amazon.in"]
    # start_urls = ["http://www.amazon.in/"]

    def start_requests(self):
        yield SeleniumRequest(
            url= "https://www.amazon.in/",
            callback= self.parse
        )

    def parse(self, response):
        yield {
            "Content": response
        }
