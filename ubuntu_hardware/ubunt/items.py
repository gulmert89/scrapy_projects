import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags, strip_html5_whitespace


class UbuntItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(strip_html5_whitespace),
        output_processor=TakeFirst())
    
    bios = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst())
    
    bluetooth = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst())
    
    network = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst())
    
    processor = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst())
    
    system = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst())
    
    usb = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace)
    )
    
    video = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace)
    )  # TakeFirst() removed to get all the cards.
    
    wireless = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_html5_whitespace),
        output_processor=TakeFirst())
    
    link = scrapy.Field(output_processor=TakeFirst())
