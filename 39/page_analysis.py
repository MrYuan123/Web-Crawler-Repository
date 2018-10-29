# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

class page_analysis(object):
    def __init__(self):
        pass

    def page_analysis(self, page_detail):
        soup = BeautifulSoup(page_detail,'lxml')
        ini_lists = soup.find_all("div",class_ = "res_list")
        # title href price
        crawl_data = list()
        for item in ini_lists:
            temp = list()
            temp.append(item.a['title'])
            temp.append(item.a['href'])
            temp.append(item.span.text.strip())
            crawl_data.append(temp)
            # print(item.a['title'])
            # print(item.a['href'])
            # print('*'+item.span.text.strip()+'*')
            # print("++++++++++++++++++++++++++")

        # next_url
        next_url = None
        find_next = soup.find_all('a',class_ = "sp-a")
        for item in find_next:
            if item.text == '下页':
                # print(item['href'])
                next_url = item['href']

        return_data = dict()
        return_data['crawl_data'] = crawl_data
        return_data['next_url'] = next_url
        return return_data
