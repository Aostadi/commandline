import scrapy
from pymongo import MongoClient


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com"]

    def __init__(self, *args, **kwargs):
        super(ExampleSpider, self).__init__(*args, **kwargs)
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.example_database
        self.collection = self.db.example_collection

    def parse(self, response):
        for item in response.css('div.item'):
            data = {
                "title": item.css('h1::text').get(),
                "description": item.css('p.description::text').get(),
            }
            self.collection.insert_one(data)
            yield data

        # پیمایش به صفحات دیگر
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
