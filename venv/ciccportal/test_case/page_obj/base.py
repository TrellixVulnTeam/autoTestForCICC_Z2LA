class Page(object):
    '''
    页面基础类，用于所有页面的继承
    '''
    cicc_portal_url = 'http://49.4.15.177/cicc-portal/'

    def __init__(self, selenium_driver, base_url = cicc_portal_url, parent = None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self,url):
        self.url = self.base_url + url
        self.driver.get(self.url)
        assert self.on_page(), 'Did not land on %s' % self.url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    
    def open(self):
        self._open(self.url)
        
    def on_page(self):
        return self.driver.current_url == self.url
    
    def script(self,src):
        return self.driver.execute_script(src)