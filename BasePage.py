import abc

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage(object):
    def __init__(self, url):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.url = url

    def setup(self):
        self.driver.get(self.url)

    def teardown(self):
        self.driver.close()

    @abc.abstractmethod
    def check_availability(self):
        return
