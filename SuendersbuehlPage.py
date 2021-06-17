from selenium.webdriver.support.wait import WebDriverWait

from BasePage import BasePage
from Reservation import Reservation


class SuendersbuehlPage(BasePage):
    def test_availability(self):
        text_non_available = "Zur Zeit keine Buchung verfügbar"
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element_by_class_name("booking-message"))
        if text_non_available in self.driver.page_source:
            return Reservation.not_available
        else:
            return Reservation.available
