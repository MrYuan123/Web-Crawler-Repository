# !/User/bin/python
# -*- coding:utf-8 -*-

import pymysql,traceback


db = pymysql.connect("localhost","root","Yyk19951006+","test" )
cursor = db.cursor()
a = 'hello'
b = 'seddd'
c = 1
sql_command = 'insert into pet(owner,species) values(\'%s\', \'%s\')'%(a,b)
try:
    cursor.execute(sql_command.format('Null'))
    db.commit()
    print('ok')
except Exception:
    db.rollback()
    print("fails!")
    traceback.print_exc()
finally:
    db.close()
