# coding=UTF-8
'''
Created on 2017年4月18日

@author: zhouxb
'''

def test_oper1():
    x = int("6")
    print type(x)
    y = str(6)
    print type(y)
    str1='hello'
    print len(str1)
    print range(len(str1))
    print range(2,10,3)
    print isinstance(x,int)
    print isinstance(y,dict)
    print isinstance(x,list)
    
def test_file():
    path='D:/Data/workspace3/python01/files/read.txt'
    f = open(path,'w')
    #f = open(path,'a')'''追加
    f.write('您好，Python!');
    f.close()
    print '%s operate ok!' %(path)
    
def test_oper2():
    aList = [1,2,3]
    print aList
    del aList[1]
    print aList
    data =[]
    data.append({"prov":"gd","users":118,"price":2000})
    data.append({"prov":"bj","users":118,"price":1000})
    data.append({"prov":"sh","users":120,"price":500})
    data.sort(key=lambda z:(z["users"], -z['price']), reverse=True)
    print data
    



if __name__ == '__main__':
    test_oper1()
    print '#'*10
    test_file()
    print '#'*10
    test_oper2()
    print '#'*10
    #puple_test()
    #list_test()
    #dic_test()
    #file_test()
    #db_test()
    pass