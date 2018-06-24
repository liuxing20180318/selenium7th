#1.登录海盗商城
from selenium import webdriver
from day2.loginTest import Login
#实例化对象会占用内存，pycharm会自动帮我们释放内存
driver = webdriver.Chrome()
driver.implicitly_wait(20)

Login().loginWithDefaultUser(driver)

#2.点击账号设置

driver.find_element_by_link_text("账号设置").click()
#3.点击个人资料
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[4]/ul/li[2]/a").click()
#4.修改真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("小明")
#5.修改性别
#driver.find_element_by_css_selector('[value="1"]').click()
driver.find_elements_by_id("xb")[2].click()
#6.修改生日
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1951-06-06")
#7.修改QQ
driver.find_element_by_name("qq").clear()
driver.find_element_by_name("qq").send_keys("1006701")
#8.点击确定，保存成功
#driver.find_element_by_class_name("btn4").click()