# import selenium
from selenium import webdriver
from time import sleep
# dr=webdriver.Chrome()                       #打开浏览器
# dr.get('http://www.moore.ren/')
# dr.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_f3c899e9605d4c49bbb2c3768c39cd78')
# dr.maximize_window()                                       #窗口最大化
# dr.minimize_window()                                        #窗口最小化
# print(dr.title)                                        #获取网站的标题,通常用来做断言
# print(dr.current_url)                                   #获取网站的网址，断言用
# dr.set_window_size(400,400)                               #c窗口大小
# dr.set_window_position(500,200)
# sleep(3)
# dr.get('http://www.jd.com')
# sleep(3)
# dr.back()
sleep(1)
#通过 id属性定位  定位到ID=kw  的位置
# dr.find_element_by_id('kw').send_keys('python')
# dr.find_element_by_id('su').click()              #点击按钮
# 通过class属性定位，定位到class=s_ipt的位置
# dr.find_element_by_class_name('no-register').send_keys('asdas')
#通过name属性定位，定位到name=wd的位置
# dr.find_element_by_name('wd').send_keys('sad')
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()            #路径（xml）标记语言     //相对路径    /绝对路径
# dr.find_element_by_name('phone').send_keys('15896788128')                          xml：可扩展标记语言：存储传输数据
# dr.find_element_by_name('password').send_keys('doungin20222')                      html:显示数据
# dr.find_element_by_link_text('注册').click()                                #通过文本点击
# dr.find_element_by_id('search-submit').click()
# dr.find_element_by_partial_link_text('登').click()                         #模糊查询
# dr.find_element_by_tag_name('').click()                                  #通过标签去定位，通常用于多个元素的定位
# dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/dl/dd[6]/a').click()
# dr.find_element_by_css_selector('#user-nomal > div.login-wrap > div.before-login > li.no-login > a').click()


from selenium.webdriver.common.action_chains import ActionChains
# wd=dr.find_elements_by_class_name('cate_menu_item')      #定位一组元素，结果是列表
# 层级定位
# wd=dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')               #层级定位
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()                                                # 循环点击
#     sleep(1)


# wd=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').text
# print(wd)       #获取元素的某个属性的值
# for i in wd:
#     i.


# dr.forward()


# dr.quit()                                #关闭浏览器
# import re                                                        #防火墙自动登录
# dr.get('https://192.168.0.254:8889/')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# f=[]
# for i in range(1,5):
#     a=dr.find_element_by_css_selector('img.nobody:nth-child({})'.format(i)).get_attribute('src')
#     print(a)
#     patt=re.compile(r'/imgs/(.*?).gif')
#     i=patt.findall(a)
#     print(i)
#     f.append(i[0])
#     print(f)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="input1"]').send_keys(f)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# checkinfo > img:nth-child(1)
#



# dr.get('http://www.ctrip.com/?utm_source=baidu&utm_medium=cpc&utm_campaign=baidu81&campaign=CHNbaidu81&adid=index&gclid=&isctrip=T')
# dr.find_element_by_xpath('//*[@id="searchHotelLevelSelect"]').click()
# sleep(1)                                                                   #携程在手的房间号，十个循环
# for i in range(1,11):
#     dr.find_element_by_xpath('//*[@id="J_roomCountList"]/option[{}]'.format(i)).click()
#     sleep(1)


# dr.get('http://www.moore.ren/')
# print(dr.current_window_handle)                                                       #获得浏览器当前的句柄
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# print(dr.window_handles)
# wd=dr.window_handles                                                                      #获取所有句柄
# dr.switch_to_window(wd[1])                                                                      #切换句柄
# print(dr.title)
# dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('1589646542')



# dr.get('https://qzone.qq.com/')
# sleep(1)
# wd=dr.find_element_by_xpath('//*[@id="login_frame"]')
# dr.switch_to_frame(wd)      #切换到内嵌框架里，只能根据ID或者name或者定位到框架的属性来切换
# dr.switch_to_default_content()                                                      #退出到原始页面
# dr.switch_to.parent_frame()                                                          #切换到上一次页面
# dr.find_element_by_xpath('//*[@id="forgetpwd"]').click()




