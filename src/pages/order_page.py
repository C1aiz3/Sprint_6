import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage
from src.locators.main_page_locators import MainPageLocators as MPL


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_the_field(self, locator, data):
        with allure.step(f'Fill the field'):
            field = self.find_element(locator)
            field.send_keys(data)

    def accept_cookies(self):
        with allure.step(f'Accept cookie on main page'):
            try:
                self.find_element(MPL.cookie_button).click()
            except:
                pass

    def escape_imitation(self):
        with allure.step(f'ESC button imitation'):
            try:
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            except:
                pass

    def current_page_url(self):
        with allure.step(f'Get current page url'):
            return self.driver.current_url

