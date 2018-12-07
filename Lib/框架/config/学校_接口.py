#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
def 学校快查(a):
    url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
    querystring = {'filterInput': '{}'.format(a)}
    head = {
                'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
            }
    re = requests.get(url=url, headers=head, params=querystring)
    html = re.json()
            # print(html)

            # 自带的断言
            # assert html['code']==0   #判断预期的结果是否与断言的结果一致
    return html
def 学校考试快查(self,a):
    pass
def 学校列表(self):
    pass

