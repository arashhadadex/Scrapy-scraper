import scrapy
from book_scraper.items import BookItem

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):

        books = response.xpath('//li[contains(@class, "col-xs-6")]') # CSS: li.col-xs-6

        for book in books:
            href = book.xpath(".//article/h3/a/@href").get() # CSS: article h3 a::attr(href)

            if href:
                # scrapy uses the response's base url
                full_url = response.urljoin(href)
                yield response.follow(
					full_url,
					callback=self.parse_product,
					meta={
					"url": full_url,
					},
				)

        next_page = response.xpath("//li[@class='next']/a/@href").get() #CSS: li.next a::attr(href)
        if next_page:
            yield response.follow(next_page, callback=self.parse)
            
    def parse_product(self, response):
        
        url = response.meta['url']
        
        name = response.xpath("//div[contains(@class,'col-sm-6')]/h1/text()").get() # CSS: div.product_main h1::text
        price = response.xpath("//p[@class='price_color']/text()").get() #CSS: p.price_color::text
        available_books = response.xpath("//p[contains(@class,'instock')]/text()").get() #CSS: p.instock::text
        product_description = response.xpath("//div[@id='product_description']/following-sibling::p[1]/text()").get()
        UPC = response.xpath("(//table[contains(@class,'table')]/tbody/tr/td)[1]/text()").get() #CSS: table.table tbody tr:first-child td::text
        
        item = BookItem(
            
            URL = url,
            Name = name,
            Price = price,
            Available_books = available_books,
            Product_description = product_description,
            Upc = UPC
        )
        
        yield item