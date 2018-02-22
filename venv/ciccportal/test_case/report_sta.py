import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
sys.path.append("./login_sta")
from models import myunit, function
from page_obj.reportPage import report
from page_obj.loginPage import login
from time import sleep

class reportTest(myunit.MyTest):
    '''中金研报研报列表测试'''

    def user_login_verify(self, username = "", password = ""):
        login(self.driver).user_login(username, password)

    def report_list_enter(self):
        self.user_login_verify(username='operation@cicc.com', password='111111')
        po = report(self.driver)
        po.report_list()

    def test_report_detail(self):
        '''进入研报详情页面'''
        self.report_list_enter()
        po = report(self.driver)
        redes = po.report_detail()
        i = 0
        for rede in redes:
            i += 1
            rede.click()
            self.assertIn('研报详情', po.page_title())
            function.insert_img(self.driver, "history_recommended%d.png" % i)
            break
            # self.driver.back()
            # sleep(5)

    def test_analyst_detail(self):
        '''进入分析师简介页面'''
        self.report_list_enter()
        po = report(self.driver)
        po.analyst_head_click()
        self.assertEqual('分析师简介', po.page_title())
        self.driver.back()
        po.analyst_small_head_click()
        self.assertEqual('分析师简介', po.page_title())
        self.driver.back()
        po.analyst_name_click()
        self.assertEqual('分析师简介', po.page_title())

    def test_analyst_focus(self):
        '''小浮框关注分析师'''
        self.report_list_enter()
        po = report(self.driver)
        po.analyst_focus_click()

    def test_report_collect(self):
        '''研报列表收藏研报'''
        self.report_list_enter()
        po = report(self.driver)
        po.report_collect_click()

if __name__ == '__main__':
    unittest.main()
