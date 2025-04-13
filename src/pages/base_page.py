import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import URL, DZEN


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.site = URL

    def open_url(self, added_data = ''):
        with allure.step('Open page'):
            self.driver.get(f'{self.site}{added_data}')

    def find_element(self, *locator, time = 5):
        with allure.step(f'Find element with {locator}'):
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(*locator))

    def click_element(self, *locator, time=5):
        with allure.step(f'Click element with {locator}'):
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(*locator)).click()

    def url_checker(self, time=5):
        initial_window_handle = self.driver.current_window_handle

        with allure.step(f'Switch to new window, get url and close this window'):

            if len(self.driver.window_handles) > 1:
                try:
                    for window_handle in self.driver.window_handles:
                        if window_handle != initial_window_handle:
                            self.driver.switch_to.window(window_handle)
                            WebDriverWait(self.driver, time).until(EC.url_contains(DZEN))
                            break

                    new_url = self.driver.current_url
                    self.driver.close()
                    return new_url

                finally:
                    self.driver.switch_to.window(initial_window_handle)
                    pass

            else:
                with allure.step(f'Get current URL'):
                    return self.driver.current_url



