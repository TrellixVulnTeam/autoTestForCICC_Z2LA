from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''

    url = '/'

    #Action
    cp_login_button_loc = (By.CSS_SELECTOR,'.info-all > div:nth-child(1) > span:nth-child(2)')

    def ciccportal_login(self):
        self.find_element(*self.cp_login_button_loc).click()

    login_username_loc = (By.CSS_SELECTOR,'input#email')
    login_password_loc = (By.CSS_SELECTOR,'input#password')
    login_button_loc = (By.CSS_SELECTOR,'span#btnLogin')

    #登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口
    def user_login(self, username, password):
        '''获取的用户名密码登录'''
        self.open()
        self.ciccportal_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    error_hint_loc = (By.CSS_SELECTOR, 'p#emailError')

    #登录错误提示
    def error_hint(self):
        return self.find_element(*self.error_hint_loc).text

    person_center_loc = (By.CSS_SELECTOR, '.info-user > div:nth-child(1)')
    account_information = (By.CSS_SELECTOR, '.info-item > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
    login_account = (By.CSS_SELECTOR, '.common-info > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)')

    #登录成功校验
    def login_success(self):
        move_to_element = self.find_element(*self.person_center_loc)
        ActionChains(self.driver).move_to_element(move_to_element).perform()
        self.find_element(*self.account_information).click()
        return self.find_element(*self.login_account).text




