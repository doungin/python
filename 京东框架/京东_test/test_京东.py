
#！/usr/bin/env python
# -*- encoding:utf-8 -*-
from 京东框架.config.jingdong import *
import unittest
class 京东测试(unittest.TestCase):
    def test_1(self):
        dr=登录().ql()
        WD=dr.find_element_by_xpath('//*[@id="result"]/div/div/div[1]/div[1]/h3').is_displayed()
        self.assertEqual(WD,True)
        dr.quit()
    def test_2(self):
        dr=登录().ql()
        dr.find_element_by_xpath('//*[@id="settleup-2014"]/div[1]').click()
        sleep(2)
        wd=dr.window_handles
        sleep(2)
        dr.switch_to_window(wd[-1])
        sleep(2)
        wd1=dr.find_element_by_xpath('//*[@id="product_5089235"]/div[1]/div[2]/div/div[2]/div[1]/a').is_displayed()
        self.assertEqual(wd1,True)
        dr.quit()


