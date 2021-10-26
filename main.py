# -*- coding: utf-8 -*-
# @Time:6/25/2021 5:07 PM
# @Author:xiaoyuqing
# @File: run.py

import sys

import pytest

from Common import Log, Shell
from Conf import Config

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件， path=%s' % conf.conf_path )

    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    #--clean-alluredir参数用于执行测试用例前清空xml文件夹，避免生成的测试报告中有历史执行记录
    args = ['-s','-q', '-v', '-n','auto','TestCase', '--alluredir', xml_report_path, '--clean-alluredir']
    pytest.main(args)

    cmd ='allure generate --clean %s -o %s' % (xml_report_path, html_report_path)
    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行测试用例失败，请检查环境配置')
        raise

