import scrapy

class JimmsSpider(scrapy.Spider):
    name = 'verkkokauppa'
    start_urls = [
        'https://www.jimms.fi/'
    ]


    def parse(self, response):
        for item in response.css('div.productitem'):
            yield {
            'name': item.css('.p_name a::text')[0].get(),
            'brand': item.css('.p_name a b::text')[0].get()
            }
            for link in response.css('div.groupitems a ::attr(href)'):
                yield response.follow(link.get())


