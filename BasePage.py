import abc

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class BasePage(object):
    def __init__(self, url):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.url = url

    def setup(self):
        self.driver.get(self.url)

    def teardown(self):
        self.driver.close()

    @abc.abstractmethod
    def test_availability(self):
        return
