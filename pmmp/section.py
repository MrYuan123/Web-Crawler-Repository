# !/User/bin/python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests,csv

def read_session(nhtml):
    soup = BeautifulSoup(nhtml, 'lxml')
    viewstate = soup.find(id="__VIEWSTATE")['value']
    eventvalidation = soup.find(id="__EVENTVALIDATION")['value']
    return viewstate,eventvalidation


url = "http://pmmp.cnki.net/cdd/Disease/Dis_Basic.aspx"
s = requests.session()
r = s.get(url)
a,b = read_session(r.text)

print(a)
print(b)

# data ={'DS_Basic1$dropSearchType': 'name',
# 'DS_Basic1$txtKeyword': '',
# 'DS_Basic1$rdoSearch': '4',
# 'DS_Basic1$btnGo.x': '24',
# 'DS_Basic1$btnGo.y': '8',

data = {
# '__EVENTTARGET': 'DS_Basic1$linkNext',
# '__EVENTARGUMENT':'',
# '__LASTFOCUS':'',
'DS_Basic1$dropSearchType': 'name',
'DS_Basic1$txtCurrentPage': '2',
'DS_Basic1$DropNumber': '10',
 '__VIEWSTATE' :a,
 '__EVENTVALIDATION' :b,}

headers={
#'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
# 'Cache-Control': 'max-age=0',
# 'Connection': 'keep-alive',
# 'Content-Length': '6386',
# 'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'ASP.NET_SessionId=tviiji45dmw1lm4533jxna55; SID=201116',
# 'Host': 'pmmp.cnki.net',
# 'Origin': 'http://pmmp.cnki.net',
# 'Referer': 'http://pmmp.cnki.net/cdd/Disease/Dis_Basic.aspx',
# 'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

page = requests.post(headers = headers, data = data, url = url)
print(page.text)
# m,n = read_session(page.text)
# print(m)
# print(n)
# print(str(page.text))
#

with open("page.html","w") as f:
    writer = csv.writer(f)
    writer.writerow(str(page.text))
