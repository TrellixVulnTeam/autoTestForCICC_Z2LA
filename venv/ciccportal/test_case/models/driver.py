from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
    # driver = webdriver.Chrome()
    # lists = {
    #     'http://127.0.0.1:5555/wd/hub': 'firefox',
    #     'http://127.0.0.1:5556/wd/hub': 'internet explorer'
    # }
    # for host,browser in lists.items():
    #     driver = Remote(command_executor=host,
    #                     desired_capabilities={'browserName': browser}
    #                     )
    host = '127.0.0.1:4444'
    dc = {'browserName': 'firefox'}
    driver = Remote(command_executor = 'http://' + host + '/wd/hub',
                    desired_capabilities = dc)
    return driver

if __name__ == '__main__':
    lists = {
        'http://127.0.0.1:5555/wd/hub': 'firefox',
        'http://127.0.0.1:5556/wd/hub': 'internet explorer'
    }
    dr = browser()
    dr.get("http://49.4.15.177/cicc-portal")
    dr.quit()