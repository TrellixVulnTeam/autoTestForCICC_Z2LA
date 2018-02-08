import unittest, random, sys
from selenium.webdriver.common.by import By
sys.path.append("./models")
sys.path.append("./page_obj")
sys.path.append("./login_sta")
from models import myunit, function
from page_obj.homePage import home
from page_obj.loginPage import login
from page_obj.base import Page

class homeTest(myunit.MyTest):
    '''中金研报首页测试'''

    def user_login_verify(self, username = "", password = ""):
        login(self.driver).user_login(username, password)

    def test_daily_recommendations(self):
        '''进入每日推荐页面'''
        self.user_login_verify(username='manager@cicc.com', password='111111')
        po = home(self.driver)
        po.daily_recommendations()
        self.assertIn('每日推荐', po.page_title())
        function.insert_img(self.driver, "daily_recommendations.png")

if __name__ == '__main__':
    unittest.main()


