#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

class cat_analysis(object):
    def __init__(self):
        pass

    def cat_analysis(self, page):
        soup = BeautifulSoup(page,'lxml')
        ulList = soup.find_all('ul',class_ = 'ks-ill-list clearfix mt10')
        return_data = dict()
        for item in ulList:
            tempSoup = BeautifulSoup(str(item),'lxml')
            for m in tempSoup.find_all('a'):
                return_data[m.text] = m['href']

        return return_data
