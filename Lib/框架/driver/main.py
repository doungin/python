#!/usr/bin/env python
#-*- coding:utf-8 -*-
# import unittest
# from 框架.好test.test_学校 import xuexiao1
# import time
# import os
# from 框架.report import HTMLTestRunnertest
# # class Test_run():
# #     def run_多个(self):
# #         suit=unittest.TestSuite()
# #         discover=unittest.defaultTestLoader.discover(r'..\好test',pattern='test*.py')
# #         suit.addTest(discover)
# #         now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
# #         f=open('asd.html','wb')
# #         runner=HTMLTestRunnertest.HTMLTestRunner(tester='奥特曼',description='测试结果如下：',title='好分数测试报告',stream=f)
# #         runner.run(suit)
# #         f.close()
# import requests
# # import unittest
# # from 框架.config.学校_接口 import 学校_查询
# # from 框架.data.读取数据的 import duqu
# # from 框架.ttest111.测试1学校 import 学校1
# import HTMLTestRunnertest
# # import time
#
#
#
#
# class Test_run():
# #生成测试报告     生成一个测试套件
#     def run_多个(self):
#         suit=unittest.TestSuite()
#         # 测试类=[]
#         # with open('run.txt','r')as f:
#         #     aaa=f.read()
#         #     aaa=aaa.split('\n')
#         #     for i in aaa:
#         #         f=open(r'..\ttest111\{}.py'.format(i),'r',encoding='utf-8')
#
#
#         suit.addTest(unittest.makeSuite())
#         now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
#         f=open('abc.html','wb')
#
#         runner=HTMLTestRunnertest.HTMLTestRunner(tester='奥特曼',
#                                                  description='测试结果如下',
#                                                  title='好分数测试报告',
#                                                  stream=f,
#                                                  )
#         runner.run(suit)
#         f.close()
#     def run_all(self):#跑所有
#
#         suit = unittest.TestSuite()
#         disvover=unittest.defaultTestLoader.discover(r'..\test',pattern='test*.py')
#         suit.addTest(disvover)#往测试套件中添加测试用例
#         now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
#         f = open('abc.html', 'wb')
#
#         runner = HTMLTestRunnertest.HTMLTestRunner(tester='奥特曼',
#                                                    description='测试结果如下',
#                                                    title='好分数测试报告',
#                                                    stream=f,
#                                                    )
#         runner.run(suit)
#         f.close()
# import re
# if __name__=='__main__':
#     # run=Test_run()
#     # run.run_all()
#     with open('run.txt','r') as f:
#         aaa=f.read()
#         aaa=aaa.split('\n')
#         for i in aaa:
#             f=open(r'..\好test\{}.py)'.format(i),'r',encoding='utf-8')
#             a=f.read()
#             b=re.compile(r'class(.*?):',re.S)
#             c=b.findall(a)
#             for j in c:
#                 jjj=j.split('(')
#                 print(jjj[0])
#                 o=globals()["{}".format(jjj[0])]
#                 print(o)
import unittest
from 框架.data.duqu_数据 import tes_数据
from 框架.report.报告 import zhixing
with open('run.txt','r') as f:
    a=f.readlines()
    # print(a)
if __name__=='__main__':
    if 'all' in a:
        b=['test*']
        zhixing(b)
    else:
        zhixing(a)
