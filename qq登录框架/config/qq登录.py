#！/usr/bin/env python
# -*- encoding:utf-8 -*-
from selenium import webdriver
from time import sleep
#！/usr/bin/env python
# -*- encoding:utf-8 -*-
from selenium import webdriver
from time import sleep
from qq登录框架.data.wendang import duqu
class denglu():
    def ql(self,a,b):
        dr=webdriver.Chrome()
        dr.get('http://qzone.qq.com')
        sleep(2)
        dr.switch_to_frame('login_frame')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        dr.find_element_by_xpath('//*[@id="u"]').send_keys('{}'.format(a))
        sleep(2)
        dr.find_element_by_xpath('//*[@id="p"]').send_keys('{}'.format(b))
        sleep(2)
        dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)
        return  dr