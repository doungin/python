#!/usr/bin/env python
#-*- coding:utf-8
import HTMLTestRunnertest
from 京东框架.京东_test.test_京东 import *
import time
import HTMLTestRunne
class 报告():
    def bg(self):
        suit = unittest.TestSuite()
        suit.addTest(unittest.makeSuite(京东测试))
        now = time.strftime('%Y %M %d %H-%M-%S', time.localtime(time.time()))
        with open('考试.html', 'wb') as f:
            runner = HTMLTestRunnertest.HTMLTestRunner(tester='刘弋玮',
                                                  description='测试结果如下:',
                                                  title='考试测试报告',
                                                  stream=f)
            runner.run(suit)