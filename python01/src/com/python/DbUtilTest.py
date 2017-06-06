# coding=UTF-8
'''
Created on 

@author: 
'''
from com.asiainfo.utils.DbUtil import *

'''
测试SQL脚本：
-- create table p_test01(id int, username varchar2(128),nickname varchar2(128),created date);
drop table p_test01
select * from p_test01
'''

#对查询方法的测试         
def db_query_test():
    sql = "select login_name, password,user_name from wm_user" 
    sql="select * from p_test01 where id=:id"
    result = db_query(sql,{"id":2})
    for index in range(len(result)):
        row = result[index]
        print row[0],row[1],row[2]
    
def db_exec_sql_test():
    #sql = "insert into p_test01 values(1,'zs','张三',sysdate)" 
    #result = db_exec_sql(sql)
    #sql2 = "insert into p_test01 values(:id,:username,:nickname,sysdate)" 
    #params = {"id":2,"username":'hell',"nickname":'世界'}
    #result = db_exec_sql(sql2,params)
    result = db_exec_sql("update p_test01 set username=:username where id=:id",{"id":2,"username":'lisi'})
    if result:
        print('执行成功')
    else:
        print('执行失败')
      


if __name__ == '__main__':
    #db_query_test()
    db_exec_sql_test()
    pass