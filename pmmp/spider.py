#!/usr/bin/python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests,csv

Nurl = "http://pmmp.cnki.net/cdd/Disease/Dis_Catalog.aspx"

def post_request(url):
    return

if __name__ =="__main__":
    data ={'DS_Catalog1$txtCurrentPage':'2','DS_Catalog1$DropNumber':'50'}
    headers = {'Content-Type':'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36','Cookie':'ASP.NET_SessionId=tviiji45dmw1lm4533jxna55; SID=201116','Upgrade-Insecure-Requests': '1','DS_Catalog1$dropSearchType': 'name'}

    page = requests.post(headers = headers, data = data, url = Nurl)
    print(str(page.text))

    with open("page.html","w") as f:
        writer = csv.writer(f)
        writer.writerow(str(page.text))
