# -*- coding: utf-8 -*-
# @Time:6/24/2021 5:38 PM
# @Author:xiaoyuqing
# @File: YmlParser.py
'''
读取yml文件夹下所有数据
'''

import yaml
import os

def parse(filename = None):
    path_yaml = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '\\data\\YamlScripts'
    pages = {}
    for root, dirs, files in os.walk(path_yaml):
        if filename != None:
            watch_file_path = os.path.join(root, filename)
            with open(watch_file_path,'r', encoding='utf-8') as f:
                pages = yaml.load(f)
        else:
            for name in files:
                watch_file_path = os.path.join(root, name)
                with open(watch_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f)
                    pages.update(page)
        return pages

class GetPages:
    @staticmethod
    def get_page_list(filename = None):
        _page_list = {}
        if filename != None:
            pages = parse(filename)
        else:
            pages= parse()
        for page, value in pages.items():
            _page_list[page] = value
        return _page_list

