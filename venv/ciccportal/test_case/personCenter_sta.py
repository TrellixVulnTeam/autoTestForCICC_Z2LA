import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
sys.path.append("./login_sta")
from models import myunit, function
from page_obj.personCenterPage import personCenter
from page_obj.loginPage import login

class personCenterTest(myunit.MyTest):

    def user_login_verify(self, username = "", password = ""):
        login(self.driver).user_login(username, password)

    def person_center_enter(self):
        self.user_login_verify(username='operation@cicc.com', password='111111')
        po = personCenter(self.driver)
        po.my_report()

    def test_account_information(self):
        only_tag = '账户信息'
        self.person_center_enter()
        po = personCenter(self.driver)
        po.person_center(only_tag)
        self.assertEqual(only_tag, po.page_title())
        function.insert_img(self.driver, "account_information_from_my_report.png")

    def test_my_report(self):
        self.person_center_enter()
        po = personCenter(self.driver)
        self.assertEqual('我的研报', po.page_title())
        function.insert_img(self.driver, "my_report.png")

    def test_browsing_history(self):
        only_tag = '浏览记录'
        self.person_center_enter()
        po = personCenter(self.driver)
        po.person_center(only_tag)
        self.assertEqual(only_tag, po.page_title())
        function.insert_img(self.driver, "browsing_history_from_my_report.png")

    def test_my_collection(self):
        only_tag = '我的收藏'
        self.person_center_enter()
        po = personCenter(self.driver)
        po.person_center(only_tag)
        self.assertEqual(only_tag, po.page_title())
        function.insert_img(self.driver, "my_collection_from_my_report.png")

if __name__ == '__main__':
    unittest.main()
