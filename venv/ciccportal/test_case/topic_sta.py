import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
sys.path.append("./login_sta")
from models import myunit, function
from page_obj.topicPage import topic
from page_obj.loginPage import login

class topicTest(myunit.MyTest):
    '''中金研报专题列表测试'''

    def user_login_verify(self, username = "", password = ""):
        login(self.driver).user_login(username, password)

    def topic_list_enter(self):
        self.user_login_verify(username='operation@cicc.com', password='111111')
        po = topic(self.driver)
        po.topic_list()

    def test_topic_detail(self):
        '''进入专题详情页面'''
        self.topic_list_enter()
        po = topic(self.driver)
        po.topic_detail_title()
        self.assertEqual('专题详情', po.page_title())
        function.insert_img(self.driver, "topic_detail_from_title.png" )
        self.driver.back()
        po.topic_detail_picture()
        self.assertEqual('专题详情', po.page_title())
        function.insert_img(self.driver, "topic_detail_from_picture.png")

if __name__ == '__main__':
    unittest.main()
