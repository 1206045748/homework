from selenium import webdriver
import unittest, time
from HTMLTestRunner import HTMLTestRunner

class TestCase(unittest.TestCase):
    """primepath测试"""

    def setUp(self):
        print("test start")

    def test_equal(self):
       
        file1=[]
        file2=[]
        with open('../answer/answer0.txt', 'r') as df:
            for  de in df:
                file1.append(de)
        with open('../hshanswer/answer0.txt', 'r') as df2:
            for  de2 in df2:
                file2.append(de2)
        flag=0
        for i in range(len(file1)):
            if(file1[i]!=file2[i]):
                print("第"+str(i)+"条路径不匹配："+file1[i]+"vs"+file2[i])
                flag=1
        if(flag==0):
            print("比较成功！")
        #equal = IsHashEqual(f1, f2)
        #equal=False
        self.assertEqual(flag, 0)
    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    
    testunit = unittest.TestSuite()
    testunit.addTest(TestCase("test_equal"))

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    # filename = './report/result.html'
    filename = 'result.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,                  # 指定测试报告文件
                        title='高鑫测试报告',        # 定义测试报告标题 
                        description='用例执行状况：')    # 定义测试报告副标题
    runner.run(testunit)    # 运行测试用例
    fp.close()  # 关闭报告文件