import HTMLTestRunnertest
import unittest
import time
from 框架.好test.test_学校 import xuexiao1

def zhixing(b):
    #生出测试报告，创建一个测试套件
    suit=unittest.TestSuite()
    for i in b:
        discover = unittest.defaultTestLoader.discover(r'..\好test', pattern='{}.py'.format(i.strip()))
        suit.addTest(discover)
    # suit.addTest(xuexiao1('test_1'))
    # suit.addTest(xuexiao1('test_2'))            #添加测试用例，将测试用例添加到测试套件中
    suit.addTest(unittest.makeSuite(xuexiao1))   #将整个类里面的测试用例添加到测试套件中   只要是函数开头是test，无论函数是否是用例，都添加到套件中去
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime((time.time())))
    with open('ab.html','wb') as f:
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='奥特曼',description='测试结果如下：',title='好分数测试报告',stream=f)
        runner.run(suit)








