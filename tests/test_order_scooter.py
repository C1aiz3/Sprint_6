import allure
import pytest

from src.data import FakeData as FD, ORDER_SCENARIOS
from src.locators.order_page_locators import OrderPageLocators as OPL
from src.pages.order_page import OrderPage




class TestOrderPageScooter:
    @pytest.mark.parametrize("navigate_button, expected_url, order_button, rental_option, color_option", ORDER_SCENARIOS)
    def test_order_scooter(self, driver, navigate_button, expected_url, order_button, rental_option, color_option):
        page = OrderPage(driver)
        page.open_url('order')
        page.accept_cookies()


        page.click_element(navigate_button)

        assert page.url_checker() == expected_url

        page.click_element(order_button)
        page.fill_the_field(OPL.FIRST_NAME, FD.f_name())
        page.fill_the_field(OPL.SECOND_NAME, FD.l_name())
        page.fill_the_field(OPL.ADDRESS_LOCATOR, FD.city())
        page.click_element(OPL.METRO_STATION_FIELD)
        page.click_element(OPL.METRO_STATION_VARIANT)
        page.fill_the_field(OPL.PHONE_NUMBER, FD.phone_number())
        page.click_element(OPL.NEXT_BUTTON)
        page.fill_the_field(OPL.DATE, FD.date())
        page.escape_imitation()
        page.click_element(OPL.RENTAL_PERIOD)
        page.click_element(rental_option)
        page.click_element(color_option)
        page.fill_the_field(OPL.COMMENT, FD.comment())
        page.click_element(OPL.ORDER_BUTTON)
        page.click_element(OPL.YES_BUTTON)
        assert page.find_element(OPL.ORDER_PLACED_WINDOW).is_displayed()
