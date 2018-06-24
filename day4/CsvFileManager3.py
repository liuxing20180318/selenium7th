import csv

class  CsvFileManager3:
    @classmethod
    def read(self):
        path = r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
        file = open(path,'r')
        #通过csv代码库读取打开的csv文件，获取到文件中所有的数据
        data_table = csv.reader(file)
        #for循环  item是每一行， in是在数据集中 data_table表示数据集
        #data_table中有几行数据，我们就会执行几次
        for item in data_table:
            print(item)
        file.close()

#如果想测试一下这个方法：
if __name__ == '__main__':
   #csvr = CsvFileManager2()
    #csvr.read()
    #如果在方法上面加上classmethod，表示这个方法可以直接用类调用
    CsvFileManager3.read()