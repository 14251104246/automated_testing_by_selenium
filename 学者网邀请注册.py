#coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver =webdriver.Chrome()

driver .set_window_size(1080,800)

driver.implicitly_wait(20)

driver.get('http://www.scholat.com/login.html')

#username
time.sleep(1)
#driver.find_element_by_id("login_user").click()
driver.find_element_by_id("j_username").send_keys("523786283@qq.com")
driver.find_element_by_id("j_password_ext").send_keys("**********")
driver.find_element_by_id("login").click()

time.sleep(1)

driver.find_element_by_css_selector(u"#t7 > p").click()
driver.find_element_by_link_text(u"邀请注册").click()
#ChineseName
driver.find_element_by_id("ChineseName").send_keys(u"董浩业")
driver.find_element_by_id("workUnit").send_keys(u"广东财经大学")
driver.find_element_by_id("workEmail").send_keys(u"donghy@mail.sysu.edu.cn")

#driver.find_element_by_link_text(u"邀请好友注册").click()
