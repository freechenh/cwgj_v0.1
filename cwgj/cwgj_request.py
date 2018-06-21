#/usr/bin/python
#encoding:utf-8
import os,sys,django
import requests
pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,pathname)
sys.path.insert(0,os.path.abspath(os.path.join(pathname,'..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mytest.settings")
django.setup()
from cwgj.encrypt import AESECB
from django.views.decorators.csrf import csrf_exempt
import json
sys.path.append('../mytest/')
from ntest.models import case_eg
from mytest import settings



class cwgj():

    @staticmethod
    def ownercar(url,header,content):
        #print(url,header,content)
        rq = requests.post(url=url,headers=header,data=content,verify=False)
        #print(rq.status_code,rq.content)
        res = rq.content
        return res


    # @staticmethod
    # def get_daoban(url,param):
    #     print(url,param)
    #     rq = requests.get(url,params=param,verify=False)
    #     print(rq.content,rq.status_code)
    #     rq_content = rq.content
    #     return rq_content


# a = case_eg.objects.get(case_id=1)
# b = a.url
# c = a.header_parameter
# d = a.content_parameter
# f = eval(c)
# g = eval(d)
# tk = '0D8DF03BDAD8B96274A86EA6BE502E2B'
# print(b)
# print(f,type(f))
# print(g,type(g))
# e = cwgj.ownercar(b,f,g)
# h = AESECB.decrpyt(e,tk)
# print(h)