#
# import re
# dr.get('https://192.168.0.254:8889/')
# sleep(1)
#
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# f=[]
# for i in range(1,5):
#     a=dr.find_element_by_css_selector('img.nobody:nth-child({})'.format(i)).get_attribute('src')
#     print(a)
#     patt=re.compile(r'/imgs/(.*?).gif')
#     i=patt.findall(a)
#     print(i)
#     f.append(i[0])
#     print(f)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="input1"]').send_keys(f)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# # checkinfo > img:nth-child(1)
# #弹出框
# wd=dr.switch_to_alert()           #切换到弹出框
# # print(wd.text)
# wd.accept()                         #点击确定
# # wd.dismiss()                                #关闭弹出框
# # wd.send_keys('内容')                      #弹出框内输入内容
# sleep(2)
#
# wd=dr.find_element_by_xpath('//*[@id="Content"]/frame[1]')
# dr.switch_to_frame(wd)
# dr.find_element_by_xpath('//*[@id="04"]').click()
# sleep(2)
#
# dr.find_element_by_xpath('//*[@id="041"]/span').click()
# sleep(2)
# dr.switch_to.parent_frame()
# # dr.find_element_by_xpath('//*[@id="nav_0"]').click()
# wd=dr.find_element_by_xpath('//*[@id="main"]')
# dr.switch_to_frame(wd)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()
# sleep(2)
# dr.switch_to.parent_frame()
# wd=dr.find_element_by_xpath('//*[@id="main"]')
# dr.switch_to_frame(wd)
# dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()
# dr.switch_to_default_content()





# dr.get('http://www.baidu.com')
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('喔图')
# dr.find_element_by_xpath('//*[@id="su"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="1"]/h3/a').click()
# sleep(2)
# wd=dr.window_handles
# dr.switch_to_window(wd[-1])
# dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]/div/ul/li[6]/div/div/div/a[1]').click()
# sleep(1)
# wf=dr.window_handles
# dr.switch_to_window(wf[-1])
# dr.find_element_by_xpath('//*[@id="loginUsername"]').send_keys('1365173230')
# for i in range(1,10):
#     a=dr.find_element_by_xpath('/html/body/ul/li[{}]'.format(i))
#     if '163'in a.text:
#         a.click()



# from time import sleep
# # from selenium.webdriver
# # dr.get('http://www.alltuu.com/')
# # sleep(1)
# # js='var q=document.documentElement.scrollTop=10000'            #控制滚动条的JavaScript代码，10000表示所有网页的高度
# # dr.execute_script(js)
# # wd=dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[4]/div/div[1]')
# # js='arguments[0].scrollIntoView();'                               #控制滚动条到你输入的Xpath的位置
# # dr.execute_script(js,wd)
# # sleep(3)
# dr.get('https://qzone.qq.com/')
# # sleep(1)
# dr.switch_to_frame('login_frame')                                                               #通过框架定位
# # sleep(1)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1365173230')
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('doungin')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# a=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]').click()







from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import selenium.webdriver.support.ui as ui
# dr.get('http://www.moore.ren')
# dr.maximize_window()
# sleep(1)
#
# #强制等待   sleep()
# #智能等待     设置控制器DR等待
# wait = ui.WebDriverWait(dr, 10)
# un=wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="slider_main_block"]/div[2]/a/img').is_displayed())   #是否显示在屏幕上
# #is.enabled()   判断元素是否为灰化状态             #结果：  True  Flase
# print(un)
#
#
#
#
# dr.get_screenshot_as_file(r'‪C:\Users\doungin\Desktop\abc.png')

# dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/a[8]').click()
# dr.get('http://www.moore.ren')
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
# wd=dr.window_handles                                                                      #获取所有句柄
# dr.switch_to_window(wd[-1])
# dr.find_element_by_xpath('//*[@id="newpasswordform"]/div/div[2]/div/input').send_keys('doungin20222')
# dr.find_element_by_xpath('//*[@id="firstpassword"]').send_keys('15896788128')
# dr.find_element_by_xpath('//*[@id="newpasswordform"]/div/div[7]/div/input').send_keys('15896788128')
#

# dr.quit()




