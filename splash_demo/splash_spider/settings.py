# Splash settings:
SPLASH_URL = 'http://localhost:8050'
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    'splash_spider.middlewares.SplashSpiderSpiderMiddleware': 543,
}

DOWNLOADER_MIDDLEWARES = {
    'splash_spider.middlewares.SplashSpiderDownloaderMiddleware': 543,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


BOT_NAME = 'splash_spider'

SPIDER_MODULES = ['splash_spider.spiders']
NEWSPIDER_MODULE = 'splash_spider.spiders'
#USER_AGENT = 'splash_spider (+http://www.yourdomain.com)'
ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = "utf-8"


#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'splash_spider.pipelines.SplashSpiderPipeline': 300,
#}