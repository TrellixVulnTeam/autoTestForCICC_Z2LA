from selenium import webdriver
from .driver import browser
import unittest
import os

class MyTest(unittest.TestCase):

    def setUp(self):
        # lists = {
        #     'http://127.0.0.1:4444/wd/hub': 'firefox'
        # }
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()