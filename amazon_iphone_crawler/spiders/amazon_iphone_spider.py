import scrapy
from ..items import AmazonIphoneCrawlerItem

class AmazonIphoneSpiderSpider(scrapy.Spider):
    name = 'amazon_iphones'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com.br/s?k=iphone']

    def parse(self, response):
        items = AmazonIphoneCrawlerItem()

        all_products = response.css('.s-asin .sg-col-inner')

        for product in all_products:
            product_name = "".join(product.css('.a-color-base.a-text-normal').css('::text').extract())
            product_price_whole = product.css('.a-price-whole').css('::text').extract()
            product_price_fraction = product.css('.a-price-fraction').css('::text').extract()
            product_price_combined = "".join(product_price_whole + product_price_fraction)
            # product_price_combined = product_price_whole

            items['product_name'] = product_name
            items['product_price_whole'] = product_price_combined
            # items['product_price_fraction'] = product_price_fraction

            yield items

        # pass
