# -*- coding: utf-8 -*-
import get_page, page_analysis,csv, detail_analysis

class start_crawl(object):
    def __init__(self):
        self.getPage = get_page.get_page()
        self.pageAnalysis = page_analysis.page_analysis()
        self.detailAnalysis = detail_analysis.detail_analysis()
        # self.url = "http://jbk.39.net/jiancha/search/"

    def start_crawl(self):
        with open("ini_url.csv",'r') as f:
            reader = csv.reader(f)
            for item in reader:
                print(item[0])
                print(item[1])
                now_url = self.url + item[1] + '/'
                flag = 1
                while now_url != None:
                    print('===============================')
                    print(item[0])
                    print(now_url)
                    print(flag)
                    print('===============================')
                    page_detail = self.getPage.get_page(now_url)
                    return_data = self.pageAnalysis.page_analysis(page_detail)
                    for now_detail in return_data['crawl_data']:
                        now_detail.append(item[0])
                        with open('first_cat.csv','a',newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(now_detail)

                    print(return_data['crawl_data'])
                    print(return_data['next_url'])

                    if return_data['next_url'] == None:
                        now_url = None
                        print('finish')
                    else:
                        now_url = 'http://jbk.39.net' + return_data['next_url']
                    flag +=1

    def start_detail(self):
        with open('error.csv','r') as f:
            reader = csv.reader(f)
            for item in reader:
                print('==================================')
                print('==================================')
                print(item[0])
                print(item[1])
                now_url = item[1]
                page_detail = self.getPage.get_page(now_url)
                page_detail = page_detail.encode("iso-8859-1").decode('gbk','ignore')
                return_data = self.detailAnalysis.detail_analysis(page_detail)

                # [name, position, price, tags, intro, 检查部位：， 科室, 空腹检查, details]
                temp = list()
                temp.append(item[0])
                temp.append(item[3])
                temp.append(item[2])
                temp.append(return_data['tags'])
                temp.append(return_data['intro'])
                temp.append(return_data['检查部位：'])
                temp.append(return_data['科室：'])
                temp.append(return_data['空腹检查：'])
                temp.append(return_data['details'])
                with open('39_data.csv','a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(temp)

                print(temp)
                print('==================================')
                print('==================================')
if __name__ == "__main__":
    s = start_crawl()
    # s.start_crawl()
    s.start_detail()
