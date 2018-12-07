# import pymysql
# import os
# abc=pymysql.connect(host='192.168.0.123',port=3306,user='root',password='123456',charset='utf8')
# a=abc.cursor()
# a.execute('use text;')
# with open('c.txt','r+',encoding='utf-8') as f:
#     b=f.readlines()
#     print(b)
#     for i in b:
#         i=i.replace('\n','')
#         d=i.split(',')
#         print(d)
#         if d[0]=="姓名":
#             a.execute('create table ym12({} char(30),{} char(30),{} char(30));'.format(d[0],d[1],d[2]))
#             continue
#         else:
#             a.execute('insert into ym12 values("{}","{}","{}");'.format(d[0],d[1],d[2]))
a=[1,2,3,4]
for i in a:
    for j in a:
        for e in a:
            if i!=j and j!=e and e!=i:
                print(i*100+j*10+e)