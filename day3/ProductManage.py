#1.登录海盗商城后台
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
#2.选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
#3.点击添加商品链接
driver.find_element_by_link_text("添加商品").click()
#4.输入商品名称
driver.switch_to.frame('mainFrame')
driver.find_element_by_name("name").send_keys("手机")
#5.选择商品分类

#6.在下拉框中选择商品品牌
#7.点击提交按钮
#根据以上7部编写代码，找出第一个不能实现的地方