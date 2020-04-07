import unittest
import sys
sys.path.append(r"D:\hdiwms-git\App_TestScript\demo_app")
import time
import os
import HTMLTestRunner
import mail as mail
import receive_cargo as receive_cargo


def creat_suite():
    suite = unittest.TestSuite()
    suite.addTest(receive_cargo.AddorderTestCase('receive_cargo'))
    return suite


if __name__ == '__main__':
    suite = creat_suite()
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    fp = open('D://HDiWMS//report_of_day//' + 'App'+file_prefix + '.html', "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"web新增订单-API收货", description=u"web端添加2条订单明细，"
                                                                                          u"审核后，提取单号，到查询页面输入单号查询；API端收货")
    # runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    fp.close()
    mail.MailUtils.send_test_report()

