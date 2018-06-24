import unittest

import time

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("wjz")
        driver.find_element_by_id("password").send_keys("123456")
        old_title = driver.title
        driver.find_element_by_class_name("login_btn fl").click()
        time.sleep(5)
        new_title = driver.title
        print(driver.title)

        self.assertEqual(old_title,new_title)




if __name__ == '__main__':
    unittest.main()