# -*- coding:utf-8 -*-
import csv
import requests,time

def get_urls():
    return_list = list()
    with open('imgs.csv', 'r') as f:
        reader = csv.reader(f)
        for item in reader:
            return_list.append(item)
    return return_list

def crawl_img(url):
    print('start crawl')
    while True:
        try:
            image = requests.get(url, stream=True)
            image_detail = image.content
            break
        except requests.exceptions.ConnectionError:
            print("ConnectionError -- please wait 10 seconds")
            time.sleep(10)
        except requests.exceptions.ChunkedEncodingError:
            print('ChunkedEncodingError -- please wait 10 seconds')
            time.sleep(10)
        except:
            print('Unfortunitely -- An Unknow Error Happened, Please wait 10 seconds')
            time.sleep(10)
    return image_detail

def store_img(title, img_detail, name, url):
    try:
        with open(title, 'wb') as f:
            f.write(img_detail)

        print("store success!")
    except:
        with open('img_error.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name,url])
        print('install error :' + title)
    return

if __name__ == "__main__":
    base_url = 'http://pmmp.cnki.net/cdd'
    urls = get_urls()
    flag = 1

    for item in urls:
        print("+++++++++++++++")
        name = item[0]
        print(name)
        print("+++++++++++++++")
        item = item[1:]
        if len(item) == 0:
            pass
        else:
            count = 1
            for n in item:
                n = n[2:]
                url = base_url + n
                url = url.replace(" ","%20")
                print(url)
                print(flag)
                image_detail = crawl_img(url)
                imgPATH = './imgs/' + name + str(count) + '.jpg'
                store_img(imgPATH, image_detail, name, url)

                flag +=1
                count +=1
            print('====================')
