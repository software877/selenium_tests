from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_ICON = (By.XPATH, "//button[@type='submit']")
    PASSENGERS_ITEM = (By.XPATH, "//a[@href='/passenger/']")

    def __init__(self, browser):
        super().__init__(browser)

    def enter_searched_word(self, value="Test"):
        with allure.step(f"Ввожу слово {value} в строку поиска"):
            self.is_element_located(self.SEARCH_FIELD).send_keys(value)

    def click_search_icon(self):
        with allure.step(f"Нажимаю значок поиска"):
            self.is_element_located(self.SEARCH_ICON).click()

    def click_passengers_item(self):
        with allure.step(f"Нажимаю меню 'Пассажир'"):
            self.is_element_located(self.PASSENGERS_ITEM).click()



