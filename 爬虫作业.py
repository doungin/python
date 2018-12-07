import re
import requests
import os
url='https://www.doutula.com/article/list/?page=2'
head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
res=requests.get(url=url,headers=head)
html=res.content.decode('UTF-8')
patt=re.compile(r'https://www.doutula.com/article/detail/[0-9]{7}',re.S)
patt1=re.compile(r'<div class="random_title">(.*?)<div class="date">')
items=patt.findall(html)
title = patt1.findall(html)
for q,i in enumerate(items):
    # print(title)
    os.mkdir(r'C:\Users\doungin\Desktop\新建文件夹\新建文件夹\{}'.format(title[q]))
    i=i.replace( '">' ,'')
    url=i
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    res = requests.get(url=url, headers=head)
    html1 = res.content.decode('UTF-8')
    patt1 = re.compile(r'onerror="this.src=(.*?)"', re.S)
    patt2=re.compile(r'<td align="center" class="wr pl">(.*?)</td>')
    items1=patt1.findall(html1)
    items2=patt2.findall(html1)
    # print(items2)
    for k,j in enumerate(items1):
        j = j.replace(',', '')
        j = j.replace("'", '')
        if "jpg" in j:
            tupian = requests.get(j)
            res1 = tupian.content
            with open(r'C:\Users\doungin\Desktop\新建文件夹\新建文件夹\{}\{}.jpg'.format(title[q],items2[k]),'wb') as f:
                f.write(res1)
        elif "jpeg" in j:
            tupian = requests.get(j)
            res1 = tupian.content
            with open(r'C:\Users\doungin\Desktop\新建文件夹\新建文件夹\{}\{}.jpeg'.format(title[q], items2[k]), 'wb') as f:
                f.write(res1)
        elif "png" in j :
            tupian = requests.get(j)
            res1 = tupian.content
            with open(r'C:\Users\doungin\Desktop\新建文件夹\新建文件夹\{}\{}.png'.format(title[q], items2[k]), 'wb') as f:
                f.write(res1)
        else:
            tupian = requests.get(j)
            res1 = tupian.content
            with open(r'C:\Users\doungin\Desktop\新建文件夹\新建文件夹\{}\{}.gif'.format(title[q], items2[k]), 'wb') as f:
                f.write(res1)
















#
#
#f
# import re
# import requests
# import os
# def wangzhi():
#     url='https://www.doutula.com/article/list/?page=2'
#     head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#     res=requests.get(url=url,headers=head)
#     html=res.content.decode('UTF-8')
#     patt=re.compile(r'https://www.doutula.com/article/detail/[0-9]{7}',re.S)
#     items=patt.findall(html)
#     return items
# a=wangzhi()
# print(a)
# def baocun(b):
#     for q,i in enumerate(b):
#         i=i.replace( '">' ,'')
#         os.mkdir(r'C:\Users\doungin\Desktop\新建文件夹{}'.format(q))
#         # print(i)
#         url=i
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#         res = requests.get(url=url, headers=head)
#         html1 = res.content.decode('UTF-8')
#         patt1 = re.compile(r'onerror="this.src=(.*?)"', re.S)
#         items1=patt1.findall(html1)
#         # print(items1)
#         for k,j in enumerate(items1):
#             j=j.replace(',','')
#             j=j.replace("'",'')
#             tupian = requests.get(j)
#             res1 = tupian.content
#             with open(r'C:\Users\doungin\Desktop\新建文件夹{}\{}.jpg'.format(q,k), 'wb') as f:
#                 f.write(res1)
# baocun(a)
# import socket
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# soc.connect(('192.168.0.21',13245))
# aaa='asdf'
# soc.send(aaa.encode('utf-8'))
# msg=soc.recv(1024)
# print(msg.decode('utf-8'))
