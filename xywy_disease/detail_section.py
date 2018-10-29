#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

class detail_analysis(object):
    def __init__(self):
        pass

    def treat_page(self,page):
        soup = BeautifulSoup(page,'lxml')
        return_data = dict()
        # ====================
        # name section
        dname = soup.find('div',class_ = 'jb-name fYaHei gre').text.strip().replace(' ', '')
        return_data['name'] = dname
        # =============
        # === zhiliao gaishu===
        gaishu = soup.find_all('p',class_ = 'clearfix')
        for item in gaishu:
            soupt = BeautifulSoup(str(item),'lxml')
            pdetail = soupt.find_all('span')
            name = pdetail[0].text.strip().replace(' ','')[:-1]
            gaishu_detail = pdetail[1].text.strip().replace('\n','').replace(' ','').replace('\t',' ')
            return_data[name] = gaishu_detail

        # =============
        # == zhiliao ==
        treat_detail = soup.find('div',class_ = 'jib-lh-articl')
        zhiliao = treat_detail.text.strip()
        return_data['治疗具体'] = zhiliao

        return return_data

    def symptom_page(self,page):
        return_list = list()
        soup = BeautifulSoup(page,'lxml')
        spansect = soup.find('span',class_ = 'db f12 lh240 mb15 ')
        soupa = BeautifulSoup(str(spansect),'lxml')
        details = soupa.find_all('a')
        for item in details:
            return_list.append(item.text.strip())
        return return_list

    def diagnosis_page(self,page):
        soup = BeautifulSoup(page,'lxml')
        divsection = soup.find('div', class_ = 'jib-articl fr f14 jib-lh-articl')
        return_data = divsection.text.strip()

        return return_data

    def inspect_page(self,page):
        return_list = list()
        soup = BeautifulSoup(page,'lxml')
        checkitems = soup.find_all('li',class_ = 'check-item')
        for item in checkitems:
            return_list.append(item.text)
        return return_list[1:]
