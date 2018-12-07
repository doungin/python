#!/usr/bin/env  python
#-*- coding:utf-8 -*-
# import xlrd
# def tes_数据():
#     shuju=[]
#     f=xlrd.open_workbook(r'C:\Users\doungin\Desktop\接口.xlsx')
#     sheet=f.sheet_by_name('Sheet1')
#     num=sheet.nrows
#     for i in range(1,num):
#         aaa=sheet.row_values(i)
#         shuju.append(aaa)
#     return shuju
# print(tes_数据())
import pymysql
import requests
import re
import xlwt
url='https://www.zhipin.com/job_detail/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&scity=101010100&industry=&position='
head={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
res=requests.get(url=url,headers=head)
html=res.content.decode('utf-8')
# print(html)
patt1=re.compile('<div class="job-title">(.*?)</div>',re.S)
patt2=re.compile('<span class="red">(.*?)</span>',re.S)
patt3=re.compile('_custompage" target="_blank">(.*?)</a></h3>',re.S)
items1=patt1.findall(html)
items2=patt2.findall(html)
items3=patt3.findall(html)
abc=pymysql.connect(host='192.168.0.123',port=3306,user='root',password='123456',charset='utf8')
a=abc.cursor()
a.execute('use text;')
a.execute('create table y(公司名称 char(30),工资 char(30),职业 char(30));')
for i in range(len(items1)):
    a.execute('insert into y values("{}","{}","{}");'.format(items3[i],items2[i],items1[i]))
