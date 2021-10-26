# -*- coding: utf-8 -*-
# @Time:6/23/2021 6:12 PM
# @Author:xiaoyuqing
# @File: Assert.py
'''
封装Assert方法
'''

from Common import Log, Constants
import json
import re

class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    def assert_code(self, code, expected_code):
        '''
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        '''
        try:
            assert code == expected_code
            return True
        except:
            self.log.error('status code error, expected code is %s, status code is %s' % (expected_code, code))
            Constants.RESULT_LIST.append('fail')
            raise

    def assert_body(self, body, body_msg, expected_msg):
        '''
        验证response body中任意属性的值等于预期值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        '''
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return  True
        except:
            self.log.error('Response body msg != expected msg, expected msg is %s, body msg is %s' % (expected_msg, msg))
            Constants.RESULT_LIST.append('fail')
            raise

    def assert_body_text(self, body, attr1, attr2, expected_msg):
        '''
        验证response body中任意2级属性值的中文字符是否等于预期字符串中文字符
        :param body:
        :param attr1:
        :param attr2:
        :param expected_msg:
        :return:
        '''
        try:
            msg =body[attr1][attr2]
            msg_txt = ''.join(re.findall(r'[\u4e00-\u9fa5]', msg))
            expected_msg_txt = ''.join(re.findall(r'[\u4e00-\u9fa5]', expected_msg))
            assert msg_txt == expected_msg_txt
            return  True
        except:
            self.log.error('response body text != expected msg text, expected msg text is %s,body text is %s'%(expected_msg_txt, msg_txt))
            Constants.RESULT_LIST.append('fail')
            raise

    def assert_in_text(self, body, expected_msg):
        '''
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        '''
        try:
            text = json.dumps(body, ensure_ascii=False)
            assert expected_msg in text
            return  True
        except:
            self.log.error('response body does not contain expected msg, expected msg is %s' % expected_msg)
            Constants.RESULT_LIST.append('fail')
            raise

    def assert_not_in_text(self, body, unexpected_msg):
        '''
        验证response body中是否不包含预期字符串
        :param body:
        :param unexpected_msg:
        :return:
        '''
        try:
            text = json.dumps(body, ensure_ascii=False)
            assert unexpected_msg in text
            return  True
        except:
            self.log.error('response body contain unexpected msg, unexpected msg is %s' % unexpected_msg)
            Constants.RESULT_LIST.append('fail')
            raise

    def assert_text(self, body, expected_msg):
        '''
        验证response body中任意属性字段值是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        '''
        try:
            assert body ==expected_msg
            return True
        except:
            self.log.error('response body != expected msg, expected msg is %s, body is %s' % (expected_msg, body))
            Constants.RESULT_LIST.append('fail')
            raise

    def assert_time(self, time, expected_time):
        '''
        验证response body响应时间小于预期最大响应时间，单位，毫秒
        :param time:
        :param expected_time:
        :return:
        '''
        try:
            assert time < expected_time
            return True
        except:
            self.log.error('response time > expected time, expected time is %s, time is %s' % (expected_time, time))
            Constants.RESULT_LIST.append('fail')
            raise

