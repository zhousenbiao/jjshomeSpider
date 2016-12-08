# -*- coding: utf-8 -*-
# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import json
import codecs

#用mysql存储
class MySQLStorePipeline(object):
    #数据库参数
    def __init__(self):
        dbargs = dict(
             host = '127.0.0.1',
             db = 'jjshome',
             user = 'root',
             passwd = 'rsclouds@123',
             cursorclass = MySQLdb.cursors.DictCursor,
             charset = 'utf8',
             use_unicode = True
            )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)

    '''
    The default pipeline invoke function
    '''
    def process_item(self, item,spider):
        res = self.dbpool.runInteraction(self.insert_EsfInfo,item)
        return item
    #将数据插入数据库的esfInfo表，此表需要事先创建好
    def insert_EsfInfo(self,conn,item):
            conn.execute("""insert into esfInfo(loupan,houseRoom,buildArea,sumPrice,averagePrice,title,address,source) values(%s, %s, %s, %s,%s,%s, %s, %s)""", (item['loupan'][0],item['hosuseRoom'][0],item['buildArea'][0],item['sumPrice'][0],item['averagePrice'],item['title'][0],item['address'][0],item['source']))


#以Json的形式存储
class JsonOutPutPipeline(object):
    def __init__(self):
        self.file = codecs.open('jjshome_esf.json','wb',encoding = 'utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'#对数据类型进行编码
        print line
        self.file.write(line.decode("unicode_escape"))
        return item

    def spider_closed(self, spider):  # 爬虫结束时关闭文件
        self.file.close()