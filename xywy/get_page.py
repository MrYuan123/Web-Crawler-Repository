# -*- coding: utf-8 -*-
import requests, time

class get_page(object):
    def __init__(self):
        self.header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}

    def get_page(self, url):
        while True:
            flag = 3
            # proxy = self.redisOP.get_proxy()
            while flag>0:
                try:
                    page = requests.get(url, headers = self.header)
                    # print(page.encoding)
                    page_detail = page.text.encode("iso-8859-1").decode('gbk','ignore')
                    return page_detail

                except requests.exceptions.ConnectionError:
                    print("ConnectionError -- please wait 5 seconds")
                    time.sleep(5)
                    flag = flag - 1
                except requests.exceptions.ChunkedEncodingError:
                    print('ChunkedEncodingError -- please wait 5 seconds')
                    time.sleep(5)
                    flag = flag - 1
                except:
                    print('Unfortunitely -- An Unknow Error Happened, Please wait 5 seconds')
                    time.sleep(5)
                    flag = flag - 1
