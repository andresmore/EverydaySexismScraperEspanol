import scrapy


class SexismMexSpider(scrapy.Spider):
    name = "sexism_mex_ar_es"
    allowed_domains = ["everydaysexism.com"]
    start_urls = ["https://everydaysexism.com/country/mx/","https://everydaysexism.com/country/ar/"
                                                           ,"https://everydaysexism.com/country/es/"]

    def parse(self, response):
        for item in response.xpath('//div[@itemprop="description"]/p'):
            # Extract the text from the <p> tag
            description_text = item.xpath('.//text()').getall()
            # Join the text items in case the <p> tag contains multiple strings
            description = '\n'.join(description_text).strip()
            print(description)
            yield {
                'URL': response.url,
                'Description': description,
            }

        # Using XPath to select link text "older"
        next_page_link = response.xpath('//a[contains(text(), "older")]/@href').get()
        if next_page_link is not None:
            yield response.follow(next_page_link, self.parse)
