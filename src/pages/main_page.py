import allure

from src.pages.base_page import BasePage
from src.locators.main_page_locators import MainPageLocators as MPL


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies(self):
        with allure.step(f'Accept cookie on main page'):
            try:
                self.find_element(MPL.COOKIE_BUTTON).click()
            except:
                pass


