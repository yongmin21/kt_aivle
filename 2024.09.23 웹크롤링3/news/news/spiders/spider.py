
import scrapy
from news.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    allow_domain = ['daum.net']
    start_urls = ['https://news.daum.net']
    
    def parse(self, response):
        # requests는 이미 scrapy.Spider 안에 있음.
        selector = "/html/body/div[2]/main/section/div/div[1]/div[1]/ul/li/div/div/strong/a/@href"
        links = response.xpath(selector).extract() #extract - 값들만 추출

        for link in links:
            yield scrapy.Request(link, callback=self.parse_content)
            
    def parse_content(self, response):
        item = NewsItem()
        item['link'] = response.url
        item['title'] = response.xpath('//*[@id="mArticle"]/div[1]/h3/text()')[0].extract()
        yield item
