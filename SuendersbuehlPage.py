from selenium.webdriver.support.wait import WebDriverWait

from BasePage import BasePage
from Reservation import Reservation


class SuendersbuehlPage(BasePage):
    def __init__(self, url):
        super().__init__(url)
        self.text_non_available = "Zur Zeit keine Buchung verfügbar"

    def check_availability(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_class_name("booking-message"))
        if self.text_non_available in self.driver.page_source:
            return Reservation.not_available
        else:
            return Reservation.available
