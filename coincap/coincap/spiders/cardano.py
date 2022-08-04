import scrapy
import datetime


class CardanoSpider(scrapy.Spider):
    name = 'cardano'
    allowed_domains = ['https://coinmarketcap.com/currencies/cardano']
    start_urls = ['https://coinmarketcap.com/currencies/cardano/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}, callback=self.parse)
        return super().start_requests()

    def parse(self, response):
        coinPrice=response.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span/text()').get()
        print(coinPrice)
        coinTag=response.xpath('//small[@class="nameSymbol"]/text()').get()
        print(coinTag)
        scraped_info = {
            'tag': coinTag,
            'price': coinPrice,
            'updateAt': datetime.datetime.now(),
        }
        yield scraped_info
