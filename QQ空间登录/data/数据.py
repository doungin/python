from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import selenium.webdriver.support.ui as ui
def denglu():
    dr = webdriver.Chrome()
    dr.get('https://qzone.qq.com/')
    sleep(1)
    dr.switch_to.frame('login_frame')
    sleep(1)
    dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
    sleep(1)
    dr.find_element_by_xpath('//*[@id="u"]').send_keys('1365173230')
    sleep(1)
    dr.find_element_by_xpath('//*[@id="p"]').send_keys('971101doungin')
    dr.find_element_by_xpath('//*[@id="login_button"]').click()
    sleep(1)
    wait = ui.WebDriverWait(dr, 10)
    un=wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe').is_displayed())
    sleep(1)
    wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
    dr.switch_to_frame(wd1)
    sleep(1)
    start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
    sleep(1)
    ActionChains(dr).drag_and_drop_by_offset(start,180,0).perform()
    sleep(3)
denglu()