# coding=UTF-8
'''
Created on 

@author: 
'''
import urllib
import urllib2

def send_http_request(method,reqUrl,reqData={}):
    try:
        req = urllib2.Request(url=reqUrl,data=urllib.urlencode(reqData))
        print req
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        print("Success to request url:%s"%(reqUrl))
        print("Request result:%s"%(res))
    except Exception,msg:
        print("Fail to request url:%s"%(reqUrl))
        print("Error:%s"%(msg))
    
    return res

