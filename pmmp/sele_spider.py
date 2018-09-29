# !/User/bin/python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import os,csv,chardet

def get_info(item):
    soupn = BeautifulSoup(str(item))
    dname = soupn.find(name = 'a', target = "_blank")['href']
    mlists = soupn.find_all(name = "span")
    temp = list()
    temp.append(dname)
    for item in mlists:
        temp.append(item.string)
    return temp

def get_page(pageSource):
    soup = BeautifulSoup(pageSource)
    first = soup.find_all(name = "table",cellspacing = "0", cellpadding = "6")
    soup2 = BeautifulSoup(str(first))
    mytable = soup2.find_all("tr")
    mytable = mytable[2:]
    mytable = mytable[::2]
    return mytable

def add_info(temp):
    with open ("disease_data.csv", "a",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(temp)
    return

def start_spider():
    flag = 1
    driver = webdriver.Chrome()
    driver.get("http://pmmp.cnki.net/cdd/Disease/Dis_Basic.aspx")
    button = driver.find_element_by_id('DS_Basic1_btnSubmit')
    button.click()
    pageSource = driver.page_source

    mytable = get_page(pageSource)

    for item in mytable:
        print("==================")
        print(flag)
        #print(item)
        details = get_info(item)
        add_info(details)
        for m in details:
            print(m)
        print("==================")

    flag+=1

    while True:
        if flag>672:
            return
        else:
            # link = driver.find_element_by_id('DS_Basic1_linkNext')
            # link.click()
            driver.find_element_by_link_text("下一页").click()
            pageSource = driver.page_source
            mytable = get_page(pageSource)

            for item in mytable:
                print("==================")
                print(flag)
                #print(item)
                details = get_info(item)
                add_info(details)
                for m in details:
                    print(m)
                print("==================")

            flag+=1

    input()
    driver.close()
    # with open("page.html","w") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(pageSource)


if __name__ == "__main__":
    start_spider()
