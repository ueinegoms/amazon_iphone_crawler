import scrapy
from ..items import AmazonIphoneCrawlerItem

class AmazonIphoneSpiderSpider(scrapy.Spider):
    name = 'amazon_iphones'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com.br/s?k=iphone']

    def parse(self, response):
        items = AmazonIphoneCrawlerItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_price_whole = response.css('.a-price-whole').css('::text').extract()
        product_price_fraction = response.css('.a-text-price').css('::text').extract()

        items['product_name'] = product_name
        items['product_price_whole'] = product_price_whole
        items['product_price_fraction'] = product_price_fraction

        yield items

        # pass
