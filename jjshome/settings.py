# -*- coding: utf-8 -*-
# Scrapy settings for jjshome project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'jjshome'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['jjshome.spiders']
NEWSPIDER_MODULE = 'jjshome.spiders'
# USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

# 配置使用的数据管道
ITEM_PIPELINES = {
'jjshome.pipelines.MySQLStorePipeline': 300,#mysql数据库
'jjshome.pipelines.JsonOutPutPipeline': 300,#json存储格式
}

# 设置等待时间缓解服务器压力 并能够隐藏自己
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = True

FEED_EXPORTERS = {
    'csv': 'jjshome.jjshome_csv_item_exporter.CsvItemExporter',
}
#执行scrapy crawl EsfSpider -o esf.csv 即可经将数据导出csv格式
# '楼盘',
# '格局',
# '面积',
# '总价'
# '均价',
# '位置',
# '标题',
# '来源'
FIELDS_TO_EXPORT = [
    'loupan',
    'hosuseRoom',
    'buildArea',
    'sumPrice',
    'averagePrice',
    'address',
    'title',
    'source'
]

CSV_DELIMITER = ","