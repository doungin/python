# import requests
# import xlwt
# class Shuju(object):
#     def page(self,page):
#         url='https://book.douban.com/top250?start={}'.format(page)
#         response = requests.get(url=url)
#         html = response.content.decode('utf-8')  #字节码
#         print(html)
#         return html
# def guolv(self, a):
#     shuju = []
#     patt = re.compile('<div class="content">(.*?)</div>',re.S)
#     items = patt.findall(a)
#     for i in items:
#         pp = i.replace('<span>','').replace('</span>','')
#         oo = pp.replace(' ','').replace(' ','')
#         oo = oo.replace('<br/>','\n')
#         oo = oo.strip()
#         shuju.append(oo)
#     return shuju
# def save(self,shu):
#     f=xlwt.Workbook(encoding='utf-8')
#     sheet=f.add_sheet(text.xls)
#     sheet.write(0,0,shuju)
#     with open('','a',encoding='utf-8') as f:
#         for i in shu:
#             f.write(i)
# shuju=Shuju()
# shuju.page
# sh = shuju.guolv(shu)
# qiushi.save(sh)




# import requests
# import re
#
#
# url123='http://www.doutula.com/article/list/?page=1'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
# response = requests.get(url=url123,headers=head)
#
# html=response.content.decode('UTF-8')
#
# print(html)
#
# patt = re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
# items = patt.findall(html)
# for i in items:
#     respons = requests.get(url=i,headers=head)
#     html1 = respons.content.decode('UTF-8')
#     patt1 = re.compile(r'<img src="https://ws(.*?) alt')
#     items1 = patt1.findall(html1)
#     print(items1)
# for j,i in enumerate(items1):
#     i = i.replace('"','')
#     i = 'https://ws' + i
#     #保存图片
#     tupian = requests.get(i)
#     res1 = tupian.content
#     with open('{}.jpg'.format(j),'wb') as f:
#         f.write(res1)








import requests
# import re
#
#
# url123='http://www.budejie.com/pic/1'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
# response = requests.get(url=url123,headers=head)
#
# html=response.content.decode('UTF-8')
#
# # print(html)
# patt = re.compile(r'"http://mpic.spriteapp.cn(.*?)1.jpg"')
# items = patt.findall(html)
# print(len(items))
# for j,i in enumerate(items):
#     i = i.replace('"','')
#     i = 'https://mpic.spriteapp.cn' + i + '1.jpg'
#     print(i)
#     tupian = requests.get(i,verify=False)
#     res1 = tupian.content
#     # print(res1)
    # with open(r'C:\Users\doungin\Desktop\新建文件夹{}.jpg'.format(j),'wb') as f:
    #     f.write(res1)
# #
#
#
# import requests
# import re
# class Baisi():
#     def qingqiu(self):
#         url123='http://www.budejie.com/pic/1'
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#         response = requests.get(url=url123,headers=head)
#         html=response.content.decode('UTF-8')
#         return html
#     def guolv(self,html):
#         patt = re.compile(r'"http://mpic.spriteapp.cn(.*?)1.jpg"')
#         items = patt.findall(html)
#         return items
#     def save(self,items):
#         for j,i in enumerate(items):
#             i = i.replace('"','')
#             i = 'https://mpic.spriteapp.cn' + i + '1.jpg'
#             print(i)
#         # 保存图片
#             tupian = requests.get(i,verify=False)
#             res1 = tupian.content
#             with open('{}.jpg'.format(j),'wb') as f:
#                 f.write(res1)




# aaa = baisi.qingqiu()
# bbb = baisi.guolv(aaa)
# baisi.save(bbb)

# import requests
# import re
# ur1='http://www.xiuren.com/'
# res=requests.get(url=url)
# html=res.content.decode('UTF-8')
# patt=re.compile(r'<div class="para" label-module="para">"(.*?)"<sup class="sup--normal" data-sup="8">',re.S)
# items=patt.findall(html)
# print(items)







#
# import re
# import requests
# #获取网址
# url='http://www.doutula.com/article/list/?page=2'                             #获取网址地址
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# abc=requests.get(url=url,headers=head)                                                   #发送请求
# html=abc.content.decode('utf-8')      #用字节码的方式读取，headers=head反爬
# # print(html)
# #过滤图片
# re=re.compile('data-original=(.*?)data-backup',re.S)#用正则表达式过滤
# patt=re.findall(html)       #从网址中过滤图片  结果是列表
# # print(patt)
# for m in patt:
#     m=m.replace('"','')
#     # print(m)
# #保存
# for i,j in enumerate(m):
#     new_url = j                                                                  #赋予新变量
#     respons=requests.get(url=new_url,headers=head)                                  #发送请求
#     tu=respons.content                                                                 #读取图片
#     with open(r'C:\Users\doungin\Desktop\{}.jpg'.format(i),'wb') as f:                     #保存图片
#             f.write(tu)

# import re
# import requests
# url='http://www.xiaohuar.com/s-4-444.html'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# a=requests.get(url=url,headers=head)
# html=a.content.decode('gb2312')
# # print(html)
# re=re.compile('src(.*?)data-bd-imgshare-binde',re.S)
# patt=re.findall(html)
# print(patt)
# for j,i in enumerate(patt):
#     i=i.replace('\n','')
#     with open('{}.txt'.format(j),'w',encoding='utf-8') as f:
#         f.write(i)
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=('192.168.0.21',13245)
s.bind(host)
while True:
    a,b=s.recvfrom(1024)
    print(a.decode('utf-8'))
    msg='你是谁'



    s.sendto(msg.encode('utf-8'),b)

















