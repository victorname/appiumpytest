from appium import webdriver
"""
def	init_driver():
    # 服务端启动参数
    desired_caps = {}
    # 手机系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    # 设备号
    desired_caps['deviceName'] = '127.0.0.1:62001'
    # 包名
    desired_caps['appPackage'] = 'com.easyshop.esapp'
    # 启动名
    desired_caps['appActivity'] = '.mvp.ui.activity.LoginIndexActivity t4'

    desired_caps['noReset'] = True
    # 允许输入中文
    # desired_caps['unicodeKeyboard']=True
    # desired_caps['resetKeyboard']=True
    # 手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver
"""

def	init_driver():
    # 服务端启动参数
    desired_caps = {}
    # 手机系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0'
    # 设备号
    desired_caps['deviceName'] = 'LE67A06270119183'
    # 包名
    desired_caps['appPackage'] = 'com.miui.calculator'
    # 启动名
    desired_caps['appActivity'] = '.cal.NormalCalculatorActivity t41'

    desired_caps['noReset'] = True
    # 允许输入中文
    # desired_caps['unicodeKeyboard']=True
    # desired_caps['resetKeyboard']=True
    # 手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver
