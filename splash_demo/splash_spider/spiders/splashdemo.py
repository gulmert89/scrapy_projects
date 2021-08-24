import scrapy
from scrapy_splash import SplashRequest

# Note: The lines with ## (double comments) are the changed lines for
# Splash specifically. It doesn't work with pure Scrapy requests.


class SplashdemoSpider(scrapy.Spider):
    name = 'splashdemo'
    # allowed_domains = ['https://quotes.toscrape.com/js/']
    # start_urls = ['https://quotes.toscrape.com/js/']    

    def start_requests(self):
        url = 'https://quotes.toscrape.com/js'

        # yield scrapy.Request(url=url, callback=self.parse)
        yield SplashRequest(
            url=url,
            callback=self.parse
            )

    def parse(self, response):
        quote_blocks = response.xpath('/html/body/div/div[@class="quote"]')
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        page_number = int(next_page.split("/")[-2]) - 1
        quote_dict = dict()
        person_list = list()
        tags_list = list()

        for r in quote_blocks:
            person = r.xpath('.//span[2]/small/text()').get()
            tags = r.xpath('.//div[@class="tags"]/a/text()').getall()
            person_list.append(person)
            tags_list.append(tags)

        quote_dict.update(dict(zip(person_list, tags_list)))

        yield {f"page_{str(page_number)}": quote_dict}

        if page_number < 5:
            # yield response.follow(url=next_page, callback=self.parse)
            yield SplashRequest(
                response.urljoin(url=next_page),
                callback=self.parse
                )
