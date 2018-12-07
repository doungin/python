import pymysql
import os
abc=pymysql.connect(host='192.168.0.123',port=3306,user='root',password='123456',charset='utf8')
a=abc.cursor()
f=open('a.txt','r+',encoding='utf-8')
f.write('姓名 年龄 班级 性别\n')
for i in range(1,11):
    f.write('小明 21 二班 男\n')
b=f.readlines()
f.close()
a.execute('use text;')
for j in b:
    j=j.replace('\n','')
    c=j.split(' ')
    if c[0]=='姓名':
        a.execute('create table biao33({} char(30),{} char(30),{} char(30),{} char(30));'.format(c[0],c[1],c[2],c[3]))
        break
    else:
        a.execute('insert into biao33 values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))




