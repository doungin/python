#/usr/bin/env.python
# -*- coding:utf
#
#
#
# -8 -*-

# print(a[3][0][-3])
# a.insert(2.'abc')#第一个从参数是下标位置，第二个参数是添加的元素
# print(a)
# a.remove("qwe")#删除某个元素
# print(a)
# a.pop(a)#删除下标位置所在的元素
# print(a)
# c=a.index(5)#获取某元素的下标值
# print(c)
# c=a.count(2)#统计某元素在列表中的个数
# print(c)
#第二个python中的内置函数 len() 统计某数据类型中有多少个元素
# r="123,123"
# d=len(r)
# print(d)
# import copy
# c=["z","a","A","Z","zsd"]
# b=[123,34,1,4]
# a=[2,"qwe",2,5,b]
# a.reverse()# 反转列表
# b.reverse()
# print(a)
# c.sort()#排序 默认是升序(元素必须是统一类型)
# print(c)
# b.sort(reverse=True)#倒序
# print(b)
# a.clear()#清空
# b=copy(a)#复制（浅复制，只能复制第一层的数据）
# d=copy.deepcopy(a)#深复制，复制全部数据
# print(d)
#tuple(元组)    一组数据的集合，都是用来存储数据的
#以小括号为标识，一逗号隔开，只有一个元素的时候结尾加,
# a = (12,234,154,"432")
# b=a.count(12)#统计某元素在元组中的个数
# a.index(234)#统计某元素下标位置的值
# print(b)



#dict（字典）  存储数据的，数据格式：key=value
#以键值的方式储存数据
#以大括号为标识，以逗号隔开
#特点：1，可变的，2无序的，3不支持索引
#字典中的键（key）必须是唯一的
# a={"name":"小明","sec":[90,80,100],"age":"小明"}
# a["aaa"]
# b={"wer":132}
#添加
# a["hhh"]=123456
# print(a)
#a.pop("name")  #删除key所在的键值对
#a.poptiem()# 默认删除最后一个
# b=a.keys()#获取所有的key
# c=a.values()#获取所有的值
# b=a.items()#获取所有的键值对
#不支持缩印：不支持通过下标位置取值
#支持通过key取值
# print(b)
# a.update(b)#将字典里b中的所有元素更新到a中
# a["name"]="123"#覆盖name为123
# print(a)



# set(集合)  一组数据的集合，存储数据的
#以大括号来标识的，以逗号分隔开的{1,2,34,54,7}
# 特点：1，不重复的  2，无序的  3，不支持索引  4,可变的
# a={12,312,234,54,65}
# b={12,132,34,56,65,75,43,2,2,4,5,1,1}

# a.update(b)#将集合中的所有元素更新到a中
# print(a)
# #并集 |，交集 &，差集-
# c=a|b
# print(c)
# c=a&b
# print(c)
# c=a-b
# print(c)
# a='1234'
# b=str(a)
# print(type(a))
# a=[123,123,134,5,786,97,234,1]
# b=set(a)
# c=list(b)
# c.sort()
# print(c)
# 不需要加命令
# 整除（//）除（/）
# 通数据类型直接可以运算
# a=[123]*4
# print(a)
# 比较运算符  >  <  ==等于    =!不等于  >=  <=
# 成员运算符  in  和  not in
# a=[12,234,53]
# print(4 not in a)
# 逻辑运算符    与and    或or    非not
# 赋值运算符  += -= *= /= //= **=
# a=3+4
# a+=5   等于 a=a+5
# print(a)
# 基础语句
# 判断语句，循环语句，异常处理语句，上下文管理语句
# 判断语句 格式
# if 条件：（冒号）
# （缩进）严格控制缩进 执行语句
# else
#        执行语句
# a=input('手动输入字符串')
# if a.startswith("a"):
#     if a.endswith("c"):
#      print("hello word")
#     else:
#      print("hello")
# elif a.startswith("c"):
#      print("word")
# else:
#     print(123)



# a=input("输入一组数字")
# f=list(a)
# f.sort()
# b=int(f[0])
# c=int(f[1])
# d=int(f[2])
# if b+c>d:
#     if b**2+c**2<d**2:
#         print("钝角")
#     elif b**2+c**2==d**2:
#         print("直角")
#     elif b**2+c**2>d**2:
#         print("锐角")
# else:
#     print("不是三角形")
#



