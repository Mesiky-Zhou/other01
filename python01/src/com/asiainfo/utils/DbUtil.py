# coding=UTF-8
'''
Created on 

@author: 
'''
import sys
import os
import cx_Oracle

db_ip="10.3.3.68"
db_port=1521
db_sid="gzdevdb"
db_username="BOMC50_GD_DEV"
db_password="oracledbforgd50"

def db_connect():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8' 
    #os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
    reload(sys)  
    sys.setdefaultencoding("GBK") #sys.setdefaultencoding('utf8') 
    dsn=cx_Oracle.makedsn(db_ip, db_port, db_sid)
    conn=cx_Oracle.connect(db_username, db_password, dsn) 
    return conn

#执行查询，可以传入params参数，也可以不用传，params使用dic的形式传入
def db_query(sql,params={}):
    resultList = []
    try:
        conn=db_connect();
        cursor = conn.cursor() 
        cursor.execute(sql,params) 
        result = cursor.fetchall() 
        count = cursor.rowcount 
        print ('Execute sql: %s. \nTotal count : %d.' %(sql, count))
        
        for row in result:
            #print row[0],row[1],row[2]
            resultList.append(row)
    except Exception,msg:
        print ('Fail to execute sql: %s. \nError message : %s' %(sql, msg))
    finally:
        cursor.close()
        conn.close();
        
    return resultList

#执行插入、更新、删除，执行成功返回true,执行失败返回false
#可以传入params参数，也可以不用传，params使用dic的形式传入
def db_exec_sql(sql,params={}):
    try:
        result=True
        conn=db_connect();
        cursor = conn.cursor() 
        cursor.execute(sql,params) 
        conn.commit()
        print ('Execute sql: %s. \nExecute result : %s.' %(sql, result))
    except Exception,msg:
        result=False
        conn.rollback()
        print ('Fail to execute sql: %s. \nError message : %s' %(sql, msg))
    finally:
        cursor.close()
        conn.close();
    return result
 
