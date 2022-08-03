import scrapy
import datetime


class CardanoSpider(scrapy.Spider):
    name = 'cardano'
    allowed_domains = ['https://coinmarketcap.com/currencies/cardano']
    start_urls = ['https://coinmarketcap.com/currencies/cardano/']

    def parse(self, response):
        coinPrice=response.xpath('//div[@class="priceValue "]/text()').get()
        coinTag=response.xpath('//small[@class="nameSymbol"]/text()').get()
        scraped_info = {
            'tag': coinTag,
            'price': coinPrice,
            'updateAt': datetime.datetime.now(),
        }
        yield scraped_info
