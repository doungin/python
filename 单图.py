#！ /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
url='https://book.douban.com/latest?icn=index-latestbook-all'
heard={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
res=requests.get(url=url,headers=heard)
html=res.content.decode('utf-8')
pattern=re.compile(r'><img src="(.*?)"/></a>',re.S)
pattern1=re.compile(r'a href="https://book.douban.com/subject/[0-9]{6}/">(.*?)</a>',re.S)
items=pattern.findall(html)
items1=pattern1.findall(html)
for j,i in enumerate(items):
    mew_url=i
    respons=requests.get(url=mew_url,headers=heard)
    tu=respons.content
    print(tu)
    with open(r'E:\zong\{}.jpg'.format(items1[j]),'wb') as f:
        f.write(tu)
    f.close()