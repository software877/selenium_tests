from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RoutesPage(BasePage):
    ROUTES = (By.XPATH, "//*[@id='navbarSupportedContent']/ul/li[3]/a")


