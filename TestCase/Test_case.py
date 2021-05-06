"""""
from Basic.driver import init_driver
import time
import allure
import pytest
@allure.epic("先进行登录，在进行其他操作")
@allure.feature("登录模块")
@allure.suite("测试套件")

class Test_Base(object):
    @allure.story("测试用例一")
    def test_a(self):
        self.driver = init_driver()
        time.sleep(10)
        print("启动页面后等待10秒")
        # self.driver.find_element_by_id('com.easyshop.esapp:id/tv_right').click()
        # print("点击'同意'按钮")
        # time.sleep(2)
        self.driver.find_element_by_id('com.easyshop.esapp:id/tv_login_code').click()
        print("点击'手机号登录按钮'")
        time.sleep(2)
        self.driver.find_element_by_id('com.easyshop.esapp:id/cet_phone').send_keys(18600562492)
        print("输入手机号")
        self.driver.find_element_by_id('com.easyshop.esapp:id/cet_code').send_keys(998877)
        print("输入验证码")
        self.driver.find_element_by_id('com.easyshop.esapp:id/tv_login').click()
        print("点击'下一步'")
        time.sleep(20)

        self.driver.quit()
"""""
