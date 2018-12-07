#!/usr/bin/env  python
#-*- coding:utf-8 -*-
import unittest
from 购物车框架.config.test_地址 import 默认地址快查
from  购物车框架.data.读取数据 import tes_数据
class dizhi1(unittest.TestCase):  #学校1继承这个unittest。TestCase
    def test_1(self):#以test开头的测试用例  必须以test开头
        b=默认地址快查(int(tes_数据()[0][0]))
        print(b)
        self.assertEqual(b['code'],str(int(tes_数据()[0][1])))
    def test_2(self):
        for i in range(1,len(tes_数据())+1):
            b=默认地址快查(int(tes_数据()[{}][0].format(i)))
            self.assertEqual(b['code'],str(int(tes_数据()[{}][1]).format(i)))
aaa = dizhi1()
aaa.test_1()

