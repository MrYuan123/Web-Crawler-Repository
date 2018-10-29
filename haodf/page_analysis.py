#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv
from bs4 import BeautifulSoup
import get_page

class page_analysis(object):
    def __init__(self):
        self.getPage = get_page.get_page()

    def hospital_cat_analysis(self, page):
        soup = BeautifulSoup(page,'lxml')
        tables = soup.find_all('table',class_ = 'bluepanel')
        nsection = tables.pop()
        soupt = BeautifulSoup(str(nsection),'lxml')
        alists = soupt.find_all('a')[:-1]
        flag = 1
        for item in alists:
            print(item.text)
            print(item['href'])
            with open('province_urls.csv','a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow([item.text,item['href']])

            flag += 1
        print(flag)

    def hospital_analysis(self,page):
        soup = BeautifulSoup(page,'lxml')
        tables = soup.find_all('table',class_ = 'bluepanel')
        tables.pop()
        for item in tables:
            soupt = BeautifulSoup(str(item),'lxml')
            alists = soupt.find_all('a')[1:]
            for m in alists:
                print(m.text)
                print(m['href'])
                with open('hospital_urls.csv','a',newline='') as f:
                    writer =csv.writer(f)
                    writer.writerow([m.text,'https:' + m['href']])
        return None

    def introduction_analysis(self,page):
        soup = BeautifulSoup(page, 'lxml')
        namespan = soup.find('div', id = 'ltb')
        fullname = namespan.text.strip()
        temp = soup.find('table',class_ = 'bluepanel')
        return [fullname, temp.text]

    # [rank, type, phone, address, path, department_dict]
    def hospital_detail_analysis(self,page):
        soup = BeautifulSoup(page,'lxml')
        # ======label section
        returnlist = list()
        spanlist = soup.find_all('span',class_ = 'hospital-label-item')
        if len(spanlist) == 0:
            returnlist.append(None)
            returnlist.append(None)
        elif len(spanlist) == 1:
            returnlist.append(None)
            returnlist.append(spanlist[0].text)
        else:
            returnlist.append(spanlist[0].text)
            returnlist.append(spanlist[1].text)


        # ======== address, phone, path
        mapdetail = None
        furtherurl = None
        templist = [None,None,None]
        finda = soup.find_all('a', class_ = 'h-d-c-item-link')
        for item in finda[1:-1]:
            if item['href'] != None:
                furtherurl = 'https:' + item['href']
                break

        if furtherurl == None:
            detailsection = soup.find_all('span',class_ = 'h-d-c-item-text')[1:]
            if len(detailsection) == 3:
                returnlist.append(detailsection[2].text)
                returnlist.append(detailsection[0].text)
                returnlist.append(detailsection[1].text)
            else:
                print('maybe an error!')
                input()
        else:
            furtherpage = self.getPage.get_page(furtherurl)
            soupf = BeautifulSoup(furtherpage,'lxml')
            nowtable = soupf.find_all('table')[4]
            for trdetail in nowtable.select('tr')[5:-2]:
                if '电话' in trdetail.select('td')[0].text:
                    templist[0] = trdetail.select('td')[1].text
                if '地址' in trdetail.select('td')[0].text:
                    templist[1] = trdetail.select('td')[1].text
                if '怎么走' in trdetail.select('td')[0].text:
                    templist[2] = trdetail.select('td')[1].text
            returnlist = returnlist + templist

        # ======== department catrgory
        lilist = soup.find_all('li',class_ = 'f-l-item clearfix')
        department_dict = dict()
        for item in lilist:
            # print('==================================')
            # print(item.select('div')[0].text)
            tempdict = dict()
            for m in item.select('div')[1:]:
                # print(m.select('a')[0].text.strip())
                # print(m.select('a')[0]['href'])
                tempdict[m.select('a')[0].text.strip()] = "https:" + m.select('a')[0]['href']
            department_dict[item.select('div')[0].text] = tempdict
        returnlist.append(department_dict)

        return returnlist

    def comment_analysis(self,page):
        returnlist = [None]*7
        soup = BeautifulSoup(page,'lxml')
        influence = soup.find('div',class_ = 'hospital-influence')
        plists = influence.select('p')

        #p0
        if len(plists[0].select('span')) == 3:
            returnlist[0] = plists[0].select('span')[1].text.strip() + ' ' + plists[0].select('span')[2].text.strip()
            returnlist[1] = None
        elif len(plists[0].select('span')) == 2:
            returnlist[0] = None
            returnlist[1] = None
        else:
            returnlist[0] = plists[0].select('span')[1].text.strip() + ' ' +  plists[0].select('span')[2].text.strip()
            returnlist[1] = plists[0].select('span')[3].text.strip() + ' ' + plists[0].select('span')[4].text.strip()

        # p1
        returnlist[2] = plists[1].select('span')[1].text.strip()

        # p2
        returnlist[3] = plists[2].select('span')[1].text.strip()

        # p3
        returnlist[4] = plists[3].select('span')[2].text.strip()
        returnlist[5] = plists[3].select('span')[4].text.strip()

        # p4
        returnlist[6] = plists[4].select('span')[1].text.strip()

        return returnlist

    def sitemap_analysis(self,page):
        soup = BeautifulSoup(page,'lxml')
        divlist = soup.find_all('div', class_ = 'dis_article_2 clearfix')
        for item in divlist[0].select('a'):
            print(item.text)
            print(item['href'])
            with open('prov_urls.csv','a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow([item.text,'https:' + item['href']])

    def sitemap_hospital(self,url,name):
        page = self.getPage.get_page(url)
        soup = BeautifulSoup(page,'lxml')
        divlist = soup.find_all('div',class_ = 'dis_article_2 clearfix')
        for item in divlist[2].select('a'):
            with open('hospital_cats.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, item.text, 'https://www.haodf.com' + item['href']])
            print(name + ' ' + item.text)
            print('https://www.haodf.com' + item['href'])
        footlist = soup.find('div',class_ = 'dis_article_2 clearfix footer')
        next_url = None
        for item in footlist.select('a'):
            if '下一页' in item.text:
                next_url = 'https://www.haodf.com' + item['href']

        while(next_url != None):
            page = self.getPage.get_page(next_url)
            soup = BeautifulSoup(page,'lxml')
            divlist = soup.find_all('div',class_ = 'dis_article_2 clearfix')
            for item in divlist[1].select('a'):
                with open('hospital_cats.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([name, item.text, 'https://www.haodf.com' + item['href']])
                print(name + ' ' + item.text)
                print('https://www.haodf.com' + item['href'])
            footlist = soup.find('div',class_ = 'dis_article_2 clearfix footer')
            next_url = None
            for item in footlist.select('a'):
                if '下一页' in item.text:
                    next_url = 'https://www.haodf.com' + item['href']

    def sitemap_department_analysis(self,page):
        soup = BeautifulSoup(page,'lxml')
        divlist = soup.find_all('div', class_ = 'dis_article_2 clearfix')
        returnlist = list()
        for item in divlist:
            if '科室' in str(item.h2):
                for m in item.select('a'):
                    dName = m.text
                    dUrl = 'https://www.haodf.com' + m['href']
                    dUrl  = dUrl.replace('sitemap-ys/fac_','faculty/').replace('_1','.htm')
                    returnlist.append([dName,dUrl])

        return returnlist

    def department_detail_analysis(self,page):
        soup = BeautifulSoup(page,'lxml')
        divdata = soup.find('div',id = 'about_det')

        result = divdata.text
        if '暂无科室介绍' in result:
            return None
        else:
            return result.replace('我来添加/修改此科室介绍','').strip()
