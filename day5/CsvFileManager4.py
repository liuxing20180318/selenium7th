#1.导包

import csv

import os


class csvFileManager4:
    def read(self,filename):
        list = []    #声明一个空列表
        #2.指定csv文件的路径
        path = r"C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv"
#       os.path.dirname(__file__)是一个固定写法，用来获取当前文件的目录结构
        base_parh = os.path.dirname(__file__)
# 用base_parh的好处，不管项目放在任何路径下面，都可以找到该文件的绝对路径
#通过base parh计算出csv文件路径
        print(base_parh)
        path = base_parh.replace('day5','data/' + filename)
        print(path)
#3.打开指定文件
        file = open(path,'r')
#每次打开文件，用完之后要记得关闭该文件，释放系统资源
#上课用的是tyr...finally的方法
#更常用的方法是 with as的语法结构
        with open(path,'r') as file:
            data_table = csv.reader(file)
            #4.循环遍历数据表中的每一行
            for row in data_table:
                print(row)
#5.声明一个二维列表，保存data_table中的所有数据
                list.append(row)
#6.在read方法的末尾，返回这个列表
            return  list
#这个方法写完之后，是不是所有的测试用例，都应该从这个方法读取csv数据
#我们不可能为每个测试用例都单独写这么一个方法
#但是现在这个路径已经写死了，只能读test_data.csv这个文件
#一个csv文件只适合保存一组测试用例数据
#所以不同测试用例，应该对应不同的csv文件
#7.把csv文件名作为参数传进来


if __name__ == '__main__':
    list = csvFileManager4().read('test_data.csv')
    print(list[1][0])


