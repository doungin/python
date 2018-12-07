#/usr/bin/env python
#-*- conding：'utf-8'
#接口测试：发送请求   验证响应是否符合需求的过程
#postman     jmeter
#requests 发送http请求   assert 断言处理
import requests
import time
import unittest  #是python自带的单元测试框架
import xlrd
#1  unittest TestCase   用例的管理：主要是管理用例的
#2  unittest TestSuite  测试套件：多个测试用例集合在一起
#3  unittest Tsetloader  测试载入：将测试用例加载到测试套件中
#4  unittest TestRunner  执行测试用例
#    封装了检验返回的结果
import HTMLTestRunne
import HTMLTestRunnertest
# class xuexiao():
def tes_数据():
    shuju=[]
    f=xlrd.open_workbook('123.xls')
    sheet=f.sheet_by_name('Sheet1')
    num=sheet.nrows
    for i in range(1,num):
        aaa=sheet.row_values(i)
        shuju.append(aaa)
    return shuju
def aaa(a):
    url='http://testsupport-be.haofenshu.com/v1/schools/infos'
    querystring={'filterInput':'{}'.format(a)}
    head={
            'cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
    re=requests.get(url=url,headers=head,params=querystring)
    html=re.json()
        #print(html)

        #自带的断言
    # assert html['code']==0   #判断预期的结果是否与断言的结果一致
    return  html
b=aaa('北京')
print(b)


class xuexiao1(unittest.TestCase):  #学校1继承这个unittest。TestCase
    #     print(111)

    # def tearDown(self):  #清理环境：每次用例执行之后去执行
    #     print(666)
    def test_1(self):   #以test开头的测试用例  必须以test开头
        c=tes_数据()
        b=aaa(c[0][0])
        self.assertEqual(b['code'],int(c[0][1]))
        # self.assertEqual(b['data'][0]['schoolName'],'北京七中')
    def test_2(self):
        c=tes_数据()
        b=aaa(c[1][0])
        self.assertEqual(b['code'],int(c[1][1]))
if __name__=='__main__':       #生出测试报告，创建一个测试套件
    suit=unittest.TestSuite()


    # suit.addTest(xuexiao1('test_1'))
    # suit.addTest(xuexiao1('test_2'))            #添加测试用例，将测试用例添加到测试套件中
    suit.addTest(unittest.makeSuite(xuexiao1))   #将整个类里面的测试用例添加到测试套件中   只要是函数开头是test，无论函数是否是用例，都添加到套件中去
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime((time.time())))
    with open('ab.html','wb') as f:
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='奥特曼',description='测试结果如下：',title='好分数测试报告',stream=f)
        runner.run(suit)










