from time import sleep

import allure
import pytest

from locators import ScooterLocators
from page_object.order_page.order_page import OrderPage
from constants import Urls


class Test:
    locators = [ScooterLocators.ORDER_BUTTON_UPPER, ScooterLocators.ORDER_BUTTON_LOWER]

    @allure.title('Тест заказа самоката с переходом на главную')
    @pytest.mark.parametrize('locator', locators)
    def test_fill_order_form(self, driver, locator):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.HOME_PAGE_URL)
        order_page.find_element_located(ScooterLocators.COOKIE_BUTTON).click()
        order_page.find_element_located(locator).click()
        order_page.fill_form_first_page()
        order_page.find_element_located(ScooterLocators.NEXT_BUTTON).click()
        order_page.fill_form_second_page()
        order_page.find_element_located(ScooterLocators.ORDER_BUTTON).click()
        order_page.find_element_located(ScooterLocators.CONFIRM_BUTTON).click()
        successful_header_text = order_page.find_element_located(ScooterLocators.SUCCESSFUL_TEXT).text
        assert 'Заказ оформлен' in successful_header_text
        order_page.find_element_located(ScooterLocators.VIEW_BUTTON).click()
        order_page.find_element_located(ScooterLocators.CANCEL_ORDER_BUTTON)
        order_page.find_element_located(ScooterLocators.LOGO_SCOOTER_BUTTON).click()
        assert driver.current_url == Urls.HOME_PAGE_URL
        assert "на пару дней" in order_page.find_element_located(ScooterLocators.HOME_HEADER).text

    @allure.title('Тест заказа самоката с переходом на Дзен')
    def test_fill_order_form_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.HOME_PAGE_URL)
        order_page.find_element_located(ScooterLocators.COOKIE_BUTTON).click()
        order_page.find_element_located(ScooterLocators.ORDER_BUTTON_LOWER).click()
        order_page.fill_form_first_page()
        order_page.find_element_located(ScooterLocators.NEXT_BUTTON).click()
        order_page.fill_form_second_page()
        order_page.find_element_located(ScooterLocators.ORDER_BUTTON).click()
        order_page.find_element_located(ScooterLocators.CONFIRM_BUTTON).click()
        successful_header_text = order_page.find_element_located(ScooterLocators.SUCCESSFUL_TEXT).text
        assert 'Заказ оформлен' in successful_header_text
        order_page.find_element_located(ScooterLocators.VIEW_BUTTON).click()
        order_page.find_element_located(ScooterLocators.CANCEL_ORDER_BUTTON)
        order_page.find_element_located(ScooterLocators.LOGO_YANDEX_BUTTON).click()
        driver.switch_to.window(driver.window_handles[1])
        sleep(5)
        assert Urls.DZEN_PAGE_URL in driver.current_url