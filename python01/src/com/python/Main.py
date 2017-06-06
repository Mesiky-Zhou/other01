# coding=UTF-8
'''
Created on 2017年4月18日

@author: zhouxb
'''
import sys
import os
import shutil
import cx_Oracle

def test():
    print "Hello Word"

# 数字类型  
def number_test():
    x=1
    y=2
    print x,y
    a,b=3,4
    print a,b
    m=n=5
    print m,n
    print '%d + %d = %d' %(m,n, m+n)
    
def string_test():
    str1 = 'python'
    print str1[1:3]
    print str1[:]
    print str1
    print str1[1:]
    print str1[:3]
    
def puple_test():
    p1 = (4,2,'a string')
    print p1
    #p1[0] = 5
    print p1[:]
    print p1[0]
    print p1[-1]
    print p1[1:2]
    print p1[1:]
    
def list_test():
    p1 = [4,2,'a string']
    print p1
    p1[0] = 5
    print p1[:]
    print p1[0]
    print p1[-1]
    print p1[1:2]
    print p1[1:]
    print '#' *10
    for i in p1:
        print i
    print '#' *10
    for i in range(len(p1)):
        print i,p1[i]
        
def dic_test():
    dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
    print dict
    print dict['Alice']
    ''' print dict['x']'''
    for key in dict:
        print key, dict[key]
    print("#########")
    for i,key in enumerate(dict):
        print i, key, dict[key]
        
def file_test():
    dir='D:/Data/workspace3/python01/files'
    for i in os.listdir(dir):
        newFileName = i.replace('part-r-00000','part')
        oldFile = dir + '/' + i
        newFile = dir + '/' + newFileName
        print '%s --> %s' %(i,newFileName)
        shutil.move(oldFile, newFile )
    
def db_test():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8' 
    #os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
    reload(sys)  
    sys.setdefaultencoding("GBK")
    #sys.setdefaultencoding('utf8') 
    username="BOMC50_GD_DEV"
    userpwd="oracledbforgd50"
    host="10.3.3.68"
    port=1521
    dbname="gzdevdb"
    dsn=cx_Oracle.makedsn(host, port, dbname)
    conn=cx_Oracle.connect(username, userpwd, dsn) 
    cursor = conn.cursor() 
    sql = "select login_name, password,user_name from wm_user" 
    cursor.execute(sql) 
    result = cursor.fetchall() 
    count = cursor.rowcount 
    print ("=========中文============" )
    print count
    print ("=====================" )
    for row in result:
        print row[0],row[1],row[2]
    cursor.close()
    conn.close();
    
    


if __name__ == '__main__':
    #test()
    #number_test()
    #string_test()
    #puple_test()
    #list_test()
    #dic_test()
    #file_test()
    #db_test()
    pass