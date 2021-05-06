# -*- coding: utf-8 -*-
"""
封装执行shell语句方法

"""
import subprocess
class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o


"""
上面不能使用时，试用本方法
def invoke(cmd):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    subp.wait(2) # 等待子进程终止
    if subp.poll() == 0:
        print(subp.communicate()[1])
    else:
        print("失败")
"""