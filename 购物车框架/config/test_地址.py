#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
def 默认地址快查(a):
    url = 'http://www.zhaoapi.cn/user/setAddr?uid={}&addrid=14303&status=1'.format(a)
    # querystring = {''.format(a)}
    head = {'token': '3A33D677AA9EDF27EE96308A9BAF251E'}
    re = requests.get(url=url, headers=head)
    html = re.json()
            # print(html)

            # 自带的断言
            # assert html['code']==0   #判断预期的结果是否与断言的结果一致
    return html
# print(默认地址快查(22707))