# 循环语句 for while
# for 语句 格式：
# 注意： 1，没有do和done   2，注意冒号和缩进     3,
# for 变量名 in 范围：    范围：指的事一组数据的集合
#     执行语句
#     执行语句
#     执行语句
# print(sum(range(101)))
# b=0
# for i in range(1,101):
#     b=b+i
# print(b)



# a={'name':123,'age':123}
# for i,j in a.items():
#  print(j)



# b=0
# c=0
# for i in range(1,100,2):
#   b+=i
# for j in range(2,100,2):
#   c=c+j
# f=b-c
# print(f)




# a=["电脑",'计算机','MP3']
# for i,j in enumerate(a):
#     print(i+1,j)
# b=int(input(("输入")))
# print(a[b-1])
#
#
#
# 嵌套语句    循环语句中嵌套
# 循环嵌套判断  for 语句中  if 语句
# b=0
# for a in range(1,100):
#     if a % 2 != 0:
#         b=b+a
#     else:
#         b=b-a
# print(b)

#


# import random
# a=random.randrange(1,10)
#
# for i in range(0,3,1):
#     b = int(input("请输入一个数字"))
#     if b == a:
#         print("正确")
#         break
#     if b>a:
#         print('大了')
#         print("你还有{}次机会".format(2-i))
#     if b<a:
#         print('小了')
#         print('你还有{}次机会'.format(2-i))
#         continue
# else:
#  print("笨蛋")
#
#

# for i in  range(1,10):
#     for j in range(1,i+1):
#          print('{}*{}={}'.format(i,j,j*i),end='\t')
#     print()
#
#
#
# d=0
# for i in range(2,100):
#   for j in range(2,i+1):
#      if i % j == 0:
#        break
#   if i==j:
#       d=d+i
# print(d)
#
#
# for·····else····语句           只要没被break掉就执行else语句
# a = ['qwd','sdw','asd']
# for i in a:
#     if len(i) ==2:
#         break
# else:
#     print("完美")






#/usr/bin/env.python
#-*- conding:utf-8 -*-
# a=int(input("请输入一组数字"))
# print(a)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end="\t")
#     print()





# /usr/bin/env.python
# -*- conding:utf-8 -*-
# a=[3,23,4,1,3,3,5,3,2,1,2,1,2]
# for i in a:
#     if a.count(i) > 1:
#         for j in range(a.count(i)-1):
#             a.remove(i)
# print(a)



# /usr/bin/env.python
# -*- conding:utf-8 -*-
# while 循环   格式；while条件；

# whlie条件：
#  执行语句
#  执行语句
#  ·······
# 打印三次 hello word
# a=1
# s=0
# while a < 101:
#     s=s+a
#     a=a+1
# print(s)


# import random
# a=random.randrange(1,10)
# while a < 10:
#     b = int(input("请输入一个数字"))
#     if b > a:
#      print('大了')
#     if a > b:
#      print('小了')
#     if b==a:
#      print("对了")


# while True:
#     while True:
#         for i in range(10):
#             if i==10:
#                 break
#             else:
#                 print(i)
#         break
#     break
# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#         j+=1
#     i=i+1
#     print()






# for i in range(3):
#     print('hello world')


# for 通常用于有序列的数据
# while 循环通过用于根据条件循环
# a=[23,13,45,12,2]
# b=len(a)
# for i in range(1,b):
#     for j in range(1,b):








# a=(2,34,12,45)
# print(sum(a)/4)


# while True:
#     a=input('手动输入一组数')
#     if a == 'exit':
#         break
#     else:
#         b=a.split(',')
#         c=len(b)
#         for i,j in enumerate(b):
#             b[i]=int(j)
#         print(sum(b)/c)
#         for f in b:
#             if f < sum(b)/c:
#                 print(f)
#
# print(c)



# a='123'
# b='='.join(a)
# print(b)







# 对文件的操作   open()函数
# 格式  open('文件名','权限','编码方式')
# 批量操作
# 文件名：如果不加路径就是在当前目录下执行
# 如果目录下有该文件名，那么操作的就是该文件里执行
# 如果有路径的话，要在路径前加\\标识不转义或者在路径前加r也是不转义
# 权限：代码对文件的操作权限   w写（只能写入字符串），r读，a追加
# write具备不换行的功能
# read读取的是文件中的所有内容，他把所有内容变成一串字符串，打印出来
#readlines（）读取出所有文件内容，结果是一个列表
# readline()本身自己会叠加，第一个第一行，第二个第二行
# w   r   a
# w+  r+  a+
#wb   rb  ab  图片
# f=open('C:\\Users\\doungin\\Desktop\\a.txt','a',encoding='utf-8')    # q打开一个空文件
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write('{}+{}={}  '.format(i,j,i*j))
#     f.write('\n')


