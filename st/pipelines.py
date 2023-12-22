# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter
from scrapy.exporters import CsvItemExporter

class JsonStPipeline:
    def __init__(self):
        #scrapy导出器
        self.file = open('bankcode.json', 'wb') # 这里得用byte类型数据
        self.exporter = JsonLinesItemExporter(self.file, ensure_ascii=False, encoding='utf-8') # 导出json

    def open_spider(self, spider):
        print('执行 open_spider 函数')

    # 接收spider扔过来的dict, 该方法默认生成
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    def close_spider(self, spider):
        self.file.close()
        print('执行 close_spider 函数')

class CsvStPipeline:
    def __init__(self):
        #scrapy导出器
        self.file = open('bankcode.csv', 'wb') # 这里得用byte类型数据
        self.exporter = CsvItemExporter(self.file, encoding='big5') # 导出csv

    def open_spider(self, spider):
        print('执行 open_spider 函数')

    # 接收spider扔过来的dict, 该方法默认生成
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    def close_spider(self, spider):
        self.file.close()
        print('执行 close_spider 函数')
