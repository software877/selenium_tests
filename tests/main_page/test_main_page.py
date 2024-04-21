from page_objects.main_page.main_page import MainPage


class TestMainPage:
    def test_find_random_word(self, browser):
        main_page = MainPage(browser=browser)
        main_page.open_url()
        main_page.enter_searched_word()
        main_page.click_search_icon()
        assert browser.current_url == f"{browser.url}/search/?q=Test"

