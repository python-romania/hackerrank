import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.epiesa.ro/cautare-piesa/?find=gdb400",
        "https://www.epiesa.ro/cautare-piesa/?find=ct1028k3",
        "https://www.epiesa.ro/cautare-piesa/?find=do229",
        "https://www.epiesa.ro/cautare-piesa/?find=hu7262x",
    ]
    # for i in range(1,10):
    #     start_urls.append('http://quotes.toscrape.com/page/' + str(i) + '/')

    def parse(self, response):
        for product in response.css('div.single_prd'):
            old_price = product.css('div.col-xs-12')[1].css("b del::text").get()
            yield {
                'name': product.css('h2 a.gg-tag::text').get(),
                'product_url': product.css('div.image_overflow a::attr(href)').extract(),
                'image_url': product.css('div.image_overflow a img::attr(src)').extract(),
                'brand': product.css('p b::text').re(r'Producator: \s*(.*)'),
                'product_mfrpn': product.css('p b::text').re(r'Cod producator: \s*(.*)'),
                'old_price': str(old_price).replace(" Lei", ""),
                'price': product.css('div.col-xs-12')[1].css("b span.red::text").get(),
            }
