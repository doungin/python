#！/usr/bin/env python
# -*- encoding:utf-8 -*-
from selenium import webdriver
from time import sleep
class 登录():
    def ql(self):
        dr=webdriver.Firefox()
        dr.get('https://www.jd.com')
        sleep(2)
        dr.find_element_by_xpath('//*[@id="J_cate"]/ul/li[2]/a[1]').click()
        sleep(2)
        wd=dr.window_handles
        sleep(2)
        dr.switch_to_window(wd[-1])
        sleep(2)
        dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div[1]/li[1]/span').click()
        sleep(2)
        dr.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div[2]/ul[1]/li[1]/a[2]').click()
        sleep(2)
        wd1=dr.window_handles
        sleep(2)
        dr.switch_to_window(wd1[-1])
        sleep(2)
        dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
        sleep(2)
        wd2=dr.window_handles
        sleep(2)
        dr.switch_to_window(wd2[-1])
        sleep(2)
        return dr
