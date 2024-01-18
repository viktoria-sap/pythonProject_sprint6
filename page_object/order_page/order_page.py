import allure
from faker import Faker
import random
from datetime import date, timedelta

from page_object.base_page import BasePage
from locators import ScooterLocators

faker = Faker(['ru_RU'])

class OrderPage(BasePage):
    @allure.step("Заполнение полей первой страницы заказа")
    def fill_form_first_page(self):
        name = faker.first_name()
        second_name = faker.last_name()
        address = faker.city_name()
        phone_number = random.randint(10000000000, 99999999999)
        self.find_element_located(ScooterLocators.FIRST_NAME_INPUT).send_keys(name)
        self.find_element_located(ScooterLocators.SECOND_NAME_INPUT).send_keys(second_name)
        self.find_element_located(ScooterLocators.ADDRESS_INPUT).send_keys(address)
        self.find_element_located(ScooterLocators.PHONE_NUMBER_INPUT).send_keys(phone_number)
        self.find_element_located(ScooterLocators.METRO_STATION_FIELD).click()
        self.find_element_located(ScooterLocators.FIRST_OPTION_METRO_STATION_FIELD).click()

    @allure.step("Заполнение полей второй страницы заказа")
    def fill_form_second_page(self):
        tomorrow = date.today() + timedelta(days=1)
        self.find_element_located(ScooterLocators.WHEN_INPUT).send_keys(tomorrow.strftime('%d.%m.%y'))
        self.find_element_located(ScooterLocators.ORDER_HEADER).click()
        self.find_element_located(ScooterLocators.PERIOD_INPUT).click()
        self.find_element_located(ScooterLocators.SECOND_OPTION_PERIOD_INPUT).click()

