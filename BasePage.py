import abc

from selenium import webdriver


class BasePage(object):
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.url = url

    def setup(self):
        self.driver.get(self.url)

    def teardown(self):
        self.driver.close()

    @abc.abstractmethod
    def test_availability(self):
        return
