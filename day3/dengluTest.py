#selenium执行JavaScript中的两个关键字：return（返回值）和argument（参数）
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://localhost/")
driver.implicitly_wait(20)
#点击登录链接
#用JavaScript的方法找登录链接的代码
#document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
#用selenium的方法找登录链接的代码
#driver.find_element_by_link_text("登录")
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
#登录
driver.find_element_by_id("username").send_keys("wjz")
#driver.find_element_by_id("password").send_keys("123456")
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
#返回商城首页
driver.find_element_by_link_text("进入商城购物").click()
#搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#点击商品（用这种方法，再实现一次不打开新窗口）
#因为img没有target属性，所以我们复制css的时候要找它的父节点a标签
#复制出来的css往往比较长，我们可以适当缩写长度
#我们定位元素的目标节点是最后一个节点，大于号>的前面是父节点，后面是子节点
#
product_link_css ="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div:nth-child(2) > div.shop_01-imgbox > a"
#使用JavaScript删除a标签的target属性
#通过xpath定位元素
iphone = driver.find_element_by_css_selector(product_link_css)
#删除元素的target属性
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
#在商品详情页面点击加入购物车
driver.find_element_by_id("joinCarButton").click()
#点击去购物车结算
driver.find_element_by_css_selector(".shopCar_T_span3").click()
#点击结算按钮
driver.find_element_by_css_selector("body > div.shopCarbox.w1100 > div:nth-child(4) > div:nth-child(3) > a").click()
#点击添加新地址
driver.find_element_by_class_name("add-address").click()
#输入收货人等信息
driver.find_element_by_name("address[address_name]").send_keys("123")
driver.find_element_by_name("address[mobile]").send_keys("15910793331")
dropdown1 = driver.find_element_by_id("add-new-area-select")
#下拉框是一种特殊的网页元素，对下拉框的操作和普通网页元素不太一样
#selenium为这种特殊的元素专门创建了一个类select
select1 = Select(dropdown1)
select1.select_by_value("110000")
time.sleep(2)
select1.select_by_visible_text("辽宁省")
dropdown2 = driver.find_elements_by_class_name("add-new-area-select")[1]
Select(dropdown2).select_by_visible_text("沈阳市")

#dropdown3 = driver.find_elements_by_class_name("add-new-area-select")[2]
#上下两个语句意思一样
dropdown3 = driver.find_elements_by_tag_name("select")[2]
Select(dropdown3).select_by_visible_text("铁西区")
driver.find_element_by_name("address[address]").send_keys("撒大家看见")
driver.find_element_by_name("address[zipcode]").send_keys("100025")
#点击保存收货人信息
#driver.find_element_by_class_name("aui_state_highlight").click()