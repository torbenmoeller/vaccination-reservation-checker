from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from BasePage import BasePage
from Reservation import Reservation

text_non_available = "Bitte versuchen Sie es erneut zu einem späteren Zeitpunkt"


class NurembergPage(BasePage):

    def __init__(self, url):
        super().__init__(url)
        self.appointment_reason = None

    def check_availability(self):
        appointment_reason_elem = WebDriverWait(self.driver, 10).until(
            element_to_be_clickable((By.ID, "booking_motive")))
        self.appointment_reason = Select(appointment_reason_elem)
        astra_available = self.check_availability_for_option("Erstimpfung Covid-19 (AstraZeneca)")
        jannsen_available = self.check_availability_for_option("Einzelimpfung Covid-19 (Janssen)")
        if astra_available and jannsen_available:
            return Reservation.not_available
        else:
            return Reservation.available

    def check_availability_for_option(self, option):
        self.appointment_reason.select_by_visible_text(option)
        if text_non_available in self.driver.page_source:
            print(option, "not available")
            return True
        else:
            print(option, "available")
            return False
