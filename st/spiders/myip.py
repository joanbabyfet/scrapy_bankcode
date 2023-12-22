import scrapy


class MyipSpider(scrapy.Spider):
    name = "myip"
    allowed_domains = ["httpbin.org"]
    start_urls = ["https://httpbin.org/ip"]

    def parse(self, response):
        print(response.text)
        pass
