from datetime import time

from BasePage import BasePage
from NurembergPage import NurembergPage
from Reservation import Reservation
from SuendersbuehlPage import SuendersbuehlPage
from win10toast import ToastNotifier

base_url = "https://www.doctolib.de/medizinisches-versorgungszentrum-mvz/nuernberg/mvz-dr-renard-kollegen"
suendersbuehl_url = base_url + "?pid=practice-159665"
nuremberg_rul = base_url + "?pid=practice-159661"


def process_page(key, base_page: BasePage):
    base_page.setup()
    result = base_page.test_availability()
    base_page.teardown()
    return key, result


def show_toast(key, result):
    if result is Reservation.available:
        toaster = ToastNotifier()
        toaster.show_toast(key, result.value)


if __name__ == "__main__":
    page_dic = {
        "Nuremberg": NurembergPage(nuremberg_rul),
        "Suendersbuehl": SuendersbuehlPage(suendersbuehl_url)
    }
    result_list = [process_page(key, page) for key, page in page_dic.items()]
    [print(key, ':', result.value) for key, result in result_list]
    [show_toast(key, result) for key, result in result_list]