# f.close()
# f=open('C:\\Users\\doungin\\Desktop\\桌面壁纸\\519afff8ee3c2.jpg','rb')
# f.read()
# f.close()

# 上下文管理器   with 语句   原理：_enter_    _exit_
# 对上下文的打开和关闭强制执行的操作
# 格式：   with  打开的文件  as  变量名：
# a='''apoisjdapsd
# aoijdoaisjd
# oiasjdoaijsdo
# aoisdjaosijd
# owiudqiwhjd
# aoisdjaosidj
# oiqwjdoiqwjd
# oiqjwdoiqjwd
# '''
# for i in range(1,11):
#     i=open('{}.txt'.format(i), 'w+', encoding="utf-8")
#     i.write(a)
# i.close()
#
# with open('a.txt','r+',encoding="utf-8") as f:
#     b=f.readlines()
#     a=len(b)
# for i in b:
#     if i=='\n' or i.startswith('#'):
#         a=a-1
# print(a)
#     f.write(a)
#     f.close



# a=0
# for i in range(1,101):
#     a=a+i
# print(a)


# 因数之和
# for i in range(1,101):
#     b=0
#     for j in range(1,i):
#         if i%j==0:
#             b=b+j
#     if  i==b:
#         print(i)


# a=input("请输入数字")
# b=a.split(",")
# b.sort()
# print(b)



# 针对某一种异常或多种异常去处理
# try:
#     a='123'
#     print(a+1)
# except NameError:    #默认处理所有的异常
#     print('hello')
# except TypeError:
#     print('123')
# except AttributeError:
#     print("234")
# except Exception:   #Exception标识所有异常
#     print('告辞')

# 当你只想处理一种异常是，在except语句后面加上异常类型如:TypeError
# 报错的格式





# try···except···else···  原理：只要try语句中的代码没有异常，就执行else
# try:
#     a='123'
#     print(a+1)
# except TypeError as c:
#     print(c)
#     print('有病')
# else:
#     print('没病')

# try···except···finally   原理：finally语句一定能执行


#raise  #触发异常
# a=123
# raise TypeError('出错')
# print(a)



# random

# 导入语句#把要使用的库导入到本文件中    import语句
# import day2
# day2.yinshu()


# from day2 import yinshu
# 下载方式：1.pip下载   pip是python自带的一个组件，用来下载网络上的python库
#         2.python 文件名
#         3.setting中下载
# from day2 improt zhishu #从day2这个文件中导入zhishu函数
# print(zhishu())
# from day2 improt *  #从day2这个文件中导入所有函数
# /usr/bin/env.python
# -*-  coding:utf-8 -*-



# 面向对象：将函数进行分类和封装，使开发更高效
# 面向过程：解决问题的过程
# 发邮件，操作数据库，操作OS，爬虫，
# 在python上同伙 类 来实现某个对象的功能
# 类：属性 方法
# object




#     def jiujiu(self):   #self也是类的实例化
#         print('hello')
#
# class shuzi():
#     def jiecheng(self):
#         s=1
#         d=0
#         for i in range(1,6):
#             s+=i
#             d+=s
#         return d
#
#     def zhishu(self):
#         b=self.jiecheng()
#         s=0
#         for i in range(2,100):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 s+=i
#         return s
# print(shuzi().jiecheng())
# print(shuzi().zhishu())







# 面向对象：将函数进行分类和封装，使开发更高效
# 面向过程：解决问题的过程
# 发邮件，操作数据库，操作OS，爬虫，
# 在python上同伙 类 来实现某个对象的功能
# 类：属性 方法
# object
#对象：是类的实体化
# 继承：一个新的类拥有旧的类的所有方法
# class asd(shuzi):
#       pass #空语句
# asd=asd()
# asd().jiujiu()
# print(asd.zhishu())
# 多继承：一个新的类具有多个旧的类的所有方法
# 如果继承的多个类里面有相同的方法，使用的事最左边的类里面的
# 多态：方法重写
# 私有方法：只属于本类的方法
# 定义私有方法：方法名前面加两个下划线
# class asd():
#     def aaa(self):
#         print(123)
#
# class bbb(asd,shuzi):
#     def aaa(self):
#         a=0
#         for i in range(101):
#             a+=i
#         print(a)
#
# bb=bbb()
# bb.aaa()


