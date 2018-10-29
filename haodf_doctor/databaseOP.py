# -*- coding: utf-8 -*-
import pymysql,traceback,csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
MYSQL_HOST = '140.143.128.221'
MYSQL_PORT = 2115
MYSQL_USER = 'gpsroot'
MYSQL_DBNAME = 'haodf'
MYSQL_PASSWORD = 'Woyaofacluster8!'

class databaseOP(object):
    def __init__(self):
        self.host = MYSQL_HOST
        self.port = MYSQL_PORT
        self.dbname = MYSQL_DBNAME
        self.password = MYSQL_PASSWORD
        self.user = MYSQL_USER

        try:
            self.db = pymysql.connect(host = self.host, port = self.port, password = self.password, database = self.dbname ,user = self.user)
            self.db.set_charset('utf8')
            self.cursor = self.db.cursor()
            print('database connection success!')
        except Exception:
            traceback.print_exc()
            return "connection fail!"
            input()

        return None

    def process_item(self, item):
        print("insert section:")
        try:
            self.cursor.execute("""insert into recommend_doctors(province, hospital, disease, doctor, hospital_position, academic_position, department) value (%s, %s, %s, %s, %s, %s, %s)""",(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
            self.db.commit()
            print("insert success!")

        except Exception:
            self.db.rollback()
            traceback.print_exc()
            # log(error)
            with open('log_error.csv','a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([item[0],item[1],item[2]])
            print('insert database error!')
            input()


        return item
