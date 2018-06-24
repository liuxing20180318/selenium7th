import unittest

import time

from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase


class LoginTest2(MyTestCase):
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("wjz")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_class_name("login_btn fl").click()
        time.sleep(5)
        #通过判断导航栏中是否存在用户名，从而判断登录是否成功
        welcomeTxt = driver.find_element(By.PARTIAL_LINK_TEXT,"您好").text
        self.assertEqual(welcomeTxt,"您好 wjz")
        #现在这个测试用例，把元素定位这样的技术问题和手工测试用例的业务逻辑混合在一个文件中，不利于后期维护
