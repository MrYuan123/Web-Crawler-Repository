# -*- coding: utf-8 -*-
import requests, time
import random

class get_page(object):
    def __init__(self):
        self.header = {"User-Agent":None}
        self.user_agents = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36']

    def get_page(self, url):
        while True:
            flag = 1
            # proxy = self.redisOP.get_proxy()
            while flag == 1:
                try:
                    now_header = self.header
                    now_header['User-Agent'] = self.user_agents[random.randint(0,3)]
                    # print(now_header)
                    page = requests.get(url, headers = now_header)

                    if str(page.url).strip() == url.strip():
                        flag = 0
                        return page.text
                    else:
                        print('there is redirection! url is not same!')

                except requests.exceptions.ConnectionError:
                    print("ConnectionError -- please wait 5 seconds")
                    time.sleep(5)

                except requests.exceptions.ChunkedEncodingError:
                    print('ChunkedEncodingError -- please wait 5 seconds')
                    time.sleep(5)

                except:
                    print('Unfortunitely -- An Unknow Error Happened, Please wait 5 seconds')
                    time.sleep(5)

    def recommend_page(self, url):
        while True:
            flag = 1
            # proxy = self.redisOP.get_proxy()
            while flag == 1:
                try:
                    now_header = self.header
                    now_header['User-Agent'] = self.user_agents[random.randint(0,3)]
                    # print(now_header)
                    page = requests.get(url, headers = now_header)
                    return [page.url, page.text]


                except requests.exceptions.ConnectionError:
                    print("ConnectionError -- please wait 5 seconds")
                    time.sleep(5)

                except requests.exceptions.ChunkedEncodingError:
                    print('ChunkedEncodingError -- please wait 5 seconds')
                    time.sleep(5)

                except:
                    print('Unfortunitely -- An Unknow Error Happened, Please wait 5 seconds')
                    time.sleep(5)
