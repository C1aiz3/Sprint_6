import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import url


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.site = url

    def open_url(self):
        with allure.step('Open page'):
            self.driver.get(self.site)

    def find_element(self, *locator, time = 5):
        with allure.step(f'Find element with {locator}'):
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(*locator))

    def click_element(self, *locator, time=5):
        with allure.step(f'Click element with {locator}'):
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(*locator)).click()

    def url_checker(self, time=5):
        initial_window_handle = self.driver.current_window_handle

        with allure.step(f'Switch to new window, get url and close this window'):
            try:
                WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(2))

                for window_handle in self.driver.window_handles:
                    if window_handle != initial_window_handle:
                        self.driver.switch_to.window(window_handle)
                        break

                new_url = self.driver.current_url
                self.driver.close()
                return new_url

            finally:
                self.driver.switch_to.window(initial_window_handle)
                pass



