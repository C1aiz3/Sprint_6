from src.locators.main_page_locators import MainPageLocators as MPL
from src.locators.order_page_locators import OrderPageLocators as OPL
from random import randint
from faker import Faker

fake = Faker('ru_RU')

class FakeData:

    @staticmethod
    def f_name():
        return fake.first_name()

    @staticmethod
    def l_name():
        return fake.last_name()

    @staticmethod
    def city():
        city = fake.city()
        return city[:13].split()[1]

    @staticmethod
    def phone_number():
        return f'8{randint(1111111111, 9999999999)}'

    @staticmethod
    def date():
        return fake.date("%d.%m.%Y")

    @staticmethod
    def comment():
        return fake.text()


URL = 'https://qa-scooter.praktikum-services.ru/'
DZEN = 'https://dzen.ru/?yredirect=true'
SCOOTER_MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
QUESTIONS_ANSWERS = [
    (MPL.FIRST_QUESTION, MPL.FIRST_ANSWER, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    (MPL.SECOND_QUESTION, MPL.SECOND_ANSWER,
     'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
    (MPL.THIRD_QUESTION, MPL.THIRD_ANSWER,
     'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    (MPL.FOURTH_QUESTION, MPL.FOURTH_ANSWER, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    (MPL.FIVETH_QUESTION, MPL.FIVETH_ANSWER,
     'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    (MPL.SIXTH_QUESTION, MPL.SIXTH_ANSWER,
     'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
    (MPL.SEVENTH_QUESTION, MPL.SEVENTH_ANSWER,
     'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    (MPL.EIGHTH_QUESTION, MPL.EIGHTH_ANSWER, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'),
]

ORDER_SCENARIOS = [
    (MPL.DZEN_BUTTON, DZEN, MPL.TOP_ORDER_BUTTON, OPL.RENT_VARIANT1, OPL.BLACK_COLOR),
    (MPL.SCOOTER_MAIN_PAGE_BUTTON, URL, MPL.BOTTOM_ORDER_BUTTON, OPL.RENT_VARIANT2, OPL.GREY_COLOR)
]




