#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import get_page, cat_analysis, detail_section

class start_crawl(object):
    def __init__(self):
        self.getPage = get_page.get_page()
        self.catAna = cat_analysis.cat_analysis()
        self.detailAna = detail_section.detail_analysis()
        self.base_url = 'http://jib.xywy.com/html/'
        self.root_url = 'http://jib.xywy.com'
    def start_crawl(self):
        with open('detail_urls.csv','r') as f:
            reader = csv.reader(f)
            flag = 2022
            for item in reader:
                now_name = item[0]
                now_append_url = item[1]
                now_url = self.root_url + now_append_url
                now_list = list()

                print('==============================')
                print('flag: ' + str(flag))
                print('now_name:' + now_name)
                print('now_url:' + now_url)

                # =================
                # ==treat section==
                treat_url = now_url.replace('il_sii_','il_sii/treat/')
                return_page = self.getPage.get_page(treat_url)
                return_data = self.detailAna.treat_page(return_page)
                now_list.append(return_data['name'])
                if return_data.get("就诊科室"):
                    now_list.append(return_data['就诊科室'])
                else:
                    now_list.append(None)

                if return_data.get('治疗方式'):
                    now_list.append(return_data['治疗方式'])
                else:
                    now_list.append(None)

                if return_data.get('治疗周期'):
                    now_list.append(return_data['治疗周期'])
                else:
                    now_list.append(None)

                if return_data.get('治愈率'):
                    now_list.append(return_data['治愈率'])
                else:
                    now_list.append(None)

                if return_data.get('常用药品'):
                    now_list.append(return_data['常用药品'])
                else:
                    now_list.append(None)

                if return_data.get('治疗费用'):
                    now_list.append(return_data['治疗费用'])
                else:
                    now_list.append(None)

                now_list.append(return_data['治疗具体'])

                # ====================
                # ==symptom section ==
                symptom_url = now_url.replace('il_sii_','il_sii/symptom/')
                return_page = self.getPage.get_page(symptom_url)
                return_data = self.detailAna.symptom_page(return_page)
                now_list.append(return_data)

                # =======================
                # == diagnosis section ==
                diagnosis_url = now_url.replace('il_sii_','il_sii/diagnosis/')
                return_page = self.getPage.get_page(diagnosis_url)
                return_data = self.detailAna.diagnosis_page(return_page)
                now_list.append(return_data)

                # ======================
                # == inspect section ====
                inspect_url = now_url.replace('il_sii_','il_sii/inspect/')
                return_page = self.getPage.get_page(inspect_url)
                return_data = self.detailAna.inspect_page(return_page)
                now_list.append(return_data)

                with open('final_data.csv','a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(now_list)
                print(now_list)
                flag += 1

    def crawl_cat(self):
        with open('cat.csv','r') as f:
            reader = csv.reader(f)
            for item in reader:
                for n in item:
                    now_url = self.base_url + n + '.html'
                    print('=================')
                    print(now_url)
                    return_page = self.getPage.get_page(now_url)
                    return_data = self.catAna.cat_analysis(return_page)
                    print(return_data)
                    for item in return_data:
                        with open('detail_urls.csv','a',newline='') as f:
                            writer = csv.writer(f)
                            temp = [item,return_data[item]]
                            writer.writerow(temp)


if __name__ == "__main__":
    s = start_crawl()
    s.start_crawl()
