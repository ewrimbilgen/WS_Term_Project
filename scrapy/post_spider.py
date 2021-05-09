import scrapy

from scrapy.selector import Selector

from scrapy.http import HtmlResponse


class shopClues(scrapy.Spider):
    name = "shopclues"


    allowed_domains = ['www.shopclues.com/']

    # lists that our products categories
    # mobile phone-gaming consoles-headphones

    start_urls = [
        "http://www.shopclues.com/branded-deals.html/",
        "https://www.shopclues.com/computer-games-gaming-consoles.html",
        "https://www.shopclues.com/audio-accessories-headphones.html",

    ]


    # extract product's name-orginal price-discount ratio-its image url
    def parse(self, response):
        img = response.css('img::attr(data-img)').extract()
        for index, col3 in enumerate(response.css('div.col3')):
            yield {
                'name': col3.css('span.prod_name::text').extract_first(),
                'price': col3.css('span.p_price::text').extract_first(),
                'discount': col3.css('span.prd_discount::text').extract_first(),
                'image': img[index],
            }

   # I run  scrapy crawl shopclues -o shopclues.csv






