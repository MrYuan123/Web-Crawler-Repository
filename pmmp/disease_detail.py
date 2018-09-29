# !/User/bin/python
# -*- coding:utf-8 -*-
import requests,csv
from bs4 import BeautifulSoup
import time
import databaseOP


a =[1]*18

title = ['概述','流行病学','病因','发病机制','临床表现','并发症','实验室检查','其他辅助检查','诊断','鉴别诊断','治疗','预后','预防']

def get_newurls():
    return_list = list()
    with open("append_disease.csv", 'r') as f:
        reader = csv.reader(f)
        for item in reader:
            temp = list()
            temp.append(' '.join(str(item[2]).split()))
            temp.append(' '.join(str(item[0]).split()))
            temp.append(' '.join(str(item[1]).split()))
            return_list.append(temp)
    return return_list



def get_urls():        # get urls from csv file
    mylist = list()
    with open("disease_data.csv","r") as f:
        reader = csv.reader(f)
        for item in reader:
            temp = list()
            temp.append(item[0]) # url
            temp.append(item[1]) # name
            temp.append(item[5]) # icd
            mylist.append(temp)
    return mylist

def page_spider(url):       # get detail page
    while True:
        try:
            page = requests.get(url)
            page_detail = page.text
            break
        except requests.exceptions.ConnectionError:
            print("ConnectionError -- please wait 10 seconds")
            time.sleep(10)
        except requests.exceptions.ChunkedEncodingError:
            print('ChunkedEncodingError -- please wait 10 seconds')
            time.sleep(10)
        except:
            print('Unfortunitely -- An Unknow Error Happened, Please wait 10 seconds')
            time.sleep(10)
    return page_detail

def img_links(page,name):      # analyze imgs in the web
    soup = BeautifulSoup(page,'lxml')
    imgs = list()
    imgs.append(name)
    for item in soup.find_all('img'):
        linkdet = item.get('src')
        # print(linkdet)
        if linkdet.find('gif') != -1:
            pass
        else:
            imgs.append(linkdet)
            # print(linkdet)
    return imgs

def get_list(page,name,icd):      # main lsit
    soup = BeautifulSoup(page,'lxml')
    return_list = list()
    spanlist = soup.find_all('span', attrs = {'class' :'ColumnValue'})
    return_list.append(name)
    return_list.append(icd)

    for item in spanlist:
        data_detail = item.get_text()
        if len(data_detail.replace(' ','')) != 0:
            return_list.append(data_detail)
        # if len(data_detail.replace(' ',''))< 10:
        #     for ls in title:
        #         if ls in data_detail:
        #             return_list.append(data_detail)
        #             print("small:")
        #             print(data_detail)
        #             print(item)
        #         else:
        #             pass
        # else:
        #     return_list.append(data_detail)
        #     print("big:")
        #     print(data_detail)

    # relative medicine
    med_list = list()
    med_table = soup.find_all(id = "DS_Content1_relMed")
    soup2 = BeautifulSoup(str(med_table),'lxml')
    med_table =soup2.find_all('a')
    for item in med_table:
        # print(item.string)
        med_list.append(item.string)
    return_list.append(med_list)

    # relative detect
    detect_list = list()
    detect_table = soup.find_all(id = "DS_Content1_relLab")
    soup3 = BeautifulSoup(str(detect_table),'lxml')
    detect_table =soup3.find_all('a')
    for item in detect_table:
        # print(item.string)
        detect_list.append(item.string)
    return_list.append(detect_list)

    return return_list

def page_analysis(page,name,icd):    #
    data_list = get_list(page,name,icd)
    imgs = img_links(page,name)
    return data_list,imgs

def show_detail(dlist,flag):
    id = 1
    status = True
    for item in dlist:
        print("+++++++++++++++++++++++++++++++")
        print("flag : %d"%(flag))
        if id>18:
            print('error!')
            input()
            status = 'MORE THAN 18'

        print('id : %d'%(id))

        if len(str(item)) > a[id-1]:
            a[id-1] = len(str(item))

        id+=1
        print(item)
        print(len(str(item)))
        print("+++++++++++++++++++++++++++++++")

    if id <19:
        print('LESS THAN 18, error!')
        input()
        status = 'LESS THAN 18'
    else:
        pass
    print(a)
    return status

def add_imgs(imgs):
    with open ('imgs.csv', 'a', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(imgs)
    return

def append_data(dlist, name, url):
    status = databaseOP.data_insert(dlist)
    if status != True:
        print("database operate error : %s"%(status))
        with open("append_error.csv","a",newline='') as f:
            writer = csv.writer(f)
            temp = [name, url]
            writer.writerow(temp)

    else:
        print("database operation success!")


if __name__ == "__main__":
    urlList = get_newurls()
    # urlList = get_urls()
    base_url = 'http://pmmp.cnki.net/cdd/Disease/'
    flag = 1
    #
    # urlList = urlList[2324:]
    # print(urlList[0])
    # input()

    for item in urlList:
        url = item[0]
        url = base_url +url
        name = item[1]
        icd = item[2]
        page = page_spider(url)

        # get analysis result
        dlist,imgs = page_analysis(page,name,icd)

        if show_detail(dlist,flag) == True:
            append_data(dlist, name, url)
        else:
            print("false list format!")
            input()
            with open("table_error.csv","a",newline='') as f:
                writer = csv.writer(f)
                temp = [name, icd, url]
                writer.writerow(temp)

        add_imgs(imgs)
        print(imgs)
        flag+=1
