from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open_url(self):
        self.browser.get(self.browser.url)

    def is_element_located(self, locator):
        return WebDriverWait(self.browser, 10).until(
            ec.presence_of_element_located(locator))

