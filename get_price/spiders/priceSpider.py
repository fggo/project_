import scrapy


class priceSpider(scrapy.Spider):
    name = 'price' # spider name

    def start_requests(self):
        """send request to url for crawling and parse
        """
        url = 'https://smartstore.naver.com/' + self.seller + '/products/' + self.product_id
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """parse the html elements and return the discount price
        """
        r = response.css('dd.default')[1]
        yield{
            "discount_price": r.css('p.sale>strong>span.thm::text').extract_first(),
        }
