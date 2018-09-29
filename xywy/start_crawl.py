#!/usr/bin/env python
# -*- coding:utf-8 -*-

import get_page,cat_analysis,detail_analysis,databaseOP
import csv

class start_crawl(object):
    def __init__(self):
        self.getPage = get_page.get_page()
        self.catAnalysis = cat_analysis.cat_analysis()
        self.detAnalysis = detail_analysis.detail_analysis()
        self.databaseOP = databaseOP.databaseOP()
        self.base_url = 'http://zzk.xywy.com/p/'

    def start_crawl(self):
        with open('detail_url.csv','r') as f:
            reader = csv.reader(f)
            flag = 415
            for item in reader:
                now_url = 'http://zzk.xywy.com' + item[1]
                # ===================
                # ==== base page ====
                return_page = self.getPage.get_page(now_url)
                return_data = self.detAnalysis.detail_analysis(return_page)
                # print(return_data)

                # ===================
                # == jie shao page ==
                jieshao_url = now_url[:-11] + 'jieshao.html'
                jieshaopage = self.getPage.get_page(jieshao_url)
                jieshaodata = self.detAnalysis.section_analysis(jieshaopage)
                return_data.append(jieshaodata)
                # print(jieshaodata)

                # ===================
                # == yuanyin page ===
                yuanyin_url = now_url[:-11] + 'yuanyin.html'
                yuanyinpage = self.getPage.get_page(yuanyin_url)
                yuanyindata = self.detAnalysis.section_analysis(yuanyinpage)
                return_data.append(yuanyindata)
                # print(yuanyindata)

                # ===================
                # == yufang page ====
                yufang_url = now_url[:-11] + 'yufang.html'
                yufangpage = self.getPage.get_page(yufang_url)
                yufangdata = self.detAnalysis.section_analysis(yufangpage)
                return_data.append(yufangdata)
                # print(yufangdata)

                # ===================
                # == jiancha page ==
                jiancha_url = now_url[:-11] + 'jiancha.html'
                jianchapage = self.getPage.get_page(jiancha_url)
                jianchadata = self.detAnalysis.section_analysis(jianchapage)
                return_data.append(jianchadata)
                # print(jianchadata)

                # ===================
                # == zhenduan page ==
                zhenduan_url = now_url[:-11] + 'zhenduan.html'
                zhenduanpage = self.getPage.get_page(zhenduan_url)
                zhenduandata = self.detAnalysis.section_analysis(zhenduanpage)
                return_data.append(zhenduandata)
                # print(zhenduandata)

                # ===================
                # === food page =====
                food_url = now_url[:-11] + 'food.html'
                foodpage = self.getPage.get_page(food_url)
                fooddata = self.detAnalysis.food_analysis(foodpage)
                return_data.append(fooddata)
                # print(fooddata)

                # self.databaseOP.process_item(return_data)
                with open('final_data.csv','a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(return_data)

                print('======================')
                print('======================')
                print("total:" + str(flag))
                flag += 1
                print(return_data)
                print('======================')
                print('======================')

#爬取目录
    def get_item(self):
        with open('catelog.csv','r') as f:
            reader = csv.reader(f)
            for item in reader:
                append_urls = item[1:]
                for aurl in append_urls:
                    now_url = self.base_url + aurl + '.html'
                    return_page = self.getPage.get_page(now_url)
                    return_page = return_page.encode("iso-8859-1").decode('gbk','ignore')
                    return_data = self.catAnalysis.cat_analysis(return_page)
                    if return_data == None or len(return_data) == 0:
                        print(now_url)
                        print('MAY BE AN ERROR!')
                        input()
                    else:
                        for item in return_data:
                            temp = list()
                            temp.append(item)
                            temp.append(return_data[item])
                            with open("detail_url.csv",'a', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(temp)

if __name__ == "__main__":
    s = start_crawl()
    s.get_item()
    s.start_crawl()
