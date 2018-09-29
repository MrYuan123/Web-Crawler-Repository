#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql,traceback
from enum import Enum

def gene_list(datadict):
    print(datadict)
    returnlist = ['']*16

    for item in datadict:
        print('*'+item+'*')
        if item == '药品名称':
            returnlist[0] = datadict[item]
        elif item == '一级分类':
            returnlist[1] = datadict[item]
        elif item == '二级分类':
            returnlist[2] = datadict[item]
        elif item == '英文名称':
            returnlist[3] = datadict[item]
        elif item == '药物别名':
            returnlist[4] = datadict[item]
        elif item == '药物剂型':
            returnlist[5] = datadict[item]
        elif item == '药理作用':
            returnlist[6] = datadict[item]
        elif item == '药动学':
            returnlist[7] = datadict[item]
        elif item == '适应证':
            returnlist[8] = datadict[item]
        elif item == '禁忌证':
            returnlist[9] = datadict[item]
        elif item == '注意事项':
            returnlist[10] = datadict[item]
        elif item == '不良反应':
            returnlist[11] = datadict[item]
        elif item == '用法用量':
            returnlist[12] = datadict[item]
        elif item == '药物相应作用':
            returnlist[13] = datadict[item]
        elif item == '专家点评':
            returnlist[14] = datadict[item]
        elif item == '相关疾病':
            returnlist[15] = datadict[item]
        else:
            pass

    return returnlist

def insert_data(datadict):
    try:
        db = pymysql.connect("localhost","root","Yyk19951006+","medicine_detail" )
        db.set_charset('utf8')
        cursor = db.cursor()
    except Exception:
        traceback.print_exc()
        return "connection fail!"

    # datal = gene_list(datadict)
    # sql_command = 'insert into medicine_detail(药品名称,一级分类,二级分类,英文名称,药物别名,药物剂型,药理作用,药动学,适应证,禁忌证,注意事项,不良反应,用法用量,药物相应作用,专家点评,相关疾病) VALUES ('
    # for item in datal:
    #     sql_command = sql_command + '\''+item +'\'' +','
    #
    # sql_command = sql_command[:-1] + ");"
    #
    # print(sql_command)
    # cursor.execute(sql_command.format('Null'))
    # db.commit()
    # print("ok")
    # input()

    row1 = 'insert into medicine_detail('
    row2 = '('
    for item in datadict:
        row1 = row1 +item + ','
        row2 = row2 + '\'' + datadict[item]+ '\'' +','

    row1 = row1[:-1]
    row2 = row2[:-1]

    sql_command = row1 + ') values ' + row2 + ');'

    print(sql_command)
    # sql_command = 'insert into medicine_detail(一级分类,二级分类,英文名称,药物别名,药物剂型,药理作用,药动学,适应证,禁忌证,注意事项,不良反应,用法用量,药物相应作用,专家点评,药品名称,相关疾病) values ( a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a);'
    # print(sql_command)
    # input()
    #
    # # sql_command = 'insert into medicine_detail('+'药品名称'+') values ('aaa');'
    # cursor.execute(sql_command.format('Null'))
    # db.commit()
    # print("ok")

    try:
        cursor.execute(sql_command.format('Null'))
        db.commit()
    except Exception:
        db.rollback()
        traceback.print_exc()
        return 'medicine_fail'

    return True
