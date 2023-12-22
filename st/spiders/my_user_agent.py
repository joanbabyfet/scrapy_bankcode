import scrapy


class MyUserAgentSpider(scrapy.Spider):
    name = "my_user_agent"
    allowed_domains = ["httpbin.org"]
    start_urls = ["https://httpbin.org/user-agent"]

    def parse(self, response):
        print(response.text)
        pass
