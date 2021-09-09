import scrapy


class HektorSpider(scrapy.Spider):
    name = 'hektor'
    start_urls = ['https://picjumbo.com/?s=nature']


    def parse(self, response):
        # pictures on the page:
        pic_links_xpath = '/html/body/div[5]/div/a[1]/@href'
        pic_links = response.xpath(pic_links_xpath)

        yield from response.follow_all(
            urls=pic_links,
            callback=self.parse_img,
            )

        next_page = response.xpath('//a[contains(text(), "Next »")]/@href').get()
        if next_page is not None:
            yield response.follow(
                url=next_page,
                callback=self.parse
                )

    def parse_img(self, response):
        # title:
        title_xpath = '/html/body/div[4]/article/div/h1/a/text()'
        pic_title = response.xpath(title_xpath).get()
        # author:
        author_xpath = '/html/body/div[4]/article/div/div[3]/p/a/span/text()'
        author_name = response.xpath(author_xpath).get()
        # view:
        view_xpath = '/html/body/div[4]/article/div/div[2]/text()'
        view_count = response.xpath(view_xpath).getall()[1].split(" ")[2]
        # image url:
        url_xpath = '/html/body/div[4]/article/div/div[1]/a/picture/img/@src'
        img_url = response.xpath(url_xpath).get()

        yield {
            "pic_title": pic_title,
            "author_name": author_name,
            "view_count": view_count,
            "img_url": img_url,
        }
