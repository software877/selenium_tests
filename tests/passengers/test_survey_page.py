from page_objects.main_page.main_page import MainPage
from page_objects.main_page.survey_page import SurveyPage

class TestSurveyPage:

    def test_make_survey(self, browser):
        main_page = MainPage(browser=browser)
        survey_page = SurveyPage(browser=browser)
        main_page.open_url()
        main_page.click_passengers_item()
        survey_page.click_survey_button()
