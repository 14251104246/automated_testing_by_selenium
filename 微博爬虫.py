#coding:utf-8
#xiaohei.python.seo.call.me:)
#win+python2.7.x
import csv
import codecs
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome()

driver =webdriver.Chrome()

driver .set_window_size(1080,800)

driver.implicitly_wait(20)

driver.get('http://s.weibo.com/top/summary?cate=realtimehot')


csvfile = file('csvtest.csv', 'wb')
csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile)
writer.writerow([u'排名',u'关键词',u'搜索指数',u'搜索热度'])

#realtimehot > tbody > tr:nth-child(1) > td.td_01
#realtimehot > tbody > tr:nth-child(1) > td.td_02 > div > p > a
#realtimehot > tbody > tr:nth-child(1) > td.td_03 > p > span
table = driver.find_element_by_css_selector("#realtimehot > tbody > tr:nth-child(1) > td.td_01")



for i in range(1,50):
    rank = unicode (driver.find_element_by_css_selector("#realtimehot > tbody > tr:nth-child("+str(i)+") > td.td_01 > span > em").text)
    keyword = driver.find_element_by_css_selector("#realtimehot > tbody > tr:nth-child("+str(i)+") > td.td_02 > div > p > a").text
    serch_num = driver.find_element_by_css_selector("#realtimehot > tbody > tr:nth-child("+str(i)+") > td.td_03 > p > span").text
    writer.writerow([rank, keyword, serch_num, " "])

csvfile.close()
