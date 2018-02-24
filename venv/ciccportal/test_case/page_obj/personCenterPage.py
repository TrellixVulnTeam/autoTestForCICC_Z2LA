from selenium.webdriver.common.by import By
from .base import Page

class personCenter(Page):
    '''
    中金研究个人中心
    '''

    # 我的研报
    def my_report(self):
        self.person_center('我的研报')

    #进入个人中心各子页面
    def person_center(self, linkText):
        self.person_center_loc = (By.LINK_TEXT, linkText)
        personCenterElements = self.find_elements(*self.person_center_loc)
        for personCenterElement in personCenterElements:
            if personCenterElement.is_displayed():
                personCenterElement.click()


    # 验证页面进入成功
    def page_title(self):
        return self.driver.title