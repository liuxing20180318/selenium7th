#1.打开主页
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
#2.点击登录按钮
driver.find_element_by_link_text("登录").click()
#3.输入iPhone
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_name("keyword").send_keys("iphone")
#如果我们想在新的标签页上操作页面元素，怎么办
#需要进行窗口切换
#driver.switch_to.window(第二个窗口的名字)
#接下来的问题是如何获取第二个窗口的名字
#selenium提供了所有窗口名字的集合
#handle是句柄的意思，把句柄理解为名字就可以了
#driver.window_handles可以理解为是一个数组，要第二个窗口的名字怎么做
#[1]表示数组的第二个元素,[-1]表示最后一个元素
#在Python中元组和列表可以正着从0开始数，也可以负着从-1开始数，倒数第一个是-1，倒数第二个是-2
#所以第二个窗口的名字就是 driver.window_handles[1]
#窗口切换语句：
#driver.switch_to.window(driver.window_handles[1])