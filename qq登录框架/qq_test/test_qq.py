#！/usr/bin/env python
# -*- encoding:utf-8 -*-
from qq登录框架.config.qq登录 import *
import unittest
from qq登录框架.data.wendang import *
from selenium.webdriver.common.action_chains import ActionChains
class qq测试(unittest.TestCase):
    def test_1(self):
        aa = duqu()
        bb = aa.shuju()
        dd=denglu()
        for i,j in enumerate(bb):
            if i==0:
                dr=dd.ql(bb[0][0],bb[0][1])
                sleep(2)
                dd=dr.current_url
                self.assertNotEqual('https://qzone.qq.com/',dd)
                dr.quit()

    def test_2(self):
        aa = duqu()
        bb = aa.shuju()
        dd = denglu()
        for i, j in enumerate(bb):
            if i == 1:
                dr = dd.ql(bb[1][0], bb[1][1])
                sleep(2)
                wd = dr.find_element_by_xpath('/html/body/div[1]/div[11]/div[2]/iframe')
                sleep(2)
                dr.switch_to_frame(wd)
                sleep(2)
                start=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
                sleep(2)
                try:
                    for i in range(175,190,4):
                        ActionChains(dr).drag_and_drop_by_offset(start,i,0).perform()       #自动移动按钮
                        sleep(2)
                except:
                    pass
                dd = dr.current_url
                self.assertEqual('https://qzone.qq.com/', dd)
                dr.quit()



