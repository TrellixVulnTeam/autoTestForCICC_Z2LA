import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
sys.path.append("./login_sta")
from models import myunit, function
from page_obj.activityPage import activity
from page_obj.loginPage import login

class activityTest(myunit.MyTest):
    '''中金研报活动列表测试'''

    def user_login_verify(self, username = "", password = ""):
        login(self.driver).user_login(username, password)

    def activity_list_enter(self):
        self.user_login_verify(username='operation@cicc.com', password='111111')
        po = activity(self.driver)
        po.activity_list()

    def test_activity_detail(self):
        '''进入活动详情页面'''
        self.activity_list_enter()
        po = activity(self.driver)
        po.activity_detail_title()
        self.assertEqual('活动详情', po.page_title())
        function.insert_img(self.driver, "activity_detail_from_title.png" )
        self.driver.back()
        po.activity_detail_picture()
        self.assertEqual('活动详情', po.page_title())
        function.insert_img(self.driver, "activity_detail_from_picture.png")

if __name__ == '__main__':
    unittest.main()
