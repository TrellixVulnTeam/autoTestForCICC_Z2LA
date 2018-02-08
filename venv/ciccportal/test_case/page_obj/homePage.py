from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class home(Page):
    '''
    中金研报首页
    '''
    daily_recommendations_loc = (By.CSS_SELECTOR,'html body div.container-fluid div.col-xs-9.w910 div.c-panel-list div.recommended_daily div.c-panel-box div div.panel-info div')
    def daily_recommendations(self):
        self.find_element(*self.daily_recommendations_loc).click()

    #验证页面进入成功
    def page_title(self):
        return self.driver.title