# class Shuzi():#为了跟函数名区分，第一个字母大写
#     name='小刚'
#     nianji=10
#     def __init__(self,a,b):#初始化属化
#         self.name=a
#         self.nianji=b
#     def jiecheng(self):
#         print("hello")
#     def zhishu(self):
#         print('hello %s,今年%d岁'%(self.name,self.nianji))



# import pymysql
#连接数据库

# abc=pymysql.connect(host='192.168.0.123',
#                     port=3306,
#                     user='root',
#                     password='654321',
#                     charset='utf8')
#创建一个游标


# aaa.execute('show databases;')#执行sql语句
# aaa.execute('use test1;')
# aaa.execute('show tables;')
# print(aaa.fetchmany(5))#读取上一句sql语句的几个几个结果（元组）
# print(aaa.fetchall())#读取上一句sql语句的结果(元组)
# print(aaa.fetchone())#读取一个结果，有累积的效果
# aaa=abc.cursor()
# aaa.execute('create database bbq;')
# aaa.execute('use bbq;')
# aaa.execute('create table biao3(name char(255),age int,banji char(255));')
# list1 = ['小张',1,'班级']
# for i in range(30):
#     aaa.execute('insert into biao3 values ("{}","{}","{}");'.format(list1[0],list1[1]+i,list1[2]))
#     abc.commit()
# aaa.execute('select * from  biao3;')
# for i in aaa.fetchall():
#     print(i)
#
# aaa=abc.cursor()
# aaa.execute('use bbq')
# aaa.execute('select * from biao3;')
# shuju = aaa.fetchall()
# aaa.execute('desc biao3;')
# biaotou=aaa.fetchall()
# with open('a.txt','w+',encoding='utf-8') as f:
#     for i in range(len(biaotou)):
#         if i == len(biaotou):
#             f.write(biaotou[1][0])
#         else:
#             f.write(biaotou[i][0]+',')
#     for j in shuju:
#         f.write('\n'+'{},{},{}'.format(j[0],j[1],j[2]))


#



# OS模块：python自带的模块
# 作用：python与操作系统直接的交换
import os
# a=os.popen('ping 8.8.8.8')#执行windows命令
# print(a.read())
# os.chdir(r'D:\Users\doungin\PycharmProjects')#切换目录
# print(os.getcwd())#获取当前所在的目录
# os.mkdir('sad')#创建目录，如果不加路径就在当前目录下创建
# os.makedirs('aaa\sda')#创建递归目录
# os.rmdir('sad')#删除空目录
# os.remove('‪C:\\Users\\doungin\\Desktop\\abc.txt')#删除文件
# print(os.listdir())#获取当前目录下的所有文件
# os.rename('day1.py','脚本.py')#更改文件名
# print(os.path.split(r'‪C:\Users\doungin\Desktop\abc.txt'))#将文件的文件名与路径分隔开
# print(os.path.splitext(r'‪C:\Users\doungin\Desktop\abc.txt'))#将文件的后缀名与前面分隔开
# print(os.path.isfile('__pycache__'))#判断是否为普通文件
# print(os.path.isdir('__pycache__'))#判断是否为目录文件
# print(os.path.islink('__pycache__'))#判断是否为链接文件

# a=0
# b=0
# os.chdir()
# for i in os.listdir():
#     if os.path.isfile(i):
#         a+=1
#         print(a)
#     else:
#         b+=1
#         print(b)
# a=[i for i in os.listdir() if os.path.isfile(i)]
# b=[y for y in os.listdir() if os.path.isfile(y)]
# print(len(a))
# print(len(a),len(b))



#xlwt 需要下载的模块  作用：给excel表格写入数据
#xlrd               作用：读取excel表格中的数据
# xlutils             作用：给excel表格中追加数据
# import xlwt
#打开一个文件
# f=xlwt.Workbook(encoding='utf-8')
#添加一个标签页
# sheet = f.add_sheet#('python操作excel表格')
#写入数据
#第一个数字代表多少行，第一行从0开始
#第二个数字代表多少列，第一列从0开始
#第三个字符串代表写入的内容
# sheet.write(0, 0, '姓名')
# sheet.write(0, 1, '年龄')
# sheet.write(0, 2, '班级')
# for i in range(1,31):
#     sheet.write(i, 0, '小明')
#     sheet.write(i, 1, '18')
#     sheet.write(i, 2, '软件')
# 保存文件
# f.save('doungin.txt')



