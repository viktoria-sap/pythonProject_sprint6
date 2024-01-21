import allure

from locators import ScooterLocators
from page_object.faq_page.faq_page import FaqPage


class Test:
    @allure.title('Тест вопроса о стоимости и оплате')
    def test_faq_how_much_question(self, driver):
        faq_page = FaqPage(driver)
        faq_page.faq_get_any_question(ScooterLocators.ACCORDION_BUTTON_HOW_MUCH_QUESTION, ScooterLocators.ACCORDION_PANEL_HOW_MUCH_QUESTION)
        assert 'Сколько это стоит? И как оплатить?' in faq_page.button_question_text and 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.' in faq_page.panel_question_text


    @allure.title('Тест вопроса о количестве самокатов в заказе')
    def test_faq_want_few_question(self, driver):
        faq_page = FaqPage(driver)
        faq_page.faq_get_any_question(ScooterLocators.ACCORDION_BUTTON_WANT_FEW_QUESTION, ScooterLocators.ACCORDION_PANEL_WANT_FEW_QUESTION)
        assert 'Хочу сразу несколько самокатов! Так можно?' in faq_page.button_question_text and 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.' in faq_page.panel_question_text


    @allure.title('Тест вопроса о времени аренды')
    def test_faq_time_calculation_question(self, driver):
        faq_page = FaqPage(driver)
        faq_page.faq_get_any_question(ScooterLocators.ACCORDION_BUTTON_TIME_CALCULATION_QUESTION, ScooterLocators.ACCORDION_PANEL_TIME_CALCULATION_QUESTION)
        assert 'Как рассчитывается время аренды?' in faq_page.button_question_text and 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.' in faq_page.panel_question_text


    @allure.title('Тест вопроса о заказе день в день')
    def test_faq_urgent_order_question(self, driver):
        faq_page = FaqPage(driver)
        faq_page.faq_get_any_question(ScooterLocators.ACCORDION_BUTTON_URGENT_ORDER_QUESTION, ScooterLocators.ACCORDION_PANEL_URGENT_ORDER_QUESTION)
        assert 'Можно ли заказать самокат прямо на сегодня?' in faq_page.button_question_text and 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.' in faq_page.panel_question_text


    @allure.title('Тест вопроса о продлении и возврате')
    def test_faq_return_renew_question(self, driver):
        faq_page = FaqPage(driver)
        faq_page.faq_get_any_question(ScooterLocators.ACCORDION_BUTTON_RETURN_RENEW_QUESTION, ScooterLocators.ACCORDION_PANEL_RETURN_RENEW_QUESTION)
        assert 'Можно ли продлить заказ или вернуть самокат раньше?' in faq_page.button_question_text and 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.' in faq_page.panel_question_text


    @allure.title('Тест вопроса о зарядке')
    def test_faq_charge_question(self, driver):
        faq_page = FaqPage(driver)
        faq_page.faq_get_any_question(ScooterLocators.ACCORDION_BUTTON_CHARGE_QUESTION, ScooterLocators.ACCORDION_PANEL_CHARGE_QUESTION)
        assert 'Вы привозите зарядку вместе с самокатом?' in faq_page.button_question_text and 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.' in faq_page.panel_question_text


    @allure.title('Тест вопроса об отмене')
    def test_faq_cancel_question(self, driver):
        faq_page = FaqPage(driver)
        faq_page.faq_get_any_question(ScooterLocators.ACCORDION_BUTTON_CANCEL_QUESTION, ScooterLocators.ACCORDION_PANEL_CANCEL_QUESTION)
        assert 'Можно ли отменить заказ?' in faq_page.button_question_text and 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.' in faq_page.panel_question_text


    @allure.title('Тест вопроса о доставке за МКАД')
    def test_faq_far_delivery_question(self, driver):
        faq_page = FaqPage(driver)
        faq_page.faq_get_any_question(ScooterLocators.ACCORDION_BUTTON_FAR_DELIVERY_QUESTION, ScooterLocators.ACCORDION_PANEL_FAR_DELIVERY_QUESTION)
        assert 'Я жизу за МКАДом, привезёте?' in faq_page.button_question_text and 'Да, обязательно. Всем самокатов! И Москве, и Московской области.' in faq_page.panel_question_text






