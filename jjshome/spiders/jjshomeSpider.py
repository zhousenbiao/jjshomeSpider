#! /usr/bin/env python
# coding=utf-8
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector
import json
from ..items import JjshomeItem
# 处理编码问题
import sys
reload(sys)
sys.setdefaultencoding('gb18030')

class jjshomeSpider(Spider):
    name = "EsfSpider"
    start_urls = ['http://dongguan.jjshome.com/esf/n1c%E5%A4%A7%E5%B2%AD%E5%B1%B1']
    dongguanUrl = "http://dongguan.jjshome.com"
    firstPageUrl = ['/esf/n1c%E5%A4%A7%E5%B2%AD%E5%B1%B1']

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    def parse(self, response):
        # 翻页,获取所有分页的链接
        next_page = response.xpath("//div[@class='jjs-page1']")
        for pageurl in next_page:
            #url = response.urljoin(next_page[0].extract())
            url=pageurl.xpath("a/@href").extract()
            del url[-2:]
            url+=self.firstPageUrl
            # print url
            for nexturl in url:
                yield Request(self.dongguanUrl+nexturl, headers=self.headers,callback=self.parseInfos)
                # yield Request(url, self.parse,dont_filter=True)

    #爬取每一页的列表中的信息
    def parseInfos(self,response):
        # # 标题： //div[@class='text']/p/a/text()  或者：//div[@ class ='img']/a//img/@alt
        # # 楼盘：response.xpath("//div[@class='text']//p[@class='clearfix f16 pt10']/span/text()")
        # # 格局：response.xpath("//div[@class='text']//p[@class='clearfix f16 pt10']//span[@class='w95 houseRoom']/text()")
        # # 面积：response.xpath("//div[@class='text']//p[@class='clearfix f16 pt10']//span[@class='w95 buildArea']/text()")
        # # 地址：response.xpath("//div[@class='text']//p[@class='clearfix mt10']//span[@class='c666 fl w410']/text()")
        # # 总价：response.xpath("//div[@class='price esf-price c90']//p[@class='f12 c333']//span[@class='num salePrice']/text()")
        sel = Selector(response)
        nodes = sel.xpath("//div[@class='one-list clearfix']")
        # items = []
        for sele in nodes:
            item = JjshomeItem()
            title = sele.xpath("div[@class='img']/a//img/@alt").extract()
            loupan = sele.xpath(
                "div[@class='text']//p[@class='clearfix f16 pt10']//span[@class='fl mr50']/text()").extract()
            houseRoom = sele.xpath(
                "div[@class='text']//p[@class='clearfix f16 pt10']//span[@class='w95 houseRoom']/text()").extract()
            buildArea = sele.xpath(
                "div[@class='text']//p[@class='clearfix f16 pt10']//span[@class='w95 buildArea']/text()").extract()
            address = sele.xpath(
                "div[@class='text']//p[@class='clearfix mt10']//span[@class='c666 fl w410']/text()").extract()
            sumPrice = sele.xpath(
                "div[@class='price esf-price c90']//p[@class='f12 c333']//span[@class='num salePrice']/text()").extract()

            # item['title'] = [t.encode('utf-8') for t in title]
            # item['loupan'] =[l.encode('utf-8') for l in loupan]
            # item['hosuseRoom'] =[h.encode('utf-8') for h in houseRoom]
            # item['buildArea'] =[b.encode('utf-8') for b in buildArea]
            # item['address'] =[a.encode('utf-8') for a in address]
            # item['sumPrice'] =[s.encode('utf-8') for s in sumPrice]
            item['title'] = title
            item['loupan'] = loupan
            item['hosuseRoom'] = houseRoom
            item['buildArea'] = buildArea
            item['address'] = address
            item['sumPrice'] = sumPrice
            # items.append(item)
            yield item
