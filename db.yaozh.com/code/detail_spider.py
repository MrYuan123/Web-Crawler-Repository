#!/usr/bin/python
# -*-coding:utf-8-*-
import csv,requests
from bs4 import BeautifulSoup

def get_urls():
    urls = list()
    with open("data.csv","r") as f:
        reader = csv.reader(f)
        for item in reader:
            urls.append(item[3])
    return urls

def detail(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    with open("detail.html","w") as f:
        f.write(page.text)

    tables = soup.find_all(name = "tbody")
    name= soup.find_all(name = "tbody")[0].get_text()
    name =  ''.join(name.split())
    name = name[5:]
    tables.remove(tables[0])

    with open ("data_detail.csv", "a",newline='') as f:
        writer = csv.writer(f)
        for item in tables:
            soupD = BeautifulSoup(str(item))
            datas = soupD.find_all(name = "td")

            temp = list()
            temp.append(name)
            print(len(datas))
            for i in range(0,len(datas)):
                temp.append(datas[i].get_text().strip())

            writer.writerow(temp)

            print("-=================")
            for Litem in temp:
                print(Litem)
            print("-=================")
    return 1
if __name__ == "__main__":
    urls = get_urls()
    for url in urls:
        now_url = "https://db.yaozh.com"+url
        print(now_url)
        page_detail = detail(now_url)
        if page_detail == 1:
            pass
        else:
            print(url)
