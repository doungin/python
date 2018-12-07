import unittest
from 购物车框架.data.读取数据 import tes_数据
from 购物车框架.report.报告 import zhixing
with open('run.txt','r',encoding='utf-8') as f:
    f.readlines()
    a=f.readlines()
    # print(a)
if __name__=='__main__':
    if 'all' in a:
        b=['test*']
        zhixing(b)
    else:
        zhixing(a)




