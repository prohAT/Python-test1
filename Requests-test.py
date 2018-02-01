# -*- coding: utf-8 -*-
#import requests,webbrowser,urllib3,bs4
##get weather info from view-source:http://www.weather.com.cn/weather/
#uri = "view-source:http://www.weather.com.cn/weather/"
#city_code=101280601#SHEN ZHENG
#http = urllib3.PoolManager()
#r = http.request('GET', 'http://www.weather.com.cn/weather/101280601.shtml')
#soup = bs4.BeautifulSoup(r.data,"lxml")
#elements = soup.select('p[class=wea]')
#print(elements[0].attrs)


#baidu search 湖南怀化
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.baidu.com/index.php?tn=monline_3_dg')
elements = driver.find_element_by_class_name('s_ipt')
elements1 = driver.find_element_by_id('su')
elements.send_keys('湖南怀化')
elements1.click()