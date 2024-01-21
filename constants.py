from faker import Faker
import random

faker = Faker(['ru_RU'])

class Urls:
    HOME_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    DZEN_PAGE_URL = 'https://dzen.ru/?yredirect=true'
    ORDER_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/order'

class UserData:
    NAME = faker.first_name()
    LAST_NAME = faker.last_name()
    ADDRESS = faker.city_name()
    PHONE_NUMBER = random.randint(10000000000, 99999999999)
