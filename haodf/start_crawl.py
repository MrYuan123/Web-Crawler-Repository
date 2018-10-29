#!/usr/bin/env python
# -*- coding:utf-8 -*-
import get_page, page_analysis,databaseOP
import csv,time,random

class start_crawl(object):
    def __init__(self):
        self.getPage = get_page.get_page()
        self.pageA = page_analysis.page_analysis()
        self.databaseOP = databaseOP.databaseOP()
    def start_crawl(self):
        # catrgory section crawler(finish)
        # now_url = 'https://q.haodf.com/'
        # page = self.getPage.get_page(now_url)
        # returndata = self.pageA.hospital_cat_analysis(page)

        # get hospitals section
        # now_url = 'https://q.haodf.com/'
        with open('province_urls.csv','r') as f:
            reader = csv.reader(f)
            for item in reader:
                print('======================')
                print('======================')
                print(item[0])
                now_url = 'https:' + item[1]
                page = self.getPage.get_page(now_url)
                returndata = self.pageA.hospital_analysis(page)

    def detail_analysis(self):
        with open('hospital_urls.csv','r') as f:
            reader = csv.reader(f)
            flag = 3013
            for item in reader:
                now_name = item[0]
                now_url = item[1][:-4] + '/jieshao.htm'
                print("===========================")
                print('===========================')
                print(now_name)
                print(now_url)
                print(flag)
                sleeptime = random.uniform(0,2)
                print('sleep:' + str(sleeptime))
                time.sleep(sleeptime)

                page = self.getPage.get_page(now_url)
                returndata = self.pageA.introduction_analysis(page)
                with open('introductions.csv','a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([now_name,returndata[0],returndata[1]])

                flag += 1

    def hospital_detail(self):
        with open("hospital_urls.csv",'r') as f:
            reader = csv.reader(f)
            flag = 5179
            for item in reader:
                now_name = item[0]
                now_url = item[1]
                page = self.getPage.get_page(now_url)
                returndata = self.pageA.hospital_detail_analysis(page)

                departments = returndata.pop()
                tempdict = dict()
                department_list = list()
                for item in departments:
                    details = list()
                    for n in departments[item].keys():
                        details.append(n)
                    tempdict[item] = details
                    # for m in departments[item]:
                    #     with open('departments_lists.csv','a',newline='') as f:
                    #         writer = csv.writer(f)
                    #         writer.writerow([now_name, item, m, departments[item][m]])

                returndata.append(tempdict)
                finaldata = [now_name,now_url] + returndata
                with open('hospital_details.csv','a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(finaldata)

                print('==================')
                print(now_name)
                print(now_url)
                print(flag)
                print(finaldata)
                flag += 1
                sleeptime = random.uniform(0,2)
                print('sleep:' + str(sleeptime))
                time.sleep(sleeptime)

    def doctor_crawl(self):
        pass

    def comment_crawl(self):
        with open("hospital_urls.csv",'r') as f:
            reader = csv.reader(f)
            flag = 7639
            for item in reader:
                now_name = item[0]
                now_url = item[1]
                print('=====================')
                print(now_name)
                print(now_url)
                print(flag)

                page = self.getPage.get_page(now_url)
                returndata = self.pageA.comment_analysis(page)
                writelist = [now_name,now_url] + returndata
                with open('comment_data.csv','a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(writelist)
                print(returndata)
                # sleeptime = random.uniform(0,2)
                # print('sleep:' + str(sleeptime))
                # time.sleep(sleeptime)
                flag += 1

    def sitemap_crawl(self):
        # now_url = 'https://www.haodf.com/sitemap.html'
        # page = self.getPage.get_page(now_url)
        # returndata = self.pageA.sitemap_analysis(page)
        with open('prov_urls.csv','r') as f:
            reader = csv.reader(f)
            for item in reader:
                now_url = item[1]
                now_name = item[0]
                self.pageA.sitemap_hospital(now_url,now_name)

    def sitemap_department(self):
        with open('hospital_cats.csv','r') as f:
            reader = csv.reader(f)
            for item in reader:
                now_prov = item[0]
                now_hospital = item[1]
                now_url = item[2]

                print('=====================')
                print('province: '+ now_prov)
                print('hospital: ' + now_hospital)
                print('url: ' + now_url)
                page = self.getPage.get_page(now_url)
                returndata = self.pageA.sitemap_department_analysis(page)

                for item in returndata:
                    if now_hospital in item[0]:
                        pass
                    else:
                        with open('department_urls.csv','a',newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([now_prov,now_hospital] + item)
                            print(item)

                sleeptime = random.uniform(0,2)
                print('sleep:' + str(sleeptime))
                time.sleep(sleeptime)

    def department_detail(self):
        flag = 95624
        with open('department_urls.csv','r') as f:
            reader = csv.reader(f)
            for item in reader:
                now_prov = item[0]
                now_hospital = item[1]
                now_department = item[2]
                now_url = item[3]
                now_url = now_url[:-4] + '/jieshao.htm'
                print('======================')
                print('now province: ' + now_prov)
                print('now hospital: ' + now_hospital)
                print('now department: ' + now_department)
                print('now url: ' + now_url)
                print('flag: ' + str(flag))
                enter = 1
                while enter == 1:
                    try:
                        page = self.getPage.get_page(now_url)
                        returndata = self.pageA.department_detail_analysis(page)
                        enter = 0
                    except:
                        print('avoid Anti_crawl!')
                        # sleeptime = random.uniform(0,4)
                        sleeptime = 2
                        print('sleep:' + str(sleeptime))
                        time.sleep(sleeptime)

                wlist = [now_prov,now_hospital,now_department,returndata]
                self.databaseOP.process_item(wlist)
                # with open("department_data.csv",'a',newline='') as f:
                #     writer = csv.writer(f)
                #     wlist = [now_prov,now_hospital,now_department,returndata]
                #     writer.writerow(wlist)
                if returndata == None:
                    print('Finish! It is None.')
                else:
                    print('Finish! len of the data is:' + str(len(returndata)))

                # sleeptime = random.uniform(0,2)
                # print('regular sleep:' + str(sleeptime))
                # time.sleep(sleeptime)

                flag += 1


if __name__ == '__main__':
    s = start_crawl()
    s.department_detail()
