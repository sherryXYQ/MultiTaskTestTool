# -*- coding: utf-8 -*-
# @Time:6/23/2021 6:13 PM
# @Author:xiaoyuqing
# @File: Log.py
'''
封装Log方法
'''
import logging
import os
import time

LEVELS={
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

#initialize logging class
logger = logging.getLogger()
level = 'default'


def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass
def set_handler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.handler)

def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)
    logger.removeHandler(MyLog.handler)

class MyLog:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path+'/Log/log.log'
    error_file = path + '/Log/error.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(error_file)
    date ='%Y-%m-%d %H-%M-%S'

    handler = logging.FileHandler(log_file,encoding='utf-8')
    err_handler = logging.FileHandler(error_file,encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    handler.setFormatter(formatter)
    err_handler.setFormatter(formatter)

    @staticmethod
    def debug(log_msg):
        set_handler('debug')
        logger.debug(log_msg)
        remove_handler('debug')

    @staticmethod
    def info(log_msg):
        set_handler('info')
        logger.info(log_msg)
        remove_handler('info')

    @staticmethod
    def warning(log_msg):
        set_handler('warning')
        logger.warning(log_msg)
        remove_handler('warning')

    @staticmethod
    def error(log_msg):
        set_handler('error')
        logger.error(log_msg)
        remove_handler('error')

    @staticmethod
    def critical(log_msg):
        set_handler('critical')
        logger.critical(log_msg)
        remove_handler('critical')


if __name__ == '__main__':
    MyLog.debug('this is debug msg')
    MyLog.info('this is info msg')
    MyLog.warning('this is warning msg')
    MyLog.error('this is error msg')
    MyLog.critical('this is critical msg')




