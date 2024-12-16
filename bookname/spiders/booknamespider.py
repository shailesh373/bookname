import scrapy


class BooknamespiderSpider(scrapy.Spider):
    name = "booknamespider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
         

        Bookname = response.css("h3 > a::attr(title)").getall()
        
        for title in Bookname:
            print()
            print()
            print()
            print(title) 
            print()
            print()
            print()
            
            yield{
            "NameTitle" : title 
            }