# import pymysql
# abc=pymysql.connect(host='192.168.0.123',
#                     port=3306,
#                     user='root',
#                     password='654321',
#                     charset='utf8')
# aaa.execute('show databases;')#执行sql语句
# aaa.execute('use test1;')
# aaa.execute('show tables;')
# print(aaa.fetchmany(5))#读取上一句sql语句的几个几个结果（元组）
# print(aaa.fetchall())#读取上一句sql语句的结果(元组)
# print(aaa.fetchone())#读取一个结果，有累积的效果
# aaa=abc.cursor()
# a=abc.cursor()
# a.execute('show databases;')
# a.execute('use test1;')
# a.execute('show tables;')
# a.execute('select * from stu;')
# print(a.fetchall())




# import xlrd
# import os
# import pymysql
# abc=pymysql.connect(host='192.168.0.123',
#                     port=3306,
#                     user='root',
#                     password='654321',
#                     charset='utf8')
# a=abc.cursor()
# with open('doungin.txt','r',encoding='utf-8') as f:
#     b=f.readlines()
# c=b[1].split(" ")
# print(c)
# a.execute('create database haizeiwan;')
# a.execute('use haizeiwan;')
# a.execute('create table doungin(姓名 char(30),年龄 int,性别 char(30));')
# a.execute('insert into doungin values("{}","{}","{}");'.format(c[0],c[1],c[2]))
# a.execute('select * from doungin;')
# print(a.fetchall())






# f = xlwt.Workbook(encoding='utf-8')
# os.chdir(r'D:\Users\doungin\PycharmProjects\untitled')
#
#
# 读取
# 打开一个文件
# f=xlrd.open_workbook('text.xls')
# 两种获取标签页
# 1，同过索引来获取
#  sheet=f.sheets()[0]                               #索引获取标签页
#2，通过名称获取
# print(f.sheet_names())                        #获取所有标签页的名称
# sheet=f.sheet_by_name('python操作excel表格')      #括号内填写操作的标签
# sheet=f.nsheets                               #获取有多少个标签页
# print(sheet.nrows)                               #获取文件有多少行
# print(sheet.row_values(0))                    #row_values 读取第几行的内容 第一行从0开始
# a=sheet.nrows
# for i in range(a):
#     print(sheet.row_values(i))                     # 取出列表中所有内容
# print(sheet.ncols)                                  #获取有多少列
# print(sheet.col_values(0))                         #获取第几列的所有内容
# print(sheet.cell(0,0).value)                        #读取某一个单元格的内容






# import xlrd
# from xlutils.copy import copy
# f = xlrd.open_workbook('text.xls')                #复制文件
# new_f = copy(f)                             #操作复制的文件
# sheet=new_f.get_sheet(0)                    #通过索引来获取
# sheet.write(5,10,'哈哈哈')                    #写入
# new_f.save('text.xls')
#
#
#
# python包和模块的区别


# import  paramiko                   #封装ssh协议  作用：远程连接
# ssh123=paramiko.SSHClient()#创建一个ssh客户端
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())#把将要连接的主机添加到know_hosts 文件中
# ssh123.connect(hostname='192.168.0.123',
#                port=22,
#                username='root',
#                password='doungin')
# 执行命令  产生三个结果
# stuin,stuout,stuerr=ssh123.exec_command('ls -al')
#第一个变量，执行的命令，输入#第二个变量：命令的结果，输出#第三个变量：命令的报错
# print(stuout.read().decode())
# ssh123.close()#断开连接
# while True:
#     a=input('请输入命令')
#     stuin,stuout,stuerr=ssh123.exec_command(a)
#     print(stuout.read().decode())
#     if a == 'exit':
#         break
# ssh123.close()
# ssh123=paramiko.Transport(('192.168.0.123',22))# 创建一个传输通道
# ssh123.connect(username='root',password='doungin')
# sftp=paramiko.SFTPClient.from_transport(ssh123)        #传输文件使用sftp协议    创建一个sftp的实例
# sftp.get('源文件路径','目的路径')                       #get 是从linux下载文件到本地windows
# sftp.put('文件','路径')                         #put  从windows上传Linux上
# sftp.put('脚本.py','/etc/aaa.py')
# sftp.close()





