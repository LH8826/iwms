import re
import os
import sys
sys.path.append(r"D:\hdiwms-git\App_TestScript\demo_YSApp")
import API_add_order
import common.mail as mail
import time
from time import sleep
import unittest
import HTMLTestRunner
from common.rizhi import *

logger = getlog()
def creat_suite():
    suite = unittest.TestSuite()
    # suite.addTest(login.LoginTestCase('login'))
    suite.addTest(API_add_order.ShouHuoTestCase('getorders'))
    return suite

if __name__ == '__main__':
    suite = creat_suite()
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    fp = open('D://HDiWMS//report_of_day//YSApp//' +'YSApp'+ file_prefix + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"web新增订单-APP收货",verbosity=2,
                                           description=u"web添加2条订单明细，提取单号，APP根据单号收货")
    # runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    fp.close()
    print(u'生成测试报告')
    try:
        mail.MailUtils.send_test_report()
        sleep(5)
    except:
        print("邮件发送失败")
        logger.error("邮件发送失败")
    finally:
        sleep(3)
        c = os.popen('adb devices')
        d = c.read()
        sleep(5)
        print(type(d), d)
        d1 = re.findall(r"127(.+)\tdevice", d)
        print(type(d1), d1)
        if d1:
            d2 = '127' + d1[0]
            s = os.popen('adb disconnect %s' % d2).read()
            logger.info(s)

        # 根据端口号查询appium 的进程id，再根据id关闭appium服务
        process = os.popen("netstat -aon |findstr 4723")
        p = process.read()
        pid = p.replace('  ', '').split(" ")[2]
        print(u"获得appium 进程id:%s" % pid)
        process.close()
        m = os.popen("taskkill -f -pid %s" % pid)
        print(m.read())
        m.close()

    # 关闭cmd窗口
    # k = os.popen('taskkill /f /im cmd.exe /t')
    # k.close()
    # print(u'关闭cmd窗口')

