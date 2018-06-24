#第一个单元测试框架的示例
#1.要想用unittest框架，首先要导包

import unittest

#2.创建一个类，用来编写自动化测试用例，这个类需要继承unittest框架中的TestCase类
#我们继承了TestCase这个类，就说明我们这个类是一个测试用例类
#Python中类名最好和文件名不一样，文件名首字母小写，类名首字母大写
#（）表示继承，继承是指子类完全继承父类的所有方法和属性，并有自己扩展内容
class FirstUnitTest(unittest.TestCase):
    #   3.重写父类的setup和teardown方法
    def setUp(self):
#setup()是在测试用例方法执行之前要做的操作
#类似手工测试中的预置条件
        print(1)
    def tearDown(self):
#tearDown()是在测试用例方法执行之后要做的操作
#比如可能需要还原测试场景，清除脏数据
        print(2)
    def test_login(self):
        #框架规定测试用例方法必须用test开头
        #只有以test开头的方法才会被当做测试用例，直接执行
#这个方法用来编写测试步骤
        print(3)
    def switch_window(self):
        print(4)
    def test_zhuce(self):#在Python中类里面的每个方法都有一个默认参数，叫self
        #self类似于Java中this关键字，代表类本身
        #根据光标所在位置，决定执行什么测试用例
        #光标在哪个方法中，那么就会只运行哪个测试用例
        self.switch_window()
    #也可以选择重写setupclass和tesrdownclass方法
    @classmethod  #在Python中叫装饰器，在Java中叫注解
    def setUpClass(cls):
        print(5)
    @classmethod
    def tearDownClass(cls):
        print(6)
#classmethod只在类中所有方法前或者方法后执行一次

#if __name__ == '_main_':这是一个固定写法
#在程序运行时，通过这句话，可以自动判断当前文件是不是程序入口
#如果当前文件是程序的入口，那么就会执行if子句中的内容
#一个类中，所有测试用例方法的执行顺序，是根据方法名的字母顺序决定的
if __name__ == '_main_':
    unittest.main()