# 发送邮件

# import smtplib  #发送邮件协议
# import email.mime.text  #处理   发送的内容
# import email.mime.multipart #处理发送的内容
#
# sender='doungln@163.com'
# recver='13346647595@163.com'
# server='stmp:163.com'
# passwd='doungin20222'
# message=email.mime.multipart.MIMEMultipart()
# message['from']=sender
# message['to']=recver
# message['subject']='python报告'
# text='''
# 大圣你好啊
# 晚上来玩啊
# '''
# text=email.mime.text.MIMEText(text)
# message.attach(text)
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,passwd)
# smtp123.sendmail(sender,recver,message.as_string())
# smtp123.close()



















import smtplib  # 发送邮件的协议
# import email.mime.text  # 处理发送的内容
# import email.mime.multipart  #  处理邮件的表头

# sender = 'doungln@163.com'  #  发送者
# recver = ['m15037109541@163.com',
#           'xcz201807@163.com']   #  接收者
# server = 'smtp.163.com'          #  服务器地址
# passwd = 'doungin20222'             #  授权码

# message = email.mime.multipart.MIMEMultipart()      #创建一个空邮件

# message['from'] = sender                                #发件人

# message['to'] = ','.join(recver)                            #收件人

# message['subject'] = 'python lenrn'                         #主题
# text ='''小真真'''
# text = email.mime.text.MIMEText(text)                   # 处理文本信息

# message.attach(text)                                    #将处理后的信息添加到邮件里
# att2=email.mime.text.MIMEText(open('int.py','rb').read(),'base64','utf-8')
# att2['Content-Type']='appolication/octet-stream'
# att2['Content-Disposition']='attachment; filename="int.py"'
# message.attach(att2)


# smtp123 = smtplib.SMTP_SSL(server,465)                    #定义服务器和端口

# smtp123.login(sender,passwd)                           # 登录服务器

# smtp123.sendmail(sender,recver,message.as_string())     #发送邮件

# smtp123.close()                                             #断开连接
#
#
#



































# 时间模块
# import time
# print(time.time())                                  #时间戳   从公元1970年到现在经历的秒
# print(time.localtime())                #本地时间  元组   默认显示当前时间  参数：填时间戳
# print(time.localtime(1540025315))
# print(time.strftime('%Y %m %d %H-%M-%S %w',time.localtime())) #将本地时间格式化成现代化时间
# print(time.strptime('1970 12 12','%Y %m %H'))       #将现代化的时间格式化成本地时间
# a=time.strptime('1970 12 12','%Y %m %H')            #将元祖的时间转换成时间戳
# print(time.mktime(a))
# b=(1978,12,12,12,23,33,3,123,0)                      #必须有九位，后三位无意义
# print(time.mktime(b))
# time.sleep(2)   #休眠
# print(123)
#输入一个现代化时期（年月日）
#输出，今年是否为闰年，今天是星期几，今天是一年中的第几天
# def nianyue(a):
    # d=a.split(' ')
# def riqi(a,b,c):
#     d=time.strptime('{} {} {}'.format(a,b,c),'%Y %m %d')
#     e=d[0]
#     if e % 4 ==0 and e%100 != 0:
#         print(e, '是闰年')
#         print('星期', d[-3] + 1)
#         print('今天是第', d[-2], '天')
#     elif e % 400 ==0:
#         print(e,'是闰年')
#         print('星期', d[-3] + 1)
#         print('今天是第', d[-2], '天')
#     else:
#         print(e,'不是闰年')
#         print('星期',d[-3]+1)
#         print('今天是第',d[-2],'天')
# riqi(2018,10,22)
#




# requests 第三方库需要下载
#爬虫  又叫  网络蜘蛛（spider）
# 模仿浏览器的模块，根据自己制定的规则批量下载网络中的资源
# 正则表达式：匹配文件中的内容
# 模仿浏览器的模块：urllip.   urllip3    requests
# 匹配内容的模块：re，  bs4， xpath
# 爬虫分类：  1，聚焦爬虫（只爬取某个网站的资源）
#             2,搜索爬虫（爬取整个网络中的资源）
# 面向对象代码    爬虫第一步，分析网址的变化

