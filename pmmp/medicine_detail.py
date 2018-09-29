# !/User/bin/python
# -*- coding:utf-8 -*-

import requests,csv
import databaseOP_med
from bs4 import BeautifulSoup
import time

#get urls from csv file
def get_urls():
    mylist = list()
    with open("medicine_data.csv",'r') as f:
        reader = csv.reader(f)
        for item in reader:
            url = item[0]
            name = item[1]
            temp = [name, url]
            mylist.append(temp)
    return mylist

# to get detail web page according to url
def web_crawler(url):
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

# analyze website and get data list
def page_analysis(name, page):
    print(name)
    soup = BeautifulSoup(page,'lxml')
    table = soup.find('table', height = '100%', cellspacing = '0', cellpadding = '0')
    souptr = BeautifulSoup(str(table),'lxml')
    trtable = souptr.find_all('td')
    trtable = trtable[1:]
    detailtable =list()

    for item in trtable:
        if '<td width="50%">' in str(item):
            pass
        else:
            detailtable.append(''.join(str(item.get_text()).split()))
    detailtable.pop()

    temp_dict = dict(zip(detailtable[0::2],detailtable[1::2]))
    final_dict = dict()

    for item in temp_dict:
        final_dict[' '.join(str(item[:-1]).split())] = temp_dict[item]

    final_dict['药品名称'] = name
    # relative disease
    diseasec = ''
    disease_table = soup.find_all(id = 'MD_Context1_relDis')
    soup2 = BeautifulSoup(str(disease_table),'lxml')
    disease_table = soup2.find_all('a')
    for item in disease_table:
        diseasec = diseasec + item.string+ ','

    final_dict['相关疾病'] = diseasec[:-1]

    return final_dict

# insert data into database
def append_data(name, url, datadict):
    status = databaseOP_med.insert_data(datadict)
    if status == True:
        print("insert data success!")
    else:
        print('insert data fail!')
        input()
        with open('medicine_error.csv','a', newline='') as f:
            writer = csv.writer(f)
            temp = list()
            temp.append(name)
            temp.append(url)
            writer.writerow(temp)

    return

if __name__ == '__main__':
    mylist = get_urls()
    base_url = 'http://pmmp.cnki.net/cdd/Medicine/'
    # url = 'http://pmmp.cnki.net/cdd/Medicine/Med_Detail.aspx?id=114&SearchType=1'
    # name = '17β-雌二醇'
    # # url = "http://pmmp.cnki.net/cdd/Medicine/Med_Detail.aspx?id=5837&SearchType=1"
    # # name = '西他沙星'
    # page = web_crawler(url)
    #
    # datadict = page_analysis(name,page)
    # flag = 1
    # for item in datadict:
    #     print(flag)
    #     print(item)
    #     print(datadict[item])
    #     flag+=1
    # append_data(name, url, datadict)
    flag = 1
    # mylist = mylist[909:]
    # print(mylist[0])
    # input()
    with open('medicine_error.csv','r') as f:
        reader = csv.reader(f)
        for item in reader:
            url = item[1]
            name = item[0]
            page = web_crawler(url)
            datadict = page_analysis(name,page)
            for m in datadict:
                print(m + " : " + datadict[m])
            # append_data(name, url, datadict)

    print("pause")
    input()

    for item in mylist:
        name = item[0]
        url = base_url+item[1]
        print('=======================')
        print(name)
        print(url)
        print('=======================')
        page = web_crawler(url)
        datadict = page_analysis(name,page)
        for item in datadict:
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
            print(flag)
            print(item)
            print(datadict[item])
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
        append_data(name, url, datadict)
        flag+=1
