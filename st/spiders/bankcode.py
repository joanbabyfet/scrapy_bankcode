import scrapy

'''
该爬虫使用代理池中间件后无法获取数据待解决
'''
class BankcodeSpider(scrapy.Spider):
    name = "bankcode"
    allowed_domains = ["twtc.inbegin.com"]
    start_urls = ["https://twtc.inbegin.com/html/ezcatfiles/main/img/img/48397/bank.html"]

    def parse(self, response):
        # 銀行
        for selector in response.xpath("/html/body/table/tbody/tr[3]/td[1]/table/tbody/tr[position()>1]"):
            banks = selector.xpath('./td/text()').getall()
            for bank in banks:
                bank = bank.replace(u'\xa0', u'').replace(u'\r\n', u'').replace(u'\t', u'') # 干掉 \xa0
                if len(bank) == 0: # 值为空则跳过
                    continue
                arr_bank = bank.split('-')
                items = {
                    'code': arr_bank[0],
                    'name': arr_bank[1],
                    'type': '銀行',
                }
                yield items # 相当于1个生成器扔给引擎, 引擎再扔给pipelines.py
        
        #信用合作社
        for selector in response.xpath("/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[position()>1]"):
            credit_unions = selector.xpath('./td/text()').getall()
            for credit_union in credit_unions:
                credit_union = credit_union.replace(u'\xa0', u'').replace(u'\r\n', u'').replace(u'\t', u'') # 干掉 \xa0
                if len(credit_union) == 0: # 值为空则跳过
                    continue
                arr_credit_union = credit_union.split('-')
                items = {
                    'code': arr_credit_union[0],
                    'name': arr_credit_union[1],
                    'type': '信用合作社',
                }
                yield items

        # 農會
        for selector in response.xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[position()>1]"):
            associations = selector.xpath('./td/text()').getall()
            for association in associations:
                association = association.replace(u'\xa0', u'').replace(u'\r\n', u'').replace(u'\t', u'') # 干掉 \xa0
                if len(association) == 0: # 值为空则跳过
                    continue
                arr_association = association.split('-')
                items = {
                    'code': arr_association[0],
                    'name': arr_association[1],
                    'type': '農會',
                }
                yield items
        pass
