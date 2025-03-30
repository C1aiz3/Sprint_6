from time import sleep
import allure
from src.data import FakeData as FD
from src.locators.order_page_locators import OrderPageLocators as OPL
from src.locators.main_page_locators import MainPageLocators as MPL
from src.pages.order_page import OrderPage


class TestOrderPageScooter:

    @allure.description('Проверяем переход через кнопку "Яндекс" к главной странице "Дзен", возвращаемся обратно, переходим на страницу оформления самоката через кнопку сверху на главной, заполняем данные и проверяем что заказ оформлен')
    @allure.title('Проверка перехода на главную "Дзена" и оформления самоката через кнопку "Заказать" сверху')
    def test_order_scooter_from_top_button(self, driver):
        scooter_order_page = OrderPage(driver)
        scooter_order_page.open_url()
        scooter_order_page.accept_cookies()
        scooter_order_page.click_element(MPL.dzen_button)
        sleep(3)
        assert scooter_order_page.url_checker() == 'https://dzen.ru/?yredirect=true'
        scooter_order_page.click_element(MPL.top_order_button)
        scooter_order_page.fill_the_field(OPL.first_name, FD.f_name())
        scooter_order_page.fill_the_field(OPL.second_name, FD.l_name())
        scooter_order_page.fill_the_field(OPL.address_locator, FD.city())
        scooter_order_page.click_element(OPL.metro_station_field)
        scooter_order_page.click_element(OPL.metro_station_variant)
        scooter_order_page.fill_the_field(OPL.phone_number, FD.phone_number())
        scooter_order_page.click_element(OPL.next_button)
        scooter_order_page.fill_the_field(OPL.date, FD.date())
        scooter_order_page.escape_imitation()
        scooter_order_page.click_element(OPL.rental_period)
        scooter_order_page.click_element(OPL.rent_variant1)
        scooter_order_page.click_element(OPL.black_color)
        scooter_order_page.fill_the_field(OPL.comment, FD.comment())
        scooter_order_page.click_element(OPL.order_button)
        scooter_order_page.click_element(OPL.yes_button)
        assert scooter_order_page.find_element(OPL.order_placed_window).is_displayed()

    @allure.description('Проверяем возврат на главную через кнопку "Самокат" со станицы оформления заказа, затем переходим к оформлению самоката через кнопку в центре главной страницы, заполняем данные и проверяем что заказ оформлен')
    @allure.title('Проверка перехода на главную и оформления самоката через кнопку "Заказать" по центру')
    def test_order_scooter_from_bottom_button(self, driver):
        scooter_order_page = OrderPage(driver)
        scooter_order_page.open_url()
        scooter_order_page.accept_cookies()
        scooter_order_page.click_element(MPL.bottom_order_button)
        scooter_order_page.click_element(MPL.scooter_main_page_button)
        assert scooter_order_page.current_page_url() == 'https://qa-scooter.praktikum-services.ru/'
        scooter_order_page.click_element(MPL.bottom_order_button)
        scooter_order_page.fill_the_field(OPL.first_name, FD.f_name())
        scooter_order_page.fill_the_field(OPL.second_name, FD.l_name())
        scooter_order_page.fill_the_field(OPL.address_locator, FD.city())
        scooter_order_page.click_element(OPL.metro_station_field)
        scooter_order_page.click_element(OPL.metro_station_variant)
        scooter_order_page.fill_the_field(OPL.phone_number, FD.phone_number())
        scooter_order_page.click_element(OPL.next_button)
        scooter_order_page.fill_the_field(OPL.date, FD.date())
        scooter_order_page.escape_imitation()
        scooter_order_page.click_element(OPL.rental_period)
        scooter_order_page.click_element(OPL.rent_variant2)
        scooter_order_page.click_element(OPL.grey_color)
        scooter_order_page.fill_the_field(OPL.comment, FD.comment())
        scooter_order_page.click_element(OPL.order_button)
        scooter_order_page.click_element(OPL.yes_button)
        assert scooter_order_page.find_element(OPL.order_placed_window).is_displayed()
