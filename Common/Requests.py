# -*- coding: utf-8 -*-
# @Time:6/23/2021 4:09 PM
# @Author:xiaoyuqing
# @File: Requests.py

'''
封装request
'''
import os
import random
import requests
import json
#发送文件中的数据需要pip安装requests_toolbelt库
from requests_toolbelt import MultipartEncoder

import Common.Constants


class Request:
    def get_request(self, url, data, header):
        '''
        get请求
        :param url:
        :param data:
        :param header:
        :return:
        '''
        if not url.startswith('http://'):
            url= '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.get(url=url, headers=header)
            else:
                response = requests.get(url=url, params=data, headers=header)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url:', url))
            print(e)
            return()
        except requests.exceptions as e:
            print('%s%s' % ('exception url:', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()
        Common.Constants.STRESS_LIST.append(time_consuming)

        response_dict = dict()
        response_dict['code'] = response.status_code
        try:
            response_dict['body'] = response.json()
        except Exception as e:
            response_dict['body'] = ''
            print(e)
        response_dict['text'] = response.text
        return response_dict


    def post_request(self, url, data, header):
        '''
        post请求
        :param url:
        :param data: 注意判断header为application/json时需将dict类型的data dump成str类型并编码
        :param header:
        :return:
        '''
        if not url.startswith('http://'):
            url= '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header)
            elif header['Content-Type'] == 'application/json;charset=UTF-8':
                response = requests.post(url=url, data=json.dumps(data).encode('utf-8'),headers=header)
            else:
                response = requests.post(url=url, data=data, headers=header)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url', url))
            print(e)
            return ()
        except requests.exceptions as e:
            print('%s%s' % ('exception url:', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()
        Common.Constants.STRESS_LIST.append(time_consuming)

        response_dict = dict()
        response_dict['code'] = response.status_code
        try:
            response_dict['body'] = response.json()
        except Exception as e:
            response_dict['body'] = ''
            print(e)
        response_dict['text'] = response.text
        return response_dict

    def post_request_multipart(self, url, data, header,file_param, file, file_type):
        '''
        上传图片，MP3，文件用的表单：multipart/form-data格式的post请求
        :param url:
        :param data:
        :param header:
        :param file_param:
        :param file:
        :param file_type:
        :return:
        '''
        if not url.startswith('http://'):
            url= '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                data[file_param] = (os.path.basename(file),open(file,'rb'),file_type)
                m = MultipartEncoder(fields=data)
            header['Content-Type'] = m.content_type
            response = requests.post(url=url, params=data, headers=header)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url', url))
            print(e)
            return ()
        except requests.exceptions as e:
            print('%s%s' % ('exception url:', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()
        Common.Constants.STRESS_LIST.append(time_consuming)

        response_dict = dict()
        response_dict['code'] = response.status_code
        try:
            response_dict['body'] = response.json()
        except Exception as e:
            response_dict['body'] = ''
            print(e)
        response_dict['text'] = response.text
        return response_dict

    def put_requests(self,url, data, header):
        '''
        put请求
        :param url:
        :param data:
        :param header:
        :return:
        '''
        if not url.startswith('http://'):
            url= '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.put(url=url, headers=header)
            else:
                response = requests.put(url=url,params=data, headers=header)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url', url))
            print(e)
            return ()
        except requests.exceptions as e:
            print('%s%s' % ('exception url:', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()
        Common.Constants.STRESS_LIST.append(time_consuming)

        response_dict = dict()
        response_dict['code'] = response.status_code
        try:
            response_dict['body'] = response.json()
        except Exception as e:
            response_dict['body'] = ''
            print(e)
        response_dict['text'] = response.text
        return response_dict


