from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class home(Page):
    '''
    中金研报首页
    '''
    #每日推荐
    daily_recommendations_loc = (By.CSS_SELECTOR, 'body > div.container-fluid > div.col-xs-9.w910 > div.c-panel-list > div > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > h4 > a')
    def daily_recommendations(self):
        self.find_element(*self.daily_recommendations_loc).click()

    #历史推荐
    history_recommended_loc = (By.CSS_SELECTOR, 'body > div.container-fluid > div.col-xs-9.w910 > div.c-panel-title > div > a')
    def history_recommended(self):
        self.find_element(*self.history_recommended_loc).click()

    #晨会焦点
    morning_focus_loc = (By.CSS_SELECTOR, '#latestDocument')
    def morning_focus(self):
        self.find_element(*self.morning_focus_loc).click()

    #专属推荐
    exclusive_recommended_loc = (By.CSS_SELECTOR, 'body > div.container-fluid > div.pull-right.w270 > div.c-recommend > div.list-shadow > div:nth-child(1) > a > p')
    def exclusive_recommended(self):
        self.find_element(*self.exclusive_recommended_loc).click()

    #热门行业
    popular_profession_loc = (By.CSS_SELECTOR, '#hy-jr > div:nth-child(1) > a > p')
    def popular_profession(self):
        self.find_element(*self.popular_profession_loc).click()

    #热门公司
    hot_company_loc = (By.CSS_SELECTOR, '#gs-jr > div:nth-child(1) > a > p')
    def hot_company(self):
        self.find_element(*self.hot_company_loc).click()

    #验证页面进入成功
    def page_title(self):
        return self.driver.title