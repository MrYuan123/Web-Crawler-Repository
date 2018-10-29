#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv
from bs4 import BeautifulSoup
import get_page

class page_analysis(object):
    def __init__(self):
        self.getPage = get_page.get_page()

    # analyze the first page of hospital's map page
    def first_page_analysis(self,page):
        returnlist = []
        soup = BeautifulSoup(page,'lxml')

        divlists = soup.find_all("div", class_ = 'dis_article_2 clearfix')
        recommand_doctor = dict()
        doctor_dict = dict()
        if len(divlists) != None:
            for divdata in divlists:
                if '推荐专家' in str(divdata.h2):
                    for item in divdata.select('a')[1:]:
                        recommand_doctor[item.text] = 'https:' + item['href']
                if '医生' in str(divdata.h2):
                    for item in divdata.select('a'):
                        doctor_dict[item.text] = 'https:' + item['href']

            if len(recommand_doctor) == 0 and len(doctor_dict) == 0:
                errorflag = 2
            else:
                errorflag = 0
        else:
            errorflag = 1
        returnlist.append(recommand_doctor)
        returnlist.append(doctor_dict)
        returnlist.append(errorflag)

        # find next_page link
        next_page = None
        divdata = soup.find('div',class_ = 'dis_article_2 clearfix footer')
        if divdata != None:
            for item in divdata.select('a'):
                if '下一页' in item.text:
                    next_page = 'https://www.haodf.com' + item['href']

        returnlist.append(next_page)
        return returnlist

    # analyze further page of hospital's map page
    def page_analysis(self,page):
        returnlist = list()
        soup = BeautifulSoup(page,'lxml')
        # doctor data
        divlists = soup.find_all("div", class_ = 'dis_article_2 clearfix')
        doctor_dict = dict()
        errorflag = 0
        if divlists != None:
            for divdata in divlists:
                if '医生' in str(divdata.h2):
                    for item in divdata.select('a'):
                        doctor_dict[item.text] = 'https:' + item['href']
        else:
            errorflag = 1

        returnlist.append(doctor_dict)
        returnlist.append(errorflag)

        # find next page
        next_page = None
        divdata = soup.find('div',class_ = 'dis_article_2 clearfix footer')
        if divdata != None:
            for item in divdata.select('a'):
                if '下一页' in item.text:
                    next_page = 'https://www.haodf.com' + item['href']

        returnlist.append(next_page)

        return returnlist

    # analyze doctor's detail page
    def doctor_analysis(self,page):
        print(page)
        input()
        # soup = BeautifulSoup(page,'lxml')
        # scriptlist = soup.select('script')
        # for item in scriptlist:
        #     print('====================')
        #     print('====================')
        #     print(item)

    def recommend_analysis(self,page):
        returnlist = list()
        soup = BeautifulSoup(page,'lxml')

        # doctor section
        doctorlist = soup.find_all('tr',class_ = 'yy_jb_df2')
        find_logo = soup.find('div', id = 'headpA_blue')
        
        if find_logo != None and len(doctorlist) == 0:
            return 'empty'
        elif find_logo != None and len(doctorlist) != 0:
            for item in doctorlist:
                tritems = item.select('tr')
                trlength = len(tritems)

                if trlength == 4:
                    name = tritems[0].text.strip()
                    hospital_position = tritems[1].text.strip()
                    academic_position = tritems[2].text.strip()
                    department = tritems[3].text.strip()
                elif trlength == 3:
                    name = tritems[0].text.strip()
                    hospital_position = tritems[1].text.strip()
                    academic_position = None
                    department = tritems[2].text.strip()
                else:
                    print('there is a error!')
                    input()
                temp_list = [name, hospital_position, academic_position, department]
                returnlist.append(temp_list)

            # next page section
            next_page = None
            pagelist = soup.find('div', class_ = 'p_bar')
            if pagelist == None:
                pass
            else:
                alist = pagelist.select('a')
                if alist == None:
                    pass
                else:
                    for item in alist:
                        if '下一页' in item.text:
                            next_page = item['href']

            returnlist.append(next_page)

            return returnlist

        else:
            print('unexpected error!')
            return None
