from scrapy import cmdline


# 执行爬虫
cmdline.execute('scrapy crawl bankcode --nolog'.split())