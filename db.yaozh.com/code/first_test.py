#!/usr/bin/python
# -*-coding:utf-8-*-
from urllib import request
import requests,csv
from bs4 import BeautifulSoup


cookie = "PHPSESSID=ur559k6brmb5chdd9gprjt7fg1; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1524722580; _ga=GA1.2.746580841.1524722581; ad_download=1; MEIQIA_EXTRA_TRACK_ID=13g1u5rqg0uyUVcIxbVSpHPy4Fc; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1524725826"
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

def spider(url):
    page = requests.get(url)
    with open("new.html","w") as f:
        f.write(page.text)
    return page.text

def parsing(ptext):
    soup = BeautifulSoup(ptext)
    # ============next_page

    # ===========table
    tds = soup.find_all(name='tr')
    if len(tds) == 0:
        return 0

    tds.remove(tds[0])
    with open ("data.csv", "a",newline='') as f:
        writer = csv.writer(f)
        for item in tds:
            soupItem = BeautifulSoup(str(item))
            name = soupItem.th.get_text()
            interaction_name = soupItem.find_all(name = "td")[0].get_text()
            action = soupItem.find_all(name = "td")[1].get_text()
            chain = soupItem.a["href"]
            temp =[name, interaction_name, action, chain]
            writer.writerow(temp)
            print(temp)
            print("===========")

    return 1


if __name__ == "__main__":
    for Hsearch in range(97,123):
        number = 0
        flag = 1
        while flag == 1:
            number+=1
            url = "https://db.yaozh.com/interaction?interactdrugname="+chr(Hsearch)+"&p="+str(number)+"&pageSize=20"
            print(url)
            ptext = spider(url)
            flag = parsing(ptext)

    # for i in range(1,11):
    #     url = "https://db.yaozh.com/interaction?p="+str(i)+"&pageSize=20"
    #     ptext = spider(url)
    #     data = parsing(ptext)
    # print(m)
