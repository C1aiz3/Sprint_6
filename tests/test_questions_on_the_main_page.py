import allure
from src.locators.main_page_locators import MainPageLocators as MPL
from src.pages.main_page import MainPage


class TestQuestionsText:


    def test_first_question(self, driver):
        with allure.step(f'Check first question answer text'):
            scooter_main_page = MainPage(driver)
            scooter_main_page.open_url()
            scooter_main_page.accept_cookies()
            scooter_main_page.click_element(MPL.first_question)
            assert scooter_main_page.find_element(MPL.first_answer).text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_second_question(self, driver):
        with allure.step(f'Check second question answer text'):
            scooter_main_page = MainPage(driver)
            scooter_main_page.open_url()
            scooter_main_page.accept_cookies()
            scooter_main_page.click_element(MPL.second_question)
            assert scooter_main_page.find_element(MPL.second_answer).text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_third_question(self, driver):
        with allure.step(f'Check third question answer text'):
            scooter_main_page = MainPage(driver)
            scooter_main_page.open_url()
            scooter_main_page.accept_cookies()
            scooter_main_page.click_element(MPL.third_question)
            assert scooter_main_page.find_element(MPL.third_answer).text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_fourth_question(self, driver):
        with allure.step(f'Check fourth question answer text'):
            scooter_main_page = MainPage(driver)
            scooter_main_page.open_url()
            scooter_main_page.accept_cookies()
            scooter_main_page.click_element(MPL.fourth_question)
            assert scooter_main_page.find_element(MPL.fourth_answer).text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_fiveth_question(self, driver):
        with allure.step(f'Check fiveth question answer text'):
            scooter_main_page = MainPage(driver)
            scooter_main_page.open_url()
            scooter_main_page.accept_cookies()
            scooter_main_page.click_element(MPL.fiveth_question)
            assert scooter_main_page.find_element(MPL.fiveth_answer).text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_sixth_question(self, driver):
        with allure.step(f'Check sixth question answer text'):
            scooter_main_page = MainPage(driver)
            scooter_main_page.open_url()
            scooter_main_page.accept_cookies()
            scooter_main_page.click_element(MPL.sixth_question)
            assert scooter_main_page.find_element(MPL.sixth_answer).text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_seventh_question(self, driver):
        with allure.step(f'Check seventh question answer text'):
            scooter_main_page = MainPage(driver)
            scooter_main_page.open_url()
            scooter_main_page.accept_cookies()
            scooter_main_page.click_element(MPL.seventh_question)
            assert scooter_main_page.find_element(MPL.seventh_answer).text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_eighth_question(self, driver):
        with allure.step(f'Check eighth question answer text'):
            scooter_main_page = MainPage(driver)
            scooter_main_page.open_url()
            scooter_main_page.accept_cookies()
            scooter_main_page.click_element(MPL.eighth_question)
            assert scooter_main_page.find_element(MPL.eighth_answer).text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'