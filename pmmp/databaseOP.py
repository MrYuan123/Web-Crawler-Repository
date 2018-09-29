# !/User/bin/python
# -*- coding:utf-8 -*-

import pymysql,traceback

def data_insert(dlist):
    try:
        db = pymysql.connect("localhost","root","Yyk19951006+","disease_detail" )
        db.set_charset('utf8')
        cursor = db.cursor()
    except Exception:
        traceback.print_exc()
        return "connection fail!"

    sql_command1 = 'insert into detail_table1(name,icd,c2,c3,c4) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'%(dlist[0],dlist[1],dlist[2],dlist[3],dlist[4])

    sql_command2 = 'insert into detail_table2(name,icd,c5,c6,c7,c8) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'%(dlist[0],dlist[1],dlist[5],dlist[6],dlist[7],dlist[8])

    sql_command3 = 'insert into detail_table3(name,icd,c9,c10,c11) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'%(dlist[0],dlist[1],dlist[9],dlist[10],dlist[11])

    sql_command4 = 'insert into detail_table4(name,icd,c12) values (\'%s\',\'%s\',\'%s\');'%(dlist[0],dlist[1],dlist[12])
    if len(dlist[16]) == 0:
        c16 = None
    else:
        c16 = pymysql.escape_string(str(dlist[16]))

    if len(dlist[17]) == 0:
        c17 = None
    else:
        c17 = pymysql.escape_string(str(dlist[17]))

    sql_command5 = 'insert into detail_table5(name,icd,c13,c14,c15,c16,c17) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'%(dlist[0],dlist[1],dlist[13],dlist[14],dlist[15],c16,c17)

    print("insert table1")
    try:
        cursor.execute(sql_command1.format('Null'))
        db.commit()
    except Exception:
        db.rollback()
        traceback.print_exc()
        return 'detail_table1'

    print("insert table2")
    try:
        cursor.execute(sql_command2.format('Null'))
        db.commit()
    except Exception:
        db.rollback()
        traceback.print_exc()
        return 'detail_table2'

    print("insert table3")
    try:
        cursor.execute(sql_command3.format('Null'))
        db.commit()
    except Exception:
        db.rollback()
        traceback.print_exc()
        return 'detail_table3'

    print("insert table4")
    try:
        cursor.execute(sql_command4.format('Null'))
        db.commit()
    except Exception:
        db.rollback()
        traceback.print_exc()
        return 'detail_table4'

    print("insert table5")
    try:
        cursor.execute(sql_command5.format('Null'))
        db.commit()
    except Exception:
        db.rollback()
        traceback.print_exc()
        return 'detail_table5'

    return True
