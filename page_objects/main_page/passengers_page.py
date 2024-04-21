from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class PassengersPage(BasePage):
    FEEDBACK_BUTTON = (By.XPATH, "/html/body/div[3]/main/div/div/div/div[1]/div/menu/li[6]")
    USER_NAME = (By.ID, "form_callback_FIELD_TITLE")
    EMAIL = (By.ID, "form_callback_FIELD_EMAIL")
    MESSAGE = (By.ID, "form_callback_FIELD_MESSAGE")

    def __init__(self, browser):
        super().__init__(browser=browser)

    def click_feedback_button(self):
        with allure.step(f"Нажимаю на кнопку 'Обратная связь'"):
            self.is_element_located(self.FEEDBACK_BUTTON).click()

    def enter_name(self, name="Test"):
        with allure.step(f"Ввожу имя пользователя"):
            self.is_element_located(self.USER_NAME).send_keys(name)

    def enter_email(self, email="test@test.com"):
        with allure.step(f"Ввожу email"):
            self.is_element_located(self.EMAIL).send_keys(email)

    def enter_message(self, message="Это тестовое сообщение"):
        with allure.step(f"Ввожу сообщение"):
            self.is_element_located(self.MESSAGE).send_keys(message)
