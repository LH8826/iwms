import time
import os
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


class MailUtils():

    @classmethod
    def send_test_report(cls):
        sender = "haidingtest@sina.com"
        receiver = ["yanping@hd123.com", "haidingtest@sina.com"]
        str_add = ','.join(receiver)
        print(str_add)
        auto_code = "467bffc1f4451677"
        subject = "iwms测试报告"

        # 在测试报告存放的目录里，找到最新的测试报告文件
        lists = os.listdir('D://HDiWMS//report_of_day//')  # 列出目录的下所有文件和文件夹保存到lists
        lists.sort(key=lambda fn: os.path.getmtime('D://HDiWMS//report_of_day//' + fn))  # 按时间排序
        file_new = os.path.join('D://HDiWMS//report_of_day//', lists[-1])

        f = open(file_new, "rb")
        mail_body = f.read()
        f.close()

        # 将测试报告以附件发送
        att = MIMEText(mail_body, "base64", 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att_name = 'attachment;'+"filename="+str(lists[-1])
        att['Content-Disposition'] = att_name
        msg = MIMEMultipart('related')
        msgtext = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg.attach(att)
        msg.attach(msgtext)
        msg['From'] = sender
        msg['To'] = str_add
        msg['Subject'] = Header(subject, 'utf-8').encode()

        # 链接邮箱服务器，登录邮箱
        smtp = smtplib.SMTP()
        smtp.connect("smtp.sina.com")
        smtp.login(sender, auto_code)

        # 发送邮件
        try:
            smtp.sendmail(sender, str_add.split(','), msg.as_string())
            print("发送成功")
        except smtplib.SMTPDataError as e:
            print("发送失败")
        finally:
            smtp.quit()


