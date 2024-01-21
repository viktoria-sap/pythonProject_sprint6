import allure
from datetime import date, timedelta
from time import sleep
from constants import Urls

from page_object.base_page import BasePage
from locators import ScooterLocators
from constants import UserData


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.successful_header_text = None

    @allure.step("Заполнение полей первой страницы заказа")
    def fill_form_first_page(self):
        name = UserData.NAME
        last_name = UserData.LAST_NAME
        address = UserData.ADDRESS
        phone_number = UserData.PHONE_NUMBER
        self.find_element_located(ScooterLocators.FIRST_NAME_INPUT).send_keys(name)
        self.find_element_located(ScooterLocators.SECOND_NAME_INPUT).send_keys(last_name)
        self.find_element_located(ScooterLocators.ADDRESS_INPUT).send_keys(address)
        self.find_element_located(ScooterLocators.PHONE_NUMBER_INPUT).send_keys(phone_number)
        self.find_element_located(ScooterLocators.METRO_STATION_FIELD).click()
        self.find_element_located(ScooterLocators.FIRST_OPTION_METRO_STATION_FIELD).click()
        self.find_element_located(ScooterLocators.NEXT_BUTTON).click()

    @allure.step("Заполнение полей второй страницы заказа")
    def fill_form_second_page(self):
        tomorrow = date.today() + timedelta(days=1)
        self.find_element_located(ScooterLocators.WHEN_INPUT).send_keys(tomorrow.strftime('%d.%m.%y'))
        self.find_element_located(ScooterLocators.ORDER_HEADER).click()
        self.find_element_located(ScooterLocators.PERIOD_INPUT).click()
        self.find_element_located(ScooterLocators.SECOND_OPTION_PERIOD_INPUT).click()

    @allure.step("Переход к логотипам")
    def go_to_logo(self, button, index):
        self.driver.get(Urls.ORDER_PAGE_URL)
        self.find_element_located(button).click()
        self.driver.switch_to.window(self.driver.window_handles[index])
        sleep(5)

    @allure.step("Старт заказа и переход к форме")
    def start_of_order(self, locator):
        self.driver.get(Urls.HOME_PAGE_URL)
        self.find_element_located(ScooterLocators.COOKIE_BUTTON).click()
        self.find_element_located(locator).click()

    @allure.step("Подтверждение заказа")
    def confirm_of_order(self):
        self.find_element_located(ScooterLocators.ORDER_BUTTON).click()
        self.find_element_located(ScooterLocators.CONFIRM_BUTTON).click()
        self.successful_header_text = self.find_element_located(ScooterLocators.SUCCESSFUL_TEXT).text
