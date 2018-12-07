#!/usr/bin/env python
#-*- coding:utf-8
import unittest
import HTMLTestRunnertest
from qq登录框架.qq_test.test_qq import *
import time
class 报告():
    def bg(self):
        suit = unittest.TestSuite()
        suit.addTest(unittest.makeSuite(qq测试))
        now = time.strftime('%Y %M %d %H-%M-%S', time.localtime(time.time()))
        with open('考试.html', 'wb') as f:
            runner = HTMLTestRunnertest.HTMLTestRunner(tester='刘弋玮',
                                                  description='测试结果如下:',
                                                  title='考试测试报告',
                                                  stream=f)
            runner.run(suit)