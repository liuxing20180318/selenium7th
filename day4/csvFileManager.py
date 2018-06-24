#一、要想读取CSV文件，首先要导入csv代码库
#发现csv不用下载，是Python内置的代码库
#如果要读取Excel需要下载相应的代码库：xlrd
#字母下载：1.通过命令下载：在dos窗口中输入pip install -U xlrd
#pip是Python语言最常用的项目管理工具，和Java中的maven类似
#2.点击file--点击settings--project下面的interpreter--点击+号
#搜索需要的代码库，并可直接安装

#二、指定要读取文件的路径
import csv

path = 'C:/Users/51Testing/PycharmProjects/selenium7th/data/test_data.csv'
#因为字符串中包含反斜线\t等
#1.每个反斜线前面加一个反斜线
#2.把每个反斜线都改成正斜线/
#print(path)
#三、打开路径所对应的文件
file = open(path,'r')
#四、读取文件的内容，通过什么读取
data_table = csv.reader(file)

#五、打印data_table中的每一行数据，怎么办？循环for--each语句
for item in data_table:
    print(item)
#很多的测试用例可能都需要从Excel中读取数据，所以我们应该对这些代码做一个封装，建一个文件叫csvFileManager2，把以上代码封装到一个方法中，并且
