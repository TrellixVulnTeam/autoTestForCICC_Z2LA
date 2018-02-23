from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class report(Page):
    '''
    中金研究研报
    '''

    #研报列表
    report_list_loc = (By.LINK_TEXT, '研报')
    def report_list(self):
        self.find_element(*self.report_list_loc).click()

    #研报详情
    report_detail_loc = (By.CSS_SELECTOR, 'span.over-ell > a')
    def report_detail(self):
        return self.find_elements(*self.report_detail_loc)

    #头像进入分析师详情
    analyst_head_loc = (By.CSS_SELECTOR, '#container > div:nth-child(1) > div.report-list.my-star > div:nth-child(1) > div.rgt > div > a')
    def analyst_head_click(self):
        self.find_element(*self.analyst_head_loc).click()


    #展开分析师简介小浮框
    def analyst_float_box(self):
        move_to_element = self.find_element(*self.analyst_head_loc)
        ActionChains(self.driver).move_to_element(move_to_element).perform()

    #浮框中分析师头像进入分析师详情
    analyst_small_head_loc = (By.CSS_SELECTOR, '#container > div:nth-child(1) > div.report-list.my-star > div:nth-child(1) > div.rgt > div > div > div.doc-info-top.clearfix > a')
    def analyst_small_head_click(self):
        self.analyst_float_box()
        self.find_element(*self.analyst_small_head_loc).click()

    #浮框中分析师名称进入分析师详情
    analyst_name_loc = (By.CSS_SELECTOR, '#container > div:nth-child(1) > div.report-list.my-star > div:nth-child(1) > div.rgt > div > div > div.doc-info-top.clearfix > div > h4 > a')
    def analyst_name_click(self):
        self.analyst_float_box()
        self.find_element(*self.analyst_name_loc).click()

    #浮框中点击关注
    analyst_focus_loc = (By.CSS_SELECTOR, '#container > div:nth-child(1) > div.report-list.my-star > div:nth-child(1) > div.rgt > div > div > div.doc-info-top.clearfix > div > span')
    def analyst_focus_click(self):
        self.analyst_float_box()
        focus_on = self.find_element(*self.analyst_focus_loc).text
        if focus_on == '+关注':
            self.analyst_float_box()
            self.find_element(*self.analyst_focus_loc).click()
            self.analyst_float_box()
            assert('已关注' == str(self.find_element(*self.analyst_focus_loc).text))
            self.analyst_float_box()
            self.find_element(*self.analyst_focus_loc).click()
            self.analyst_float_box()
            assert ('+关注' == str(self.find_element(*self.analyst_focus_loc).text))
        elif focus_on == '已关注':
            self.analyst_float_box()
            self.find_element(*self.analyst_focus_loc).click()
            self.analyst_float_box()
            assert ('+关注' == str(self.find_element(*self.analyst_focus_loc).text))
            self.analyst_float_box()
            self.find_element(*self.analyst_focus_loc).click()
            self.analyst_float_box()
            assert ('已关注' == str(self.find_element(*self.analyst_focus_loc).text))
        else:
            print(focus_on)

    #点击收藏研报
    report_collect_loc = (By.CSS_SELECTOR, '#container > div:nth-child(1) > div.report-list.my-star > div:nth-child(1) > div.rgt > span > i')
    report_collection_loc = (By.CSS_SELECTOR, '#container > div:nth-child(1) > div.report-list.my-star > div:nth-child(1) > div.rgt > span > p')
    def report_collect_click(self):
        report_collection = self.find_element(*self.report_collection_loc).text
        if report_collection == '收藏':
            self.find_element(*self.report_collect_loc).click()
            sleep(1)
            assert ('已收藏' == str(self.find_element(*self.report_collection_loc).text))
            self.find_element(*self.report_collect_loc).click()
            sleep(1)
            assert ('收藏' == str(self.find_element(*self.report_collection_loc).text))
        elif report_collection == '已收藏':
            self.find_element(*self.report_collect_loc).click()
            sleep(1)
            assert ('收藏' == str(self.find_element(*self.report_collection_loc).text))
            self.find_element(*self.report_collect_loc).click()
            sleep(1)
            assert ('已收藏' == str(self.find_element(*self.report_collection_loc).text))
        else:
            print(report_collection)

    #验证页面进入成功
    def page_title(self):
        return self.driver.title