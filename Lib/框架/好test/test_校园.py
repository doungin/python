#!/usr/bin/env  python
#-*- coding:utf-8 -*-
import unittest
from 框架.config.学校_接口 import 学校快查
from  框架.data.duqu_数据 import tes_数据
class xuexiao1(unittest.TestCase):  #学校1继承这个unittest。TestCase
    def test_1(self):#以test开头的测试用例  必须以test开头
        b=学校快查(tes_数据()[0][0])
        # print(tes_数据()[0][0])
        self.assertEqual(b['code'],int(tes_数据()[0][1]))
    def test_2(self):
        b=学校快查(tes_数据()[1][0])
        self.assertEqual(b['code'],int(tes_数据()[1][1]))


aaa = xuexiao1()
aaa.test_1()