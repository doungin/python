import os
# for i in range(1,11):
#     os.mkdir(r'C:\Users\doungin\Desktop\新建文件夹{}'.format(i))
#     for j in range(1,11):
#         with open(r'C:\Users\doungin\Desktop\新建文件夹{}\{}.txt'.format(i,j),'w',encoding='utf-8') as f:
#             for c in range(9):
#                 f.write('123\n')
#         os.remove(r'C:\Users\doungin\Desktop\新建文件夹{}\{}.txt'.format(i,j))
#     os.rmdir(r'C:\Users\doungin\Desktop\新建文件夹{}'.format(i))
# for i in range(1,11):
#     os.mkdir(r'C:\Users\doungin\Desktop\新建文件夹{}'.format(i))
#     for j in range(1,11):
#         with open(r'C:\Users\doungin\Desktop\新建文件夹{}\{}.txt'.format(i,j),'w+',encoding='utf-8') as f:
#             for c in range(9):
#                 f.write('123\n')
#         os.remove(r'C:\Users\doungin\Desktop\新建文件夹{}\{}.txt'.format(i,j))
#     os.rmdir(r'C:\Users\doungin\Desktop\新建文件夹{}'.format(i))
# for i in range(1,11):
#     os.mkdir(r'C:\Users\doungin\Desktop\新建文件夹{}'.format(i))
#     for j in range(1,11):
#         with open(r'C:\Users\doungin\Desktop\新建文件夹{}\{}.txt'.format(i,j),'w',encoding='utf-8') as f:
#             for m in range(10):
#                 f.write("123\n")

# import requests
# url=''
# head=
# response=requests.get(url=url,headers=head)
# html=response.content.decode('utf-8')
# return html
# patt=re.compile()
# items=patt.findall()


import xlrd
import pymysql
import os
import xlwt
abc=pymysql.connect(host='192.168.0.123',port=3306,user='root',password='123456',charset='utf8')
a=abc.cursor()
with open('a.txt','r',encoding='utf-8') as f :
    b=f.readlines()
a.execute('use text;')
for i in b:
    j=i.replace('\n','')
    c=j.split(',')
    if c[0]=='姓名':
        a.execute('create table lyw8({} char(30),{} char(30),{} char(30));'.format(c[0],c[1],c[2]))
        break
    else:
        a.execute('insert into lyw8 values("{},{},{}");'.format(c[0],c[1],c[2]))































