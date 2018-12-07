from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
dr.get('https://qzone.qq.com/')
sleep(1)
wd=dr.find_element_by_xpath('//*[@id="login_frame"]')
dr.switch_to_frame(wd)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
dr.find_element_by_xpath('//*[@id="u"]').send_keys('1365173230')
dr.find_element_by_xpath('//*[@id="p"]').send_keys('971101doungin')
dr.find_element_by_xpath('//*[@id="login_button"]').click()
