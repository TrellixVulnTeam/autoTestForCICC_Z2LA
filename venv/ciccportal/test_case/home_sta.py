import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
sys.path.append("./login_sta")
from models import myunit, function
from page_obj.homePage import home
from page_obj.loginPage import login


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

    def test_history_recommended(self):
        '''进入每日推荐页面'''
        self.user_login_verify(username='manager@cicc.com', password='111111')
        po = home(self.driver)
        po.history_recommended()
        self.assertIn('历史推荐', po.page_title())
        function.insert_img(self.driver, "history_recommended.png")

    def test_morning_focus(self):
        '''进入晨会焦点页面'''
        self.user_login_verify(username='manager@cicc.com', password='111111')
        po = home(self.driver)
        po.morning_focus()
        self.assertIn('晨会焦点', po.page_title())
        function.insert_img(self.driver, "morning_focus.png")

    def test_exclusive_recommended(self):
        '''进入专属推荐页面'''
        self.user_login_verify(username='manager@cicc.com', password='111111')
        po = home(self.driver)
        po.exclusive_recommended()
        self.assertIn('研报详情', po.page_title())
        function.insert_img(self.driver, "exclusive_recommended.png")

    def test_popular_profession(self):
        '''进入热门行业页面'''
        self.user_login_verify(username='manager@cicc.com', password='111111')
        po = home(self.driver)
        po.popular_profession()
        self.assertIn('研报详情', po.page_title())
        function.insert_img(self.driver, "popular_profession.png")

    def test_hot_company(self):
        '''进入热门公司页面'''
        self.user_login_verify(username='manager@cicc.com', password='111111')
        po = home(self.driver)
        po.hot_company()
        self.assertIn('研报详情', po.page_title())
        function.insert_img(self.driver, "hot_company.png")

if __name__ == '__main__':
    unittest.main()


