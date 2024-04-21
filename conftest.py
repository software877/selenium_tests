import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://etk31.ru")


@pytest.fixture(scope="class")
def browser(request):
    url = request.config.getoption("--url")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def close_driver():
        driver.close()

    request.addfinalizer(close_driver)

    driver.url = url

    return driver
