from datetime import datetime

from win10toast import ToastNotifier

from BasePage import BasePage
from NurembergPage import NurembergPage
from Reservation import Reservation
from SuendersbuehlPage import SuendersbuehlPage

base_url = "https://www.doctolib.de/medizinisches-versorgungszentrum-mvz/nuernberg/mvz-dr-renard-kollegen"
suendersbuehl_url = base_url + "?pid=practice-159665"
nuremberg_rul = base_url + "?pid=practice-159661"


def show_toast(key, result):
    if result is Reservation.available:
        toaster = ToastNotifier()
        toaster.show_toast(key, result.value)


def process_page(key, base_page: BasePage):
    print("Checking", key)
    base_page.setup()
    result = base_page.check_availability()
    base_page.teardown()
    return key, result


def check_for_appointments():
    print("Checking for appointments...", datetime.now())
    page_dic = {
        "Suendersbuehl": SuendersbuehlPage(suendersbuehl_url),
        "Nuremberg": NurembergPage(nuremberg_rul)
    }
    result_list = [process_page(key, page) for key, page in page_dic.items()]
    print("Checking for appointments done")
    [print(key, ':', result.value) for key, result in result_list]
    [show_toast(key, result) for key, result in result_list]


if __name__ == "__main__":
    check_for_appointments()
