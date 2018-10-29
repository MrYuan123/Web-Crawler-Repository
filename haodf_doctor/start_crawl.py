#!/usr/bin/env python
# -*- coding:utf-8 -*-
import get_page, page_analysis,databaseOP
import csv,time,random

class start_crawl(object):
    def __init__(self):
        self.getPage = get_page.get_page()
        self.pageA = page_analysis.page_analysis()
        self.databaseOP = databaseOP.databaseOP()
        # self.databaseOP = databaseOP.databaseOP()
    def start_crawl(self):
        with open('hospital_cats.csv','r') as f:
            reader = csv.reader(f)
            hospital_flag = 1
            for hospital_detail in reader:
                # relevant_list
                doctorlist = list()

                hospital_flag += 1
                now_prov = hospital_detail[0]
                now_hospital = hospital_detail[1]
                now_url = hospital_detail[2]

                judge = 1
                flag = 1
                emptyflag = 1
                while judge == 1:
                    print('===================')
                    print('province: ' + now_prov)
                    print('hospital: ' + now_hospital)
                    print('url: ' + now_url)
                    print('hospital flag:' + str(hospital_flag))
                    print('page flag: ' + str(flag))


                    try:
                        page = self.getPage.get_page(now_url)
                        returndata = self.pageA.first_page_analysis(page)
                        recommand_dict = returndata[0]
                        doctor_dict = returndata[1]
                        errorflag = returndata[2]
                        next_page = returndata[3]

                        print(recommand_dict)
                        print(doctor_dict)
                        print(errorflag)
                        if errorflag == 1:
                            print('guess there is another redirection!')
                            sleeptime = 2
                            print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                            time.sleep(sleeptime)
                        elif errorflag == 0:
                            if len(recommand_dict) == 0 and len(doctor_dict) == 0:
                                print('empty page!')
                                sleeptime = 2
                                print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                                time.sleep(sleeptime)
                            else:
                                for ditem in doctor_dict:
                                    doctorlist.append([ditem,doctor_dict[ditem]])
                                flag += 1
                                judge = 0

                        elif errorflag == 2:
                            print('this is truely a empty page!')
                            if emptyflag < 7:
                                sleeptime = 2
                                print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                                time.sleep(sleeptime)
                            else:
                                with open('empty_hospitals.csv','a',newline='') as f:
                                    writer = csv.writer(f)
                                    writer.writerow([now_prov,now_hospital,now_url])
                                flag += 1
                                judge = 0
                        else:
                            print('error!')
                            input()
                    except:
                        sleeptime = 2
                        print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                        time.sleep(sleeptime)

                    emptyflag += 1

                while next_page != None:
                    print('===================')
                    print('province: ' + now_prov)
                    print('hospital: ' + now_hospital)
                    print('url: ' + next_page)
                    print('hospital flag:' + str(hospital_flag))
                    print('page flag: ' + str(flag))

                    try:
                        page = self.getPage.get_page(next_page)
                        returndata = self.pageA.page_analysis(page)
                        doctor_dict = returndata[0]
                        errorflag = returndata[1]
                        if errorflag == 1:
                            print('guess there is another redirection!')
                            sleeptime = 2
                            print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                            time.sleep(sleeptime)
                        else:
                            if len(doctor_dict) == 0:
                                print('empty page!')
                                sleeptime = 2
                                print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                                time.sleep(sleeptime)
                            else:
                                next_page = returndata[2]
                                for ditem in doctor_dict:
                                    doctorlist.append([ditem,doctor_dict[ditem]])
                                print(doctor_dict)
                                flag += 1

                    except:
                        sleeptime = 2
                        print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                        time.sleep(sleeptime)


                for item in recommand_dict:
                    with open('recommand_lists.csv','a',newline='') as f:
                        writer = csv.writer(f)
                        templist = [now_prov, now_hospital, item, recommand_dict[item]]
                        writer.writerow(templist)
                for item in doctorlist:
                    with open('doctors.csv','a',newline='') as f:
                        writer = csv.writer(f)
                        templist = [now_prov,now_hospital, item[0], item[1]]
                        writer.writerow(templist)
                print('writer into files successfully!')

    def doctor_detail(self):
        now_prov = '北京'
        now_hospital = '北京协和医院'
        now_doctor = '蔡柏蔷'
        now_url = 'https://www.haodf.com/doctor/DE4r08xQdKSLBvHcvNv5LwmK7DLi.htm'
        page = self.getPage.get_page(now_url)
        returndata = self.pageA.doctor_analysis(page)
        return

    def recommend_detail(self):
        with open('recommand_lists.csv','r') as f:
            reader = csv.reader(f)
            hospital_flag = 36930

            for items in reader:
                now_prov = items[0]
                now_hospital = items[1]
                now_disease = items[2]
                now_url = items[3]
                flag = 1
                datalist = []
                page_flag = 1

                while flag == 1:
                    print('==============================')
                    print("==============================")
                    print('province: ' + now_prov)
                    print('hospital: ' + now_hospital)
                    print('now_disease: ' + now_disease)
                    print('hospital flag:' + str(hospital_flag))
                    print('page flag:' + str(page_flag))
                    print('url: ' + now_url)

                    returnpage = self.getPage.recommend_page(now_url)
                    base_url = returnpage[0]
                    page = returnpage[1]
                    returnlist = self.pageA.recommend_analysis(page)

                    if returnlist == None:
                        print('wrong page!')
                        sleeptime = 2
                        print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                        time.sleep(sleeptime)
                    elif returnlist == 'empty':
                        print('this is an empty page')
                        with open('emptypage.csv','a', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([now_prov, now_hospital, now_disease, now_url])
                        flag = 0
                        next_url = None
                    else:
                        if len(returnlist) == 0:
                            print('return empty data!')
                            sleeptime = 2
                            print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                            time.sleep(sleeptime)
                        else:
                            print(returnlist)
                            for now_item in returnlist[:-1]:
                                datalist.append([now_prov, now_hospital, now_disease] + now_item)
                            page_flag += 1
                            if returnlist[-1] == None:
                                next_url = None
                            else:
                                next_url = base_url + returnlist[-1]
                            flag = 0

                while next_url != None:
                    print('==============================')
                    print("==============================")
                    print('province: ' + now_prov)
                    print('hospital: ' + now_hospital)
                    print('now_disease: ' + now_disease)
                    print('hospital flag:' + str(hospital_flag))
                    print('page flag:' + str(page_flag))
                    print('url: ' + next_url)

                    returndata = self.getPage.recommend_page(next_url)
                    page = returndata[1]
                    returnlist = self.pageA.recommend_analysis(page)
                    if returnlist == None:
                        print('wrong page!')
                        sleeptime = 2
                        print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                        time.sleep(sleeptime)

                    elif returnlist == 'empty':
                        print('this is an empty page')
                        with open('emptypage.csv','a', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([now_prov, now_hospital, now_disease, now_url])
                        next_url = None
                    else:
                        if len(returnlist) == 0:
                            print('return empty data!')
                            sleeptime = 2
                            print('avoid anti_crawler!============' + 'sleep: ' + str(sleeptime) + 's')
                            time.sleep(sleeptime)
                        else:
                            print(returnlist)
                            for now_item in returnlist[:-1]:
                                datalist.append([now_prov, now_hospital, now_disease] + now_item)
                            page_flag += 1

                            if returnlist[-1] == None:
                                next_url = None
                            else:
                                next_url = base_url + returnlist[-1]
                            flag = 0

                for result_item in datalist:
                    self.databaseOP.process_item(result_item)
                    # with open('recommend_doctors.csv', 'a', newline='') as f:
                    #     writer = csv.writer(f)
                    #     writer.writerow(result_item)

                hospital_flag += 1
        return


if __name__ == '__main__':
    s = start_crawl()
    # s.doctor_detail()
    s.recommend_detail()
