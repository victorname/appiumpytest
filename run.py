import os
import shutil
import subprocess
import time
import pytest
from Basic import Log

PATH = os.path.split(os.path.realpath(__file__))[0]
print("PATH路径：", PATH)
xml_report_path = PATH + "./report/xml"
print("xml_report_path路径：", PATH)
html_report_path = PATH + "./report/html"
print("html_report_path路径:", PATH)
tm = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
print("tm时间：", tm)


def invoke(md):
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o


if __name__ == '__main__':
    log = Log.MyLog()
    log.info("-----------------------------START: %s----------------------------------" % tm)
    # #递归删除一个目录以及目录内的所有内容
    shutil.rmtree(xml_report_path)
    args = ['-s', '-v', '-q', '--alluredir', xml_report_path]   # //[xml_report_path]根据自己需要定义文件夹，作者定义为：/report/xml
    pytest.main(args)   # args 传一个list对象，list 里面是多个命令行的参数
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    invoke(cmd)
    log.info("-----------------------------END: %s------------------------------------" % tm)

"""
在运行的时候，也可以指定参数运行:
-s： 显示程序中的 print/logging 输出
-v: 丰富信息模式, 输出更详细的用例执行信息
-k： 运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
-q: 简单输出模式, 不输出环境信息
-x: 出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
"""
"""
意思是需要在执行前清空上一次的报告，因此，在run.py里，将生成报告的命令改为如下：每次运行前将上一次的xml和html报告都清空。
# 定义测试集
# --clean-alluredir清空上一次的xml报告
args = ['-s', '-q', 'TestCase/test_Case.py', '--alluredir', xml_report_path, '--clean-alluredir']    
pytest.main(args)    
# --clean清空上一次的html报告
cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)  
shell.invoke(cmd)

"""