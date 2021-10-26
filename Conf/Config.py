# -*- coding: utf-8 -*-
# @Time:6/25/2021 4:34 PM
# @Author:xiaoyuqing
# @File: Config.py
from configparser import ConfigParser
from Common import Log
import os

class Config:
    #titles:
    TITLE_TEST = 'dmchat_test'
    TITLE_MAIL = 'mail'

    #values:
    VALUE_TESTER = 'tester'
    VALUE_ENVIRONMENT = 'environment'
    VALUE_HOST = 'host'
    VALUE_API = 'api'
    VALUE_HEADERS = 'headers'

    VALUE_SMTP_SERVER = 'smtpserver'
    VALUE_SENDER = 'sender'
    VALUE_RECEIVER = 'receiver'
    VALUE_USERNAME = 'username'
    VALUE_PASSWORD = 'password'

    path_dir =str(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))

    def __init__(self):
        '''
        初始化
        '''
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir + '\Report\\xml'
        self.html_report_path = Config.path_dir + '\Report\\html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError('请确保配置文件存在！')

        self.config.read(self.conf_path, encoding='utf-8')

        self.tester_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_TESTER)
        self.environment_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_ENVIRONMENT)
        self.host_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_HOST)
        self.api_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_API)
        self.headers_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_HEADERS)

        self.smtpserver = self.get_conf(Config.TITLE_MAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.TITLE_MAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.TITLE_MAIL, Config.VALUE_RECEIVER)
        self.username = self.get_conf(Config.TITLE_MAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_MAIL, Config.VALUE_PASSWORD)

    def get_conf(self, title, value):
        '''
        配置文件读取
        :param title:
        :param value:
        :return:
        '''
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        '''
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        '''
        self.config.set(title, value, text)
        with open(self.conf_path, 'w+') as f:
            return self.config.write(f)

    def add_conf(self, title):
        '''
        配置文件添加
        :param title:
        :return:
        '''
        self.config.add_section(title)
        with open(self.conf_path, 'w+') as f:
            return  self.config.write(f)
