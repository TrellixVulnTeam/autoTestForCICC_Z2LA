from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
    '''中金研报登录测试'''

    #测试用户登录
    def user_login_verify(self, username = "", password = ""):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        '''用户名、密码为空登录'''
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.error_hint(), '请输入账号和密码后登录！')
        function.insert_img(self.driver, "user&pawd_empty.png")

    def test_login2(self):
        '''用户名正确，密码为空'''
        self.user_login_verify(username='manager@niub.la')
        po = login(self.driver)
        self.assertEqual(po.error_hint(),'请输入账号和密码后登录！')
        function.insert_img(self.driver, "pawd_empty.png")

    def test_login3(self):
        '''用户名为空，密码正确'''
        self.user_login_verify(password='111111')
        po = login(self.driver)
        self.assertEqual(po.error_hint(),'请输入账号和密码后登录！')
        function.insert_img(self.driver, "user_empty.png")

    def test_login4(self):
        '''用户名密码不匹配'''
        charactor = random.randint(1,100)
        username = "manager" + str(charactor) + "@niub.la"
        self.user_login_verify(username=username, password='111111')
        po = login(self.driver)
        self.assertEqual(po.error_hint(), '密码错误，还剩4次机会！')
        function.insert_img(self.driver, "user_pawd_error.png")

    def test_login5(self):
        '''用户名、密码正确'''
        self.user_login_verify(username='manager@niub.la', password='111111')
        po = login(self.driver)       
        self.assertEqual(po.login_success(), 'manager@niub.la')
        function.insert_img(self.driver, "user_pawd_true.png")



if __name__ == '__main__':
    unittest.main()
