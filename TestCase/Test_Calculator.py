from Basic.Driver import init_driver
import time
import allure
import pytest
import os

"""
allure定制化报告：
@allure.feature ：标注主要功能模块
@allure.story ： 标注Features功能模块下的分支功能
@allure.step ：标注测试用例的重要步骤
allure.attach ： 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
@allure.feature('登录功能')
@allure.story('登录成功')
@allure.title('用例的标题')#用例的标题
@allure.severity('blocker')标注测试用例的重要级别
1）blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
2）critical级别：临界缺陷（功能点缺失）
3）normal级别：正常    默认为这个级别
4）minor级别：次要缺陷（界面错误与UI需求不符）
5）trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
@allure.issue('https://www.baidu.com/')#这里传的是一个连接，记录的是你的问题
@allure.testcase('https://www.baidu.com/')#这里传的是一个连接，记录的是你的用例
description：描述用例信息
"""


@allure.feature("进行计算器的加、减、乘、除操作")
class Test_Calculator(object):
    """
    def test_start_up(self):
        self.driver = init_driver()
        time.sleep(5)
        print("启动页面后等待10秒")
        allure.attach("启动页面后等待10秒")
        """

    @allure.title("加法运算")
    @allure.story("test_a")
    def test_a(self):
        """
        用例描述额内容
        allure.MASTER_HELPER.description("11111111111111")   # 如果没有description，那么就取3引号文档注释
        :return:
        """
        self.driver = init_driver()
        time.sleep(5)
        self.driver.find_element_by_id('com.miui.calculator:id/btn_c_1').click()
        allure.step("点击清除按钮")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_7').click()
        allure.step("点击按钮7")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_plus').click()
        allure.step("点击+号")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_8').click()
        allure.step("点击按钮8")
        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="等于"]').click()
        allure.step("点击等于号")
        time.sleep(5)
        allure.step("执行完用例等待5秒")

    @allure.title("减法运算")
    @allure.story("test_b")
    # 用例等级程度
    @allure.severity("minor")
    def test_b(self):
        self.driver = init_driver()
        self.driver.find_element_by_id('com.miui.calculator:id/btn_c_1').click()
        print("点击清除按钮")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_9').click()
        print("点击按钮9")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_minus').click()
        print("点击-号")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_5').click()
        print("点击按钮5")
        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="等于"]').click()
        print("点击等于号")
        time.sleep(5)

    @allure.title("乘法运算")
    @allure.story("test_c")
    def test_c(self):
        self.driver = init_driver()
        self.driver.find_element_by_id('com.miui.calculator:id/btn_c_1').click()
        self.driver.find_element_by_id('com.miui.calculator:id/btn_9').click()
        print("点击按钮9")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_mul').click()
        print("点击X号")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_8').click()
        print("点击按钮8")
        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="等于"]').click()
        print("点击等于号")
        time.sleep(5)

    @allure.title("除法运算")
    @allure.story("test_d")
    def test_d(self):
        self.driver = init_driver()
        self.driver.find_element_by_id('com.miui.calculator:id/btn_c_1').click()
        print("点击清除按钮")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_8').click()
        print("点击按钮8")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_div').click()
        print("点击//号")
        self.driver.find_element_by_id('com.miui.calculator:id/btn_4').click()
        print("点击按钮4")
        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="等于"]').click()
        print("点击等于号")
        time.sleep(10)
        print("等待10秒")
        # self.driver.quit()


if __name__ == '__main__':
    # pytest.main()
    # 以alluredir运行生成报告，并保存在result文件中
    # (-s:允许终端在测试运行时输出某些结果，例如你想输入print的内容，可以加上-s),--alluredir: 生成allure指定语法,
    # ./report":生成报告的路径
    # --clean - alluredir：因为这个插件库allure-pytest生成的报告文件，你第二次运行时候不会清理掉里面的东西，所以你需要删除这个report文件夹，然后运行重新新建reoprt文件夹
    pytest.main(["-s", "--alluredir", "./report/result"])
    # 将报告转换成html格式文件的命令
    allure_cmd = "allure generate ./report/result -o ./report/html --clean"
    p = os.popen(allure_cmd, mode="r")  # 运行命令
    print(p.read())  # 打印查看结果

"""
直接在case文件里运行示例：
if __name__ == '__main__':
    pytest.main([ __file__, '-s','-q','--alluredir', 'allure-report'])

json转换成HTML格式
allure generate ison/ -o html
if __name__ == '__main__':
     pytest.main(["-s","-v","--html=Outputs/reports/pytest.html",
                 "--alluredir=Outputs/allure"])   # allure文件生成的目录


pytest <测试目录> --alluredir <测试结果存放目录>
pytest tests --alluredir report/allure_raw

allure generate <allure测试结果目录> -o <存放报告的目录> --clean
allure测试结果目录，是上面运行 pytest 命令后存放结果的地方，我们这里的目录是 report 下的 allure_raw 文件夹；
存放报告的目录，是最终生成的测试报告存放的目录，我打算把生成出的报告放在 report 下的 allure_report文件夹中；
--clean参数用来清空已有的报告，避免覆盖时出错。
allure generate report/allure_raw -o report/allure_report --clean

"""