#库导txt
# import pymysql
# adc=pymysql.connect(host='192.168.0.38',port=3306,user='root',password='123456',charset='utf8')
# a=adc.cursor()
# a.execute('use xcz')
# a.execute('select * from oyy;')
# d=a.fetchall()
# a.execute('desc oyy;')
# v=a.fetchall()
# with open('x.txt','w+',encoding='utf-8') as f:
#         f.write('{},{},{}'.format(v[0][0],v[1][0],v[2][0]))
#         for j  in d:
#             f.write('\n{},{},{}'.format(j[0],j[1],j[2]))

#库导xls
# import xlwt
# import pymysql
# adc=pymysql.connect(host='192.168.0.38',port=3306,user='root',password='123456',charset='utf8')
# a=adc.cursor()
# a.execute('use xcz;')
# a.execute('select * from oyy;')
# c=a.fetchall()
# a.execute('desc oyy;')
# d=a.fetchall()
# o=xlwt.Workbook(encoding='utf-8')
# sheet=o.add_sheet('天选之人')
# for i in range(len(d)):
#     sheet.write(0,i,d[i][0])
#     for j in range(len(c)):
#         sheet.write(j+1,i,c[j][i])
# o.save('x.xls')

#TXT导xls
# import xlwt
# with open('a.txt','r+',encoding='utf-8') as  f:
#     a=f.readlines()
# g=xlwt.Workbook(encoding='utf-8')
# sheet=g.add_sheet('这是色子')
# for i,j in enumerate(a):
#     j=j.replace('\n','')
#     c=j.split(',')
#     for r in range(3):
#         sheet.write(i,r,c[r])
# g.save('z.xls')


#txt导数据库
# import xlwt
# import pymysql
# adc=pymysql.connect(host='192.168.0.38',port=3306,user='root',password='123456',charset='utf8')
# a=adc.cursor()
# a.execute('use xcz')
# with open('x.txt','r+',encoding='utf-8') as f:
#     b=f.readlines()
#     for i  in b:
#         i=i.replace('\n','')
#         p=i.split(',')
#         if p[0]=='姓名':
#             a.execute('create table yy({} char(100),{} char(100),{}  int);'.format(p[0],p[1],p[2]))
#         else:
#             a.execute('insert into  yy  values("{}","{}","{}");'.format(p[0],p[1],p[2]))
# adc.commit()

#txt导表格
# import xlwt
# with open('a.txt','r+',encoding='utf-8') as f:
#     c=f.readlines()
# ad=xlwt.Workbook(encoding='utf-8')
# sheet=ad.add_sheet('创建')
# for j,i in enumerate(c):
#     i=i.replace('\n','')
#     d=i.split(',')
#     for h in range(3):
#         sheet.write(j,h,d[h])
# ad.save('www.xls')


#脚本

#质数之和
# s=0
# for i in range(2,100):
#     for j in  range(2,i):
#         if i%j==0:
#             break
#     else:
#         s+=i
# print(s)

# def zhishu(a,b):
#     s=0
#     for i in range(a,b):
#         for j in range(a,i):
#             if i%j==0:
#                 break
#         else:
#             s+=i
#     return(s)
# a=zhishu(2,100)
# print(a)

# import requests
# import re
# url='https://book.douban.com/latest?icn=index-latestbook-all'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77'}
# adc=requests.get(url=url,headers=head)
# html=adc.content.decode('utf-8')
# att=re.compile('"><img src="(.*?)"/></a>')
# aff=att.findall(html)
# print(aff)
# for  i,j in enumerate(aff):
#     new_j=j
#     ddd=requests.get(new_j)
#     htmll=ddd.content
#     with open('{}.jpg'.format(i),'wb') as  f:
#         f.write(htmll)

# import os
# for i in range(40):
#     os.remove('{}.jpg'.format(i))

# 猜大小
import random
a=random.randrange(1,10)
while True:
    q = int(input('请输入数字'))
    if q<a:
        print('小了')
    elif q>a:
        print('大了')
    else:
        print('答对了')
        break