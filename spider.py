import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    
    def start_requests(self):
        urls = [
            'http://www.google.fr',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
#            yield scrapy.Request(url=url, callback=self.parse, meta={'proxy': 'https://localhost:3128'}) # proxy can be added here or as a middleware
    
    def parse(self, response):
        filename = 'test.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
