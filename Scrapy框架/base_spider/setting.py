# -*- coding: utf-8 -*-

# Scrapy settings for Web project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#这个文件只包含重要、常用的设置，可以下列文档中查看更多设置
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'base_spider'
#bot 网络机器人

SPIDER_MODULES = ['base_spider.spiders']
NEWSPIDER_MODULE = 'base_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#设置请求头
USER_AGENT ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',

# Obey robots.txt rules 爬虫协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16) 设置爬虫执行的最大请求，异步请求，默认16
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0) 针对一些网站可以设置请求延迟
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#下载延迟
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#设置每个域名请求次数，应该是每个URL请求次数
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#每个IP请求次数
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)  默认使用cookie
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers: 覆盖默认的请求头
# DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
# }

# Enable or disable spider middlewares 是否使用 爬虫中间器
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Web.middlewares.WebSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares 是否使用 下载中间器
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Web.middlewares.WebDownloaderMiddleware': 543,
#}

# Enable or disable extensions      是否使用扩展
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines  设置 item piplines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Web.pipelines.WebPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default) 是否启用自动限速设置
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default) 是否启用 http caching 缓存
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
