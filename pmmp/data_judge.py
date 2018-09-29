#!/usr/bin/env python
# -*-coding:utf8 -*-
import csv, pymysql,traceback


def get_urls():        # get urls from csv file
    mylist = list()
    with open("disease_data.csv","r") as f:
        reader = csv.reader(f)
        for item in reader:
            temp = list()
            temp.append(item[1]) # name
            temp.append(item[5]) # icd
            temp.append(item[0]) # url
            mylist.append(temp)

    return mylist

def getmysql():
    try:
        db = pymysql.connect("localhost","root","Yyk19951006+","disease_detail" )
        db.set_charset('utf8')
        cursor = db.cursor()
    except Exception:
        traceback.print_exc()
        return "connection fail!"
        input()

    sql_command = 'select name,icd from detail_table5;'

    cursor.execute(sql_command)
    results = cursor.fetchall()
    flag = 1
    returnlist = list()

    for item in results:
        #print(flag)
        flag += 1
        #print(item[0]) # name
        temp = item[0]
        returnlist.append(temp)

    return returnlist


if __name__ == "__main__":
    all_list = get_urls()


    with open('final_data.csv','r') as f:
        final_list = list()
        reader = csv.reader(f)
        flag =1
        for item2 in reader:
            for item1 in all_list:
                print('===================')
                print(flag)
                flag+=1
                print('*'+item1[0]+'*')
                print('*'+item2[0]+"*")
                print('===================')
                if str(item1[0]) == str(item2[0]):
                # if ' '.join(str(item1[0]).split()) == ' '.join(str(item2[0]).split()):
                    print("yes!!!!!!!!!!!!")
                    final_list.append(item1)
                    with open('append_disease.csv','a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(item1)
                        print(item1)

        print(len(all_list))
        print(len(final_list))
    input()




    with open('final_data.csv','r') as f:
        append_list = csv.reader(f)

    dlist = get_urls()
    final_list = list()
    for item in dlist:
        if item not in new_list:
            final_list.append(item)
            print('yes ===============')
            with open('final_data.csv','a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(item)
        else:
            print('No #################')
        print(item)

    print("@@@@@@@@@@@@@")
    print(len(final_list))
    print("@@@@@@@@@@@@@")
    # newlist = dlist + mysqllist
    #
    # dlist = list()
    # for item in newlist:
    #     if item not in dlist:
    #         dlist.append(item)
    # final_list = list()
    # for item1 in dlist:
    #     for item2 in mysqllist:
    #         print(item1[0] + " vs "+ item2)
    #         if ' '.join(str(item1[0]).split()) == ' '.join(str(item2).split()):
    #             print("having this data")
    #             final_list.append(item1)
    #             with open("append_disease.csv",'a', newline='') as f:
    #                 writer = csv.writer(f)
    #                 writer.writerow(item1)
    #         else:
    #             pass
    #
    # # difference = list(set(final_list).difference(set(dlist)))
    # print(len(final_list))
