# coding=UTF-8
'''
Created on 

@author: 
'''
from com.asiainfo.utils.HttpUtil import *

  
def sent_http_request_get_test():
    url = "http://localhost:8080/ssm-base/sysmgr/user/service/list" 
    method="GET"
    res = send_http_request(method,url)
    print res

def sent_http_request_post_test():
    url = "http://localhost:8080/ssm-base/sysmgr/user/service/list" 
    method="POST"
    data = {"pageNo":3}
    res = send_http_request(method,url,data)     
    print res

if __name__ == '__main__':
    #sent_http_request_get_test()
    sent_http_request_post_test()
    pass