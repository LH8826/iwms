import os
import sys
sys.path.append(r"D:\hdiwms-git\YeShen_App_TestScript\demo_app")
import re
import unittest
from appium import webdriver as app_webdriver
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.MysqlHelper import MysqlHelper
from common.rizhi import *

logger = getlog()
class ShouHuoTestCase(unittest.TestCase):
    def getorders(self):
        os.startfile(r'D:\Program Files\Nox\bin\Nox.exe')
        sleep(40)
        self.UI_driver = webdriver.Chrome(r'D:\python\chromedriver\chromedriver.exe')
        self.UI_driver.implicitly_wait(10)
        self.UI_driver.set_window_size(1030, 840)
        self.UI_driver.get("http://test.iwms.hd123.cn/")

        # 清理多余窗口，保证 登录页面 为当前唯一窗口
        cur_handle = self.UI_driver.current_window_handle
        handles = self.UI_driver.window_handles
        for handle in handles:
            if handle != cur_handle:
                self.UI_driver.switch_to.window(handle)
                self.UI_driver.close()
        self.UI_driver.switch_to.window(cur_handle)
        sleep(3)

        # 登录网站
        login_user_ele = self.UI_driver.find_element_by_css_selector("#loginAccount")
        login_user_ele.clear()
        login_user_ele.send_keys("13917888888")
        sleep(1)

        login_pwd_ele = self.UI_driver.find_element_by_css_selector('#password')
        login_pwd_ele.clear()
        login_pwd_ele.send_keys("888888")
        sleep(1)

        login_img_ele = self.UI_driver.find_element_by_css_selector("#imageCaptcha")
        login_img_ele.clear()
        login_img_ele.send_keys("88")
        sleep(1)

        self.UI_driver.find_element_by_css_selector("#root > div > div.antd-pro-layouts-user-layout-container > div > div "
                                                 "> div.antd-pro-pages-account-login-login-fill > div.antd-pro-pages-account-login-login-formWrapper > "
                                                 "div.antd-pro-pages-account-login-login-accountLogin > div:nth-child(2) > div > form > button").click()
        sleep(5)

        # 切换组织
        manu_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/section/section/header/div/div/div[2]/span[2]')
        ActionChains(self.UI_driver).move_to_element(manu_ele).perform()
        sleep(3)

        sub_manu_ele = self.UI_driver.find_element_by_xpath('//span[text()="切换组织"]')
        sub_manu_ele.click()
        sleep(3)

        # 切换到弹窗,选配送中心
        win = self.UI_driver.switch_to.window(self.UI_driver.window_handles[-1])
        self.UI_driver.find_element_by_xpath('//span[text()="配送中心: [P001]测试配送中心"]').click()
        sleep(1)

        # <button type="button" class="ant-btn ant-btn-primary" ><span>确 定</span></button>,class name只能写ant-btn-primary!
        self.UI_driver.find_element_by_class_name('ant-btn-primary').click()
        sleep(2)

        manu2_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/section/section/header/div/div/div[1]/div[2]/ul/li[7]/div/span')
        ActionChains(self.UI_driver).move_to_element(manu2_ele).perform()
        sleep(2)

        manu3_ele = self.UI_driver.find_element_by_xpath('//*[@id="/in-overflowed-indicator$Menu"]/li[1]/div[1]/span/span')
        ActionChains(self.UI_driver).move_to_element(manu3_ele).perform()
        sleep(2)

        self.UI_driver.find_element_by_xpath('//*[@id="/in$Menu"]/li[1]/a').click()
        sleep(2)

        # 查询定单
        # qry_bn = self.UI_driver.find_element_by_id('billNumberAndSource')
        # qry_bn.send_keys('Y001190912000001')
        # sleep(2)
        # self.UI_driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/section/section/main/div[1]/div[2]/div/div[1]/div/div/div[2]/div/form/div/div[4]/div/button[1]').click()
        # sleep(2)

        # 点击“新建”按钮
        self.UI_driver.find_element_by_xpath(
            '//*[@id="createButton"]').click()
        sleep(3)

        # 填写供应商信息
        gongying_ele = self.UI_driver.find_element_by_xpath('//*[text()="请输入供应商"]')
        ActionChains(self.UI_driver).click(gongying_ele).send_keys('Y001').send_keys(Keys.ENTER).perform()
        sleep(2)

        # 选择物流方式
        # wuliu_ele = self.UI_driver.find_element_by_css_selector('#logisticMode > div > div > div')
        # wuliu_ele.click()
        # tongpei_ele = self.UI_driver.find_element_by_xpath('//li[text()="统配"]')
        # tongpei_ele.click()
        # sleep(1)

        # 选择仓位
        cangwei_ele = self.UI_driver.find_element_by_xpath('//*[text()="请输入仓位"]')
        cangwei_ele.click()
        sleep(1)
        # ActionChains(self.UI_driver).key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).click().perform()
        xialatiao_lel = self.UI_driver.find_element_by_xpath('//*[text()="[01]正常仓"]')
        xialatiao_lel.click()
        # js = "var action=document.evaluate('//*[@id='9432c10f-6ac3-405e-9f22-58bbdb198356']/ul').scrollTop=10000"
        # self.UI_driver.execute_script(js)
        # self.UI_driver.find_element_by_xpath('//*[@id="wrh"]/div/div/div[2]').click()
        sleep(2)

        # 选择日期
        riqi_ele = self.UI_driver.find_element_by_xpath('//*[@id="expireDate"]/div/input')
        ActionChains(self.UI_driver).click(riqi_ele).send_keys('2020-01-01').send_keys(Keys.ENTER).perform()

        # 新增商品明细
        mingxi_ele = self.UI_driver.find_element_by_xpath('//*[@id="editTable"]/button')
        mingxi_ele.click()
        sleep(1)
        mingxi_ele.click()
        sleep(1)

        # 拖动鼠标到底部
        js = "var action=document.documentElement.scrollTop=10000"
        self.UI_driver.execute_script(js)
        sleep(2)

        # 新增第一个明细
        han_1_shanpin_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="editTable"]/div[3]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[3]/div/div/div/div[1]')
        ActionChains(self.UI_driver).click(han_1_shanpin_ele).send_keys('Y001').perform()
        sleep(3)
        han_1_guige_ele = self.UI_driver.find_element_by_css_selector(
            '#editTable > div.ant-table-wrapper > div > div > div > div > div.ant-table-scroll > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > div > div > div')
        han_1_guige_ele.click()
        sleep(2)
        han_1_guige_dwn_ele = self.UI_driver.find_element_by_xpath('//li[text()="1*1*1/-"]')
        han_1_guige_dwn_ele.click()
        sleep(1)
        han_1_dangjia_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="editTable"]/div[3]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[5]/div/div[2]/input')
        han_1_dangjia_ele.send_keys(Keys.CONTROL, "a")
        han_1_dangjia_ele.send_keys('3')
        han_1_dangjia_ele.send_keys(Keys.ENTER)
        sleep(1)
        han_1_jianshu_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="editTable"]/div[3]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[6]/div/div[1]/div[2]/input')
        han_1_jianshu_ele.send_keys('200')
        sleep(1)

        # 新增第二个明细
        han_2_shanpin_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="editTable"]/div[3]/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[3]/div/div/div/div[1]')
        ActionChains(self.UI_driver).click(han_2_shanpin_ele).send_keys('Y002').perform()
        sleep(3)
        ActionChains(self.UI_driver).send_keys(Keys.ENTER).perform()
        # han_2_shanpin_ele.click()
        sleep(2)
        han_2_guige_ele = self.UI_driver.find_element_by_css_selector(
            '#editTable > div.ant-table-wrapper > div > div > div > div > div.ant-table-scroll > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > div')
        han_2_guige_ele.click()
        sleep(2)
        han_2_guige_dwn_ele = self.UI_driver.find_element_by_xpath('//*[text()="1*2*6/盒"]')
        han_2_guige_dwn_ele.click()
        sleep(1)
        han_2_dangjia_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="editTable"]/div[3]/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[5]/div/div[2]/input')
        han_2_dangjia_ele.send_keys(Keys.CONTROL, "a")
        han_2_dangjia_ele.send_keys('5')
        han_2_dangjia_ele.send_keys(Keys.ENTER)
        sleep(1)
        han_2_jianshu_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="editTable"]/div[3]/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[6]/div/div[1]/div[2]/input')
        han_2_jianshu_ele.send_keys('20')
        sleep(1)

        # 拖动鼠标到最顶部，点击“确认”
        js = "var action=document.documentElement.scrollTop=0"
        self.UI_driver.execute_script(js)
        sleep(2)
        cnf_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/section/section/main/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div/button[2]')
        ActionChains(self.UI_driver).click(cnf_ele).perform()
        sleep(2)

        # #获取新增订单的来源单号
        # lst = []
        # order_num = self.UI_driver.find_elements_by_css_selector('#root > div > div.screen-xl > section > section > main > div:nth-child(1) > div.antd-pro-components-page-header-wrapper-index-content > div > div > div > div > div.antd-pro-pages-component-page-inner-view-page-detail-tab > div > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div > div > div > div.ant-collapse-content.ant-collapse-content-active > div > div')
        # for i in order_num:
        #     inf = i.text
        #     lst.append(inf)
        # bg = lst[0].replace('\n\n',',').replace('\n',',')
        # lst2 = bg.split(',')
        # laiyuan_nm = lst2[1]
        # order_num = self.UI_driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/section/section/main/div[1]/div[2]/div/div/div/div/div[1]/span/span')
        ordernum = self.UI_driver.find_element_by_xpath('//*[@id="titleEllipsis"]').text
        laiyuan_nm = re.findall(r'\w{16}', ordernum)
        logger.info(u"web新增订单号： %s" % laiyuan_nm)
        sleep(4)
        # 点击 审核 按钮
        shenhe_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/section/section/main/div[1]/div[2]/div/div/div/div/div[1]/div[2]/button[5]')
        shenhe_ele.click()
        sleep(1)

        # 切换到弹窗
        win = self.UI_driver.switch_to.window(self.UI_driver.window_handles[-1])
        sleep(1)
        # 确认审核
        # self.UI_driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]')
        self.UI_driver.find_element_by_css_selector(
            'body > div:nth-child(15) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant'
            '-modal-footer > div > button.ant-btn.ant-btn-primary').click()
        sleep(2)

        # 拖动鼠标到最顶部，点击“确认并创建”
        # js="var action=document.documentElement.scrollTop=0"
        # self.UI_driver.execute_script(js)
        # sleep(2)
        # cnf_ele = self.UI_driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/section/section/main/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div/button[3]')
        # ActionChains(self.UI_driver).click(cnf_ele).perform()

        # 新增明细后，到定单查询页面进行定单号查询
        fanghui_btn_ele = self.UI_driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/section/section/main/div[1]/div[2]/div/div/div/div/div[1]/div[2]/button[1]')
        fanghui_btn_ele.click()
        sleep(2)
        qry_bn = self.UI_driver.find_element_by_xpath('//*[@id="billNumberAndSource"]')
        qry_bn.clear()
        sleep(2)
        qry_bn.send_keys(laiyuan_nm)
        sleep(2)
        self.UI_driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/section/section/main/div[1]/div[2]/div/div[1]/div/div/div[2]/div/form/div/div[4]/div/button[1]').click()
        sleep(5)
        self.UI_driver.quit()

    # 以下是app部分
    # class LoginAndroidTestCase(unittest.TestCase):
        # 链接模拟器
        a = os.popen('adb start-server')
        b = a.read()
        print(b)
        a.close()
        sleep(2)
        c = os.popen('adb devices')
        d = c.read()
        sleep(5)
        print(type(d), d)
        d1 = re.findall(r"127(.+)\tdevice", d)
        print(type(d1), d1)
        if d1:
            d2 = '127' + d1[0]
        else:
            logger.error(u"连接夜神模拟器失败")
            d2 = '127.0.0.1:62001'
        c.close()
        e = os.popen('adb connect %s' % d2)
        f = e.read()
        logger.info(f)
        e.close()
        sleep(5)

        ## 启动appium 命令行服务
        ## 一定要加start，否则system命令会阻塞进程，无法执行后续的python语句！！！！！！！
        ## appium desktop命令行版本 1.7.2，nodev12.13 版本，才能匹配成功！！！！！！！！！！
        os.system('start appium -a 127.0.0.1 -p 4723')
        sleep(30)
        logger.info(u'启动appium服务')

        # 配置APP参数
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5'
        desired_caps['deviceName'] = 'test'
        desired_caps['appPackage'] = 'com.hd123.iwms.rf'
        desired_caps['appActivity'] = '.modules.SplashActivity'
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        desired_caps['newCommandTimeOut'] = 6000
        # desired_caps['automationName'] = 'uiautomator2'
        self.driver = app_webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        sleep(2)

        # def tearDown(self):
        #     self.UI_self.driver.close_app()
        #     self.UI_driver.quit()

        # 登录APP
        try:
            self.driver.find_element_by_id('com.hd123.iwms.rf:id/edt_ip').send_keys('app2.iwms.hd123.cn:8081/test')
            sleep(2)
            self.driver.find_element_by_id('com.hd123.iwms.rf:id/btn_ok').click()
            self.driver.find_element_by_id('com.hd123.iwms.rf:id/edt_account').send_keys('13917888888')
            sleep(2)
            self.driver.find_element_by_id('com.hd123.iwms.rf:id/edt_password').send_keys('888888')
            sleep(2)
            self.driver.find_element_by_id('com.hd123.iwms.rf:id/btn_login').click()
            sleep(2)
            logger.info(u"登录APP成功")
        except:
            logger.info(u"登录APP失败")
            self.driver.close_app()
            self.driver.quit()

        # 取消升级
        try:
            self.driver.find_element_by_id('com.hd123.iwms.rf:id/btn_no').click()
            sleep(2)
        except:
            pass

        # 点击 入库
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/navigation_stkin').click()
        sleep(2)

        # 点击 正常收货
        self.driver.find_element_by_android_uiautomator(r'new UiSelector().text("正常收货")').click()
        sleep(2)

        # 输入 第一条订单明细
        # self.driver.find_element_by_id('com.hd123.iwms.rf:id/cb_mix_load').click() #  点击 混载
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/order_bill').send_keys(laiyuan_nm[0])  # 订单
        # self.driver.find_element_by_id('com.hd123.iwms.rf:id/order_bill').send_keys('P001191209000005')
        sleep(2)
        self.driver.keyevent(66)
        sleep(2)
        helper = MysqlHelper('db2.iwms.hd123.cn',3306,'iwms','iwms','iwmsfacility')
        sql = "select barcode from iwmscontainer where state='IDLE' and barcode like 'Y00001%%' order by barcode"
        container_1 = helper.get_one(sql)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/container').send_keys(container_1[0])  # 容器条码
        sleep(2)
        self.driver.keyevent(66)
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/article').send_keys('Y001')  # 商品条码
        sleep(2)
        self.driver.keyevent(66)
        sleep(2)

        # 提取 第一条订单页面数据
        mingxi_dic_1 = {}
        shangpin_1 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_article_name').get_attribute('text')
        mingxi_dic_1['商品'] = shangpin_1

        guige_1 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_qpc_str').get_attribute('text')
        mingxi_dic_1['规格'] = guige_1

        zhuangpan_1 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_pad').get_attribute('text')
        mingxi_dic_1['装盘建议'] = zhuangpan_1

        baozhiqi_1 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_expire').get_attribute('text')
        mingxi_dic_1['保质期'] = baozhiqi_1

        daishouyingshou_1 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_stkin_qty').get_attribute('text')
        mingxi_dic_1['待收应收'] = daishouyingshou_1

        print("商品_1 明细",mingxi_dic_1)

        self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_produce_date').click()  # 生产日期
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/im_decMonth').click()
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/monthDateView').click()
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/entire').send_keys('2')  # 箱/零
        sleep(2)
        self.driver.keyevent(66)
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/scatter').send_keys('3')  # 箱/零
        sleep(2)
        self.driver.keyevent(66)
        sleep(2)

        # 输入 第二条订单明细
        # self.driver.find_element_by_id('com.hd123.iwms.rf:id/cb_mix_load').click()  # 点击 混载
        container_2 = helper.get_one(sql)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/container').send_keys(container_2[0])  # 容器条码
        sleep(2)
        self.driver.keyevent(66)
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/article').send_keys('Y002') #商品条码
        sleep(2)
        self.driver.keyevent(66)
        sleep(2)

        # 提取 第二条订单页面数据
        mingxi_dic_2 = {}
        shangpin_2 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_article_name').get_attribute('text')
        mingxi_dic_2['商品'] = shangpin_2

        guige_2 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_qpc_str').get_attribute('text')
        mingxi_dic_2['规格'] = guige_2

        zhuangpan_2 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_pad').get_attribute('text')
        mingxi_dic_2['装盘建议'] = zhuangpan_2

        baozhiqi_2 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_expire').get_attribute('text')
        mingxi_dic_2['保质期'] = baozhiqi_2

        daishouyingshou_2 = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_stkin_qty').get_attribute('text')
        mingxi_dic_2['待收应收'] = daishouyingshou_2

        print("商品_2 明细",mingxi_dic_2)

        self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_produce_date').click()  # 生产日期
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/im_decMonth').click()
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/monthDateView').click()
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/entire').send_keys('2')  # 箱/零
        sleep(2)
        self.driver.keyevent(66)
        sleep(2)
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/scatter').send_keys('1')  # 箱/零
        sleep(2)
        self.driver.keyevent(66)
        sleep(2)

        # 结束收货
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/btn_4').click()
        sleep(10)

        # 提取 订单未收货信息
        dingdan_weishuohuo = {}
        dingdan = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_order_bill').get_attribute('text')
        dingdan_weishuohuo['订单'] = dingdan
        # print("订单未收货",dingdan)

        weishoujianshu = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_unreceived_qty_str').get_attribute('text')
        dingdan_weishuohuo['未收件数'] = weishoujianshu
        # print("订单未收货",weishoujianshu)

        weishoupingxiangshu = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_unreceived_article').get_attribute('text')
        dingdan_weishuohuo['未收品项数'] = weishoupingxiangshu
        # print("订单未收货",weishoupingxiangshu)

        weishouhuo_shangpin_1 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameL'
                                                             'ayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.Relat'
                                                             'iveLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.R'
                                                             'elativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Li'
                                                             'nearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayou'
                                                             't[1]/android.widget.LinearLayout/android.widget.TextView[1]').get_attribute('text')
        dingdan_weishuohuo['商品_1'] = weishouhuo_shangpin_1
        # print("订单未收货",weishouhuo_shangpin_1)

        weishouhuo_guige_1 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                          'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameL'
                                                          'ayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.Rel'
                                                          'ativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.wid'
                                                          'get.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.'
                                                          'widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widge'
                                                          't.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]').get_attribute('text')
        dingdan_weishuohuo['规格_1'] = weishouhuo_guige_1
        # print("订单未收货",weishouhuo_guige_1)

        daishoujianshu_1 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Fr'
                                                        'ameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.Relativ'
                                                        'eLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearL'
                                                        'ayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.L'
                                                        'inearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Sc'
                                                        'rollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearL'
                                                        'ayout/android.widget.TextView[3]').get_attribute('text')
        dingdan_weishuohuo['待收件数_1'] = daishoujianshu_1
        # print("订单未收货",daishoujianshu_1)

        weishouhuo_shangpin_2 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Fra'
                                                             'meLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.Relat'
                                                             'iveLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Li'
                                                             'nearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.wi'
                                                             'dget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.wi'
                                                             'dget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.wid'
                                                             'get.LinearLayout/android.widget.TextView[1]').get_attribute('text')
        dingdan_weishuohuo['商品_2'] = weishouhuo_shangpin_2
        # print("订单未收货",weishouhuo_shangpin_2)

        weishouhuo_guige_2 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayo'
                                                          'ut/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/and'
                                                          'roid.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.sup'
                                                          'port.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widg'
                                                          'et.LinearLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.Linea'
                                                          'rLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/'
                                                          'android.widget.TextView[2]').get_attribute('text')
        dingdan_weishuohuo['规格_2'] = weishouhuo_guige_2
        # print("订单未收货",weishouhuo_guige_2)

        daishoujianshu_2 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                                        '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/andr'
                                                        'oid.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.sup'
                                                        'port.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widg'
                                                        'et.LinearLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.Linear'
                                                        'Layout/android.widget.LinearLayout[2]/android.widget.LinearLayout/androi'
                                                        'd.widget.TextView[3]').get_attribute('text')
        dingdan_weishuohuo['待收件数'] = daishoujianshu_2
        # print("订单未收货",daishoujianshu_2)
        logger.info("订单未收货信息: %s"%dingdan_weishuohuo)

        # 提取 收货单信息
        shouhuodang_dic = {}
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLa'
                                     'yout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayo'
                                     'ut/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScroll'
                                     'View/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]/android.widget.TextView').click()
        sleep(3)
        shouhuodang = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_receive_num').get_attribute('text')
        shouhuodang_dic['收货单'] = shouhuodang
        # print("收货单",shouhuodang)

        zongjianshu = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_qty_str_count').get_attribute('text')
        shouhuodang_dic['总件数'] = zongjianshu
        # print("总件数",zongjianshu)

        pingxiangshu = self.driver.find_element_by_id('com.hd123.iwms.rf:id/tv_article_count').get_attribute('text')
        shouhuodang_dic['品项数'] = pingxiangshu
        # print("品项数",pingxiangshu)

        shouhuodang_shangping_1 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                                               'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.Re'
                                                               'lativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.L'
                                                               'inearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.wi'
                                                               'dget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widg'
                                                               'et.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.Li'
                                                               'nearLayout/android.widget.TextView[1]').get_attribute('text')
        shouhuodang_dic['商品_1'] = shouhuodang_shangping_1
        # print("收货单 商品_1",shouhuodang_shangping_1)

        shouhuodang_guige_1 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayo'
                                                           'ut/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/and'
                                                           'roid.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.sup'
                                                           'port.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widge'
                                                           't.LinearLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.Linear'
                                                           'Layout/android.widget.LinearLayout[1]/android.widget.LinearLayout'
                                                           '/android.widget.TextView[2]').get_attribute('text')
        shouhuodang_dic['规格_1'] = shouhuodang_guige_1
        # print("收货单 规格_1",shouhuodang_guige_1)

        shouhuodang_jianshu_1 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayou'
                                                              't/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/andr'
                                                              'oid.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.su'
                                                              'pport.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.w'
                                                              'idget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.L'
                                                              'inearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/'
                                                             'android.widget.TextView[3]').get_attribute('text')
        shouhuodang_dic['件数_1'] = shouhuodang_jianshu_1
        # print("收货单 件数_1",shouhuodang_jianshu_1)

        shouhuodang_shangping_2 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Frame'
                                                               'Layout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLa'
                                                               'yout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayou'
                                                               't/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLa'
                                                               'yout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ScrollVie'
                                                               'w/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/'
                                                               'android.widget.TextView[1]').get_attribute('text')
        shouhuodang_dic['商品_2'] = shouhuodang_shangping_2
        # print("收货单 商品_2",shouhuodang_shangping_2)

        shouhuodang_guige_2 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                                                           'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.'
                                                           'widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.suppor'
                                                           't.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widge'
                                                           't.LinearLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.Line'
                                                           'arLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/'
                                                           'android.widget.TextView[2]').get_attribute('text')
        shouhuodang_dic['规格_2'] = shouhuodang_guige_2
        # print("收货单 规格_2",shouhuodang_guige_2)

        shouhuodang_jianshu_2 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayo'
                                                              'ut/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout'
                                                              '/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/a'
                                                              'ndroid.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayou'
                                                              't/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/a'
                                                              'ndroid.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/and'
                                                              'roid.widget.TextView[3]').get_attribute('text')
        shouhuodang_dic['件数_2'] = shouhuodang_jianshu_2
        # print("收货单 件数_2",shouhuodang_jianshu_2)
        logger.info("收货单信息:%s"%shouhuodang_dic)
        sleep(2)

        # 点击 结束
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/btn_1').click()
        sleep(10)

        # 返回首页
        self.driver.find_element_by_id('com.hd123.iwms.rf:id/actionbar_back_text').click()
        sleep(3)

        # 结束APP
        self.driver.close_app()
        self.driver.quit()





