from selenium.webdriver.common.by import By
from .base import Page

class activity(Page):
    '''
    中金研究活动
    '''

    #活动列表
    activity_list_loc = (By.CSS_SELECTOR, 'body > div.c-head > div.clearfix.header-container > div > div > div.head-left.pull-left > div > ul > li:nth-child(4) > a')
    def activity_list(self):
        self.find_element(*self.activity_list_loc).click()

    #活动详情标题进入
    activity_detail_title_loc = (By.CSS_SELECTOR, '#activityList > div:nth-child(1) > div.img-content.my-box-shadow > div.ac-text > div > h4')
    def activity_detail_title(self):
        self.find_element(*self.activity_detail_title_loc).click()

    #活动详情图片进入
    activity_detail_picture_loc = (By.CSS_SELECTOR, '#activityList > div:nth-child(1) > div.img-content.my-box-shadow > div.ac-img.img-left > a')
    def activity_detail_picture(self):
        self.find_element(*self.activity_detail_picture_loc).click()

    # 验证页面进入成功
    def page_title(self):
        return self.driver.title