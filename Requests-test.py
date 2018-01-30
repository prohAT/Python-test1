# -*- coding: utf-8 -*-
import requests,webbrowser,urllib3,bs4
http = urllib3.PoolManager()
r = http.request('GET', 'http://www.baidu.com')
soup = bs4.BeautifulSoup(r.data,"lxml")
elements = soup.select('div[class=s_tab]')
print(elements[0].attrs)
