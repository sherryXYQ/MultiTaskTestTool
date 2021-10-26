# -*- coding: utf-8 -*-
# @Time:6/24/2021 5:18 PM
# @Author:xiaoyuqing
# @File: Shell.py
'''
封装执行shell通用方法
'''
import subprocess

class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode('utf-8')
        return o