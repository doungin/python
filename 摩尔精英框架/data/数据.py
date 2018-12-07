#!/usr/bin/env  python
#-*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
import os
dr=webdriver.Chrome()
sleep(1)
dr.get('http://www.moore.ren')
dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[4]/div/li[1]/a').click()
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# sleep(1)
# wd=dr.window_handles                                                                      #获取所有句柄
# dr.switch_to_window(wd[-1])
# sleep(1)
# dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('15896788128')
# dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('doungin20222')
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
# sleep(1)
# wd=dr.window_handles                                                                      #获取所有句柄
# dr.switch_to_window(wd[-1])
# sleep(1)
# dr.find_element_by_xpath('//*[@id="login-name"]/a').click()
# dr.find_element_by_xpath('//*[@id="top_right"]/li[1]').click()
# sleep(1)
# # wd=dr.window_handles                                                                      #获取所有句柄
# # dr.switch_to_window(wd[-1])
# dr.find_element_by_xpath('//*[@id="newpasswordform"]/div/div[2]/div/input').send_keys('doungin20222')
# dr.find_element_by_xpath('//*[@id="firstpassword"]').send_keys('15896788128')
# dr.find_element_by_xpath('//*[@id="newpasswordform"]/div/div[7]/div/input').send_keys('15896788128')
