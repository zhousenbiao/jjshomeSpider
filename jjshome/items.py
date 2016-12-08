# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class JjshomeItem(Item):
    # define the fields for your item here like:
    #标题
    title =Field()
    #楼盘
    loupan = Field()
    #格局
    hosuseRoom =Field()
    #面积
    buildArea=Field()
    #位置
    address=Field()
    #总价
    sumPrice=Field()

