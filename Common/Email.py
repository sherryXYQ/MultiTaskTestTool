# -*- coding: utf-8 -*-
# @Time:6/25/2021 5:18 PM
# @Author:xiaoyuqing
# @File: Email.py

'''
封装发送邮件通用方法
'''
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common import Constants, Log
from Conf.Config import Config

class SendEmail:
    def __init__(self):
        self.config = Config()
        self.log = Log.MyLog()

    def sendEmail(self):
        msg = MIMEMultipart()
        stress_body = Constants.STRESS_LIST
        result_body = Constants.RESULT_LIST
        body = 'Dear all,\n本次接口自动化测试报告如下： \n 接口响应时间结果集： %s\n   接口执行结果集： %s\n' % (stress_body, result_body)
        mail_body = MIMEText(body, _subtype='plain', _charset='utf-8')
        strTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        msg['Subject'] = Header('接口自动化测试报告---' + strTime,'utf-8')
        msg['From'] = self.config.sender
        receiver = self.config.receiver
        if ',' in receiver:
            to = receiver.split(',')
            msg['To'] = ','.join(to)
        else:
            msg['To'] = receiver

        msg.attach(mail_body)
        smtp = smtplib.SMTP()
        try:
            smtp.connect(self.config.smtpserver)
            smtp.login(self.config.username, self.config.password)
            smtp.sendmail(self.config.sender, receiver, msg.as_string())
        except Exception as e:
            self.log.error('邮件发送失败，请检查邮件配置是否正确')
            print(e)
        else:
            self.log.info('邮件发送成功')
        finally:
            smtp.quit()