import requests

#requests  第三方库需要下载
#爬虫 ：又叫网络蜘蛛（spider）
#模仿浏览器 ，根据自己制定的规则批量下载网络中的资源
#正则表达式：匹配文件中的内容
#模仿浏览器的模块：urllib,urllib3,requests
#匹配内容的的模块：re，bs4，xpath
#爬虫分类：1.聚焦爬虫（只爬取某个网站的资源） 2.搜索爬虫（爬取整个网络中的资源）

#面向对象的代码  爬虫的第一步：分析网址的变化,并请求
#                    第二步：分析html文件，过滤并下载想要的资源
#                    第三步：保存。注意保存的权限和格式


# class Qiushi(object):
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         response = requests.get(url=url)# 发送请求
#             读取结果的方式：1.以字符串的方式读取 2.以字节码的方式读取
        # print(response.text)         #字符串
        # html = response.content.decode('utf-8')  #字节码
        # print(html)

        # return html
    #
    # def guolv(self,a):
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
    #     with open('a.txt','a',encoding='utf-8') as f:
    #         for i in shu:
    #             f.write(i)
#
# qiushi=Qiushi()
# qiushi.qingqiu(2)
# sh = qiushi.guolv(jieguo)
# qiushi.save(sh)
#




# 反爬虫机制
#1.组织爬虫程序批量
#2.验证码
# import requests
# import os
# import re
# url123='http://www.doutula.com/article/list/?page=1'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
# response=requests.get(url=url123,headers=head)
# html=response.content.decode('UTF-8')
# print(html)
# patt=re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
# items=patt.findall(html)
# print(len(items))
# for i in items:
#     respons=requests.get(url=i,headers=head)
#     html1=respons.content.decode('UTF-8')
#     patt1=re.compile(r'<img src="https://ws(.*?) alt"')
#     items1=patt1.findall(html1)
# for i in enumerate(items):
#
#
#
#
# 1，面向对象           多个具有某种功能的课重复使用的函数的集合
# 2，豆瓣
# 3，列表推导式
# 4，导入

#
# import pymysql
# import os
# abc=pymysql.connect(host='192.168.0.123',port=3306,user='root',password='123456',charset='utf8')
# a=abc.cursor()
# f=open('文本','r+',encoding='utf-8')
# f.write('姓名 年龄 班级 性别\n')
# for i in range(1,11):
#     f.write('小明 21 二班 男\n')
# b=f.readlines()
# print(b)
# f.close()
# a.execute('use text;')
#
# for j in b:
#     j=j.replace('\n','')
#     c = j.split(' ')
#     if c[0]=='姓名':
#         a.execute('create table biao10({} char(30),{} char(30),{} char(30),{} char(30));'.format(c[0],c[1],c[2],c[3]))
#     else:
#         a.execute('insert into biao10 values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# a.execute('select * from biao10;')
# o=a.fetchall()
# print(o)





# a.execute('use text;')
# a.execute('select * from yy11;')
# b=a.fetchall()
# print(b)
# a.execute('desc yy11;')
# d=a.fetchall()
# with open('n.txt','w+',encoding='utf-8') as f:
#     f.write("{},{},{}".format(d[0][0],d[1][0],d[2][0])+'\n')
#     for i in b:
#         f.write("{},{},{}".format(i[0],i[1],i[2])+'\n')





# import xlwt
# with open('n.txt','r+',encoding='utf-8') as f:
#     a=f.readlines()
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet1')
# for j,i in enumerate(a):
#     i=i.replace('\n','')
#     # print(i)
#     i=i.split(' ')
#     # print(i)
#     for m in i:
#         m=m.split(',')
#         print(m)
#         sheet.write(j,0,m[0])
#         sheet.write(j, 1, m[1])
#         sheet.write(j, 2, m[2])
# f.save('a.xls')





# import os
# import xlrd
# f=xlrd.open_workbook('text.xls')
# sheet=f.sheet_by_name('python1')
# hang=sheet.nrows
# with open('a.txt','w+',encoding='utf-8') as f:
#     for i in range(hang):
#         a = sheet.row_values(i)
#         for j in a:
#             if '\n' in j:
#                 f.write(j)
#             else:
#                 f.write(j+'{}'.format(" "))
# b=ord('A')  ASCII 对应的值
# print(b)





















