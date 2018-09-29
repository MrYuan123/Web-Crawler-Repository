#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

class detail_analysis(object):
    def __init__(self):
        pass

    def detail_analysis(self,page):
        soup = BeautifulSoup(page,'lxml')
        return_list = list()

        # ======================
        # ====cate arrangement
        # ======================
        cat_list = list()
        cat = soup.find('div',class_ = 'wrap mt10 nav-bar')
        soupT = BeautifulSoup(str(cat),'lxml')
        alist = soupT.find_all('a')
        for item in alist:
            cat_list.append(item.text)
        name = cat_list[len(cat_list)-1]
        return_list.append(name)
        cat_list = cat_list[1:-1]
        return_list.append(str(cat_list))

        # ======================
        # ==== possible disease
        # ======================
        possi_list = list()
        diseasediv = soup.find('div',class_ = 'blood-item panel')
        soupT = BeautifulSoup(str(diseasediv),'lxml')
        diseaseul = soupT.find_all('ul')
        for item in diseaseul[1:]:
            tempsoup = BeautifulSoup(str(item),'lxml')
            details = tempsoup.find_all('li')
            temp = list()
            temp.append(details[0].text.strip())
            temp.append(details[1].text.strip())
            temp.append(details[2].text.strip())
            possi_list.append(temp)
        return_list.append(str(possi_list))

        # =======================
        # ==== relevant symptom
        # =======================
        symptom_list = list()
        symptomdiv = soup.find('div',class_ = 'bor bor-top about-zz')
        soupT = BeautifulSoup(str(symptomdiv),'lxml')
        alist = soupT.find_all('a')
        for item in alist:
            symptom_list.append(item.text)
        return_list.append(str(symptom_list))

        return return_list

    def jieshao_analysis(self,page):
        soup = BeautifulSoup(page,'lxml')
        divsection = soup.find('div',class_ = 'zz-articl fr f14')
        soupT = BeautifulSoup(str(divsection),'lxml')
        plist = soupT.find_all('p')
        detail = plist[len(plist)-1].text.strip().repalce(' ','').replace('\n\n','')

        return detail

    def section_analysis(self, page):
        detail = ''
        soup = BeautifulSoup(page,'lxml')
        divsection = soup.find('div',class_ = 'zz-articl fr f14')
        soupT = BeautifulSoup(str(divsection),'lxml')
        plist = soupT.find_all('p')
        for item in plist:
            detail = detail + item.text

        return detail

    def food_analysis(self,page):
        soup = BeautifulSoup(page,'lxml')
        properfood = soup.find('div',class_ = 'diet-item clearfix ').text.strip().replace(' ','').replace('\n\n','')

        unproperfood = soup.find('div',class_ = 'diet-item none').text.strip().replace(' ','').replace('\n\n','')
        returnlist = [properfood,unproperfood]

        
        return returnlist
