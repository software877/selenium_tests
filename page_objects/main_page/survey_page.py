from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class SurveyPage(BasePage):
    __SURVEY_BUTTON = (By.XPATH, "/html/body/div[3]/main/div/div/div/div[1]/div/menu/li[8]")

    def __init__(self, browser):
        super().__init__(browser=browser)

    def click_survey_button(self):
        with allure.step(f"Нажимаю на кнопку 'Опрос качества обслуживания'"):
            self.is_element_located(self.__SURVEY_BUTTON).click()

