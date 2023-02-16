import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchSpider(scrapy.Spider):
    name = "search"

    def start_requests(self):
        yield SeleniumRequest(
            url= "https://www.amazon.in/",
            callback= self.parse
        )

    def parse(self, response):
        yield {
            "Content": response
        }
