import scrapy


class MyHeadersSpider(scrapy.Spider):
    name = "my_headers"
    allowed_domains = ["httpbin.org"]
    start_urls = ["https://httpbin.org/headers"]

    def parse(self, response):
        print(response.text)
        pass
