import allure
import pytest

from locators import ScooterLocators
from page_object.order_page.order_page import OrderPage
from constants import Urls


class Test:

    @pytest.mark.parametrize('locator,',
                             [ScooterLocators.ORDER_BUTTON_UPPER,
                              ScooterLocators.ORDER_BUTTON_LOWER])
    @allure.title('Тест заказа самоката')
    def test_fill_order_form(self, driver, locator):
        order_page = OrderPage(driver)
        order_page.start_of_order(locator)
        order_page.fill_form_first_page()
        order_page.fill_form_second_page()
        order_page.confirm_of_order()
        assert 'Заказ оформлен' in order_page.successful_header_text

    @pytest.mark.parametrize('button, index, url',
                             [(ScooterLocators.LOGO_SCOOTER_BUTTON, 0, Urls.HOME_PAGE_URL), (ScooterLocators.LOGO_YANDEX_BUTTON, 1, Urls.DZEN_PAGE_URL)])
    @allure.title('Переход по логотипам')
    def test_go_to_logo(self, driver, button, index, url):
        order_page = OrderPage(driver)
        order_page.go_to_logo(button, index)
        assert url in driver.current_url

