# -*- coding: utf-8 -*-
# @Time:6/25/2021 5:03 PM
# @Author:xiaoyuqing
# @File: conftest.py
import allure
import pytest
from Conf.Config import Config
from Common import Constants

@pytest.fixture(scope='session')
def action():
    #定义环境
    title = Constants.API_ENVIRONMENT
    conf = Config()