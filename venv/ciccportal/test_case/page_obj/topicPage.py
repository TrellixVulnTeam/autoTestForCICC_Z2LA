from selenium.webdriver.common.by import By
from .base import Page

class topic(Page):
    '''
    中金研究专题
    '''

    #专题列表
    topic_list_loc = (By.CSS_SELECTOR, 'body > div.c-head > div.clearfix.header-container > div > div > div.head-left.pull-left > div > ul > li:nth-child(3) > a')
    def topic_list(self):
        self.find_element(*self.topic_list_loc).click()

    #专题详情标题进入
    topic_detail_title_loc = (By.CSS_SELECTOR, 'body > div.c-content.sm-content.clearfix > div.container.pl15 > div.box > div:nth-child(1) > div.col-xs-12.sub-info > h4')
    def topic_detail_title(self):
        self.find_element(*self.topic_detail_title_loc).click()

    #专题详情图片进入
    topic_detail_picture_loc = (By.CSS_SELECTOR, 'body > div.c-content.sm-content.clearfix > div.container.pl15 > div.box > div:nth-child(1) > div.sub-img > img')
    def topic_detail_picture(self):
        self.find_element(*self.topic_detail_picture_loc).click()

    # 验证页面进入成功
    def page_title(self):
        return self.driver.title