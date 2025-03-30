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


url = 'https://qa-scooter.praktikum-services.ru/'





