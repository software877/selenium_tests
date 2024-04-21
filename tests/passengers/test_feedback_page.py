from page_objects.main_page.main_page import MainPage
from page_objects.main_page.passengers_page import PassengersPage
import time


class TestFeedbackPage:

    def test_send_feedback(self, browser):
        main_page = MainPage(browser=browser)
        passengers_page = PassengersPage(browser=browser)
        main_page.open_url()
        main_page.click_passengers_item()
        passengers_page.click_feedback_button()
        passengers_page.enter_name()
        passengers_page.enter_email()
        passengers_page.enter_message()
        time.sleep(30)