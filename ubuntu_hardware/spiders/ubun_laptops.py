import scrapy
from ..items import UbuntItem
from scrapy.loader import ItemLoader

class UbunLaptopsSpider(scrapy.Spider):
    name = 'ubun_laptops'
    # allowed_domains = ['https://ubuntu.com/certified?q=&limit=243&category=Laptop&release=20.04+LTS']
    start_urls = ['https://ubuntu.com/certified?q=&limit=243&category=Laptop&release=20.04+LTS']

    def parse(self, response):
        item_links = response.xpath(
            '//*[@id="main-content"]/form/section/div[4]/div[2]/table/tbody/tr[*]/td[2]/a'
        )
        yield from response.follow_all(
            urls=item_links,
            callback=self.parse_item)
    
    def parse_item(self, response):
        global name
        name = response.xpath('//*[@id="main-content"]/section[1]/div[1]/div[1]/h1/text()').get()
        yield response.follow(
            url=response.xpath(
                '//*[contains(text(), "Hardware details")]/@href'
                ).get(),
            callback=self.parse_item_content
            )
    
    def parse_item_content(self, response):
        def X(s):
            return f"//*/th[contains(text(), '{s}')]/following-sibling::node()[2]/ul/li/text()" 
        
        bios = X("BIOS")
        bluetooth = X("Bluetooth")
        network = X("Network")
        processor = X("Processor")
        system = X("System")
        usb = X("USB")
        video = X("Video")
        wireless = X("Wireless")

        IL = ItemLoader(item=UbuntItem(), response=response)
        IL.add_value("name", name)
        IL.add_xpath("bios", bios)
        IL.add_xpath("bluetooth", bluetooth)
        IL.add_xpath("network", network)
        IL.add_xpath("processor", processor)
        IL.add_xpath("system", system)
        IL.add_xpath("usb", usb)
        IL.add_xpath("video", video)
        IL.add_xpath("wireless", wireless)
        IL.add_value("link", response.url)

        yield IL.load_item()
