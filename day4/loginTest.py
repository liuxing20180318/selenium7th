#用unittest写一个后台登录的测试用例
#1.导包
import unittest

#2.建类，并继承unittest.Testcase
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class LoginTest(unittest.TestCase):
    #3.重写setup和teardown方法
    @classmethod
    def setUpClass(self):
        #做web自动化测试，所有测试用例都要先打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #窗口最大化的代码，要求驱动版本必须和浏览器精准匹配
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        #为了保证可以看清测试结果，可以在teardown方法中加一个30秒的延时等待
        time.sleep(20)
        #每次执行完测试用例，应该把打开的浏览器关闭。释放内存，清楚cookie和缓存，为下次执行测试用例做准备
        #driver是声明在setup方法中的一个局部变量
        #局部变量是不允许被其他方法访问的
        #所以我们应该把setup方法中声明的driver改成一个全局变量
        #因为self表示类本身，所以我们只要在变量前加上self,就表示这个变量是属于类的
        self.driver.quit()

    def test_login(self):  #登录方法
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()
    def test_product_adding(self): #添加商品方法
        driver = self.driver
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        #除了用name属性切换frame，也可通过8种元素定位方法定位元素，然后切换
        iframe = driver.find_element_by_name("mainFrame")
        driver.switch_to.frame(iframe)
        driver.find_element_by_name("name").send_keys("手机")
        driver.find_element_by_css_selector('[id="1"]').click()
        driver.find_element_by_id("2").click()
        driver.find_element_by_id("6").click()
        #driver.find_element_by_id("7").click()
        #双击
        ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
        select = Select(driver.find_element_by_name("brand_id"))
        select.select_by_value("1")
        driver.find_element_by_class_name("button_search").click()





if __name__ == '__main__':
    unittest.main()
