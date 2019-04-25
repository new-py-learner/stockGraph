# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:35:56 2019

@author: liuhuanying
"""
import tushare as ts # 该模块是一个免费提供股票交易数据的API<br><br>
import xlrd
import os

#根据代码获取公司名称
def getCompyName(code):
     #获取基础股票信息
    base=ts.get_stock_basics()
    #得到具体公司信息
    company=base[base.index==code]
    return company.ix[0,'name']

#从excel文件获取舆情数据,包括了舆情和情感分析数据
def getDatabyExcel(filename):
    # 打开文件
    if not os.path.exists(filename):
        print('file not exist')
        return
    workbook = xlrd.open_workbook(r'%s'%(filename))
   
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
    #sheet2 = workbook.sheet_by_name('sheet2')
    row=1
    data=[]
    while row<=sheet1.nrows :
        data.append(sheet1.row_values(row-1))
        row+=1
    return data     


#三全食品
def sqsp():
   start = '2019-01-10'
   end = '2019-03-26'
   code='002216'
   return start,end,code
#方正科技
def fzkj():
   start = '2019-02-05'
   end = '2019-04-08'
   code='600601'
   return start,end,code

#视觉中国
def sjzg():
   start = '2019-03-05'
   end = '2019-04-12'
   code='000681'
   return start,end,code

#东风股份
def dfgf():
   start = '2019-02-15'
   end = '2019-04-12'
   code='601515'
   return start,end,code

#顺灏股份 
def shgf():
   start = '2019-02-15'
   end = '2019-04-12'
   code='002565'
   return start,end,code

#劲嘉股份
def jjgf():
   start = '2019-02-15'
   end = '2019-04-12'
   code='002191'
   return start,end,code

#华宝股份
def hbgf():
   start = '2019-02-15'
   end = '2019-04-12'
   code='300741'
   return start,end,code
#美盈森
def mys():
   start = '2019-02-15'
   end = '2019-04-12'
   code='002303'
   return start,end,code
# 盈趣科技
def yqkj():
   start = '2019-02-15'
   end = '2019-04-12'
   code='002925'
   return start,end,code
# 亿纬锂能
def ywln():
   start = '2019-02-15'
   end = '2019-04-12'
   code='300014'
   return start,end,code
#和而泰
def hlt():
   start = '2019-02-15'
   end = '2019-04-12'
   code='002402'
   return start,end,code
#科森科技
def kskj():
   start = '2019-02-15'
   end = '2019-04-12'
   code='603626'
   return start,end,code

#蓝色光标
def lsgb():
    start = '2019-02-15'
    end = '2019-04-21'
    code='300058'
    return start,end,code
#美的
def md():
    start = '2019-02-15'
    end = '2019-04-21'
    code='000333'
    return start,end,code

#视觉中国
def sjzg():
    start = '2019-03-11'
    end = '2019-04-22'
    code='000681'
    filename='eagtek(2019-04-23 09_31).xls'  
    return start,end,code,filename

#浙江龙盛
def zjls():
    start = '2019-02-15'
    end = '2019-04-21'
    code='600352'
    return start,end,code

#联想集团
def lxjt():
   start = 20190205
   end = 20190408
   code='00992'
   return start,end,code
