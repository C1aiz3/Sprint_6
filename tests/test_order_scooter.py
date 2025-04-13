import allure
import pytest

from src.data import FakeData as FD, ORDER_SCENARIOS
from src.locators.order_page_locators import OrderPageLocators as OPL
from src.pages.order_page import OrderPage




class TestOrderPageScooter:
    @pytest.mark.parametrize("navigate_button, expected_url, order_button, rental_option, color_option", ORDER_SCENARIOS)
    def test_order_scooter(self, driver, navigate_button, expected_url, order_button, rental_option, color_option):
        scooter_order_page = OrderPage(driver)
        scooter_order_page.open_url('order')
        scooter_order_page.accept_cookies()

        with allure.step("Check Yandex/Scooter transition"):

            scooter_order_page.click_element(navigate_button)
            assert scooter_order_page.url_checker() == expected_url

        with allure.step("Order scooter on order page"):

            scooter_order_page.click_element(order_button)
            scooter_order_page.fill_the_field(OPL.FIRST_NAME, FD.f_name())
            scooter_order_page.fill_the_field(OPL.SECOND_NAME, FD.l_name())
            scooter_order_page.fill_the_field(OPL.ADDRESS_LOCATOR, FD.city())
            scooter_order_page.click_element(OPL.METRO_STATION_FIELD)
            scooter_order_page.click_element(OPL.METRO_STATION_VARIANT)
            scooter_order_page.fill_the_field(OPL.PHONE_NUMBER, FD.phone_number())
            scooter_order_page.click_element(OPL.NEXT_BUTTON)
            scooter_order_page.fill_the_field(OPL.DATE, FD.date())
            scooter_order_page.escape_imitation()
            scooter_order_page.click_element(OPL.RENTAL_PERIOD)
            scooter_order_page.click_element(rental_option)
            scooter_order_page.click_element(color_option)
            scooter_order_page.fill_the_field(OPL.COMMENT, FD.comment())
            scooter_order_page.click_element(OPL.ORDER_BUTTON)
            scooter_order_page.click_element(OPL.YES_BUTTON)
            assert scooter_order_page.find_element(OPL.ORDER_PLACED_WINDOW).is_displayed()
