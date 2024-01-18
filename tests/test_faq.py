import allure

from locators import ScooterLocators
from page_object.base_page import BasePage
from constants import Urls


class Test:
    @allure.title('Тест вопроса о стоимости и оплате')
    def test_faq_how_much_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site(Urls.HOME_PAGE_URL)
        button_question = base_page.find_element_located(ScooterLocators.ACCORDION_BUTTON_HOW_MUCH_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", button_question)
        button_question_text = button_question.text
        assert 'Сколько это стоит? И как оплатить?' in button_question_text
        button_question.click()
        panel_question = base_page.find_element_located(ScooterLocators.ACCORDION_PANEL_HOW_MUCH_QUESTION)
        panel_question_text = panel_question.text
        assert 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.' in panel_question_text

    @allure.title('Тест вопроса о количестве самокатов в заказе')
    def test_faq_want_few_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site(Urls.HOME_PAGE_URL)
        button_question = base_page.find_element_located(ScooterLocators.ACCORDION_BUTTON_WANT_FEW_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", button_question)
        button_question_text = button_question.text
        assert 'Хочу сразу несколько самокатов! Так можно?' in button_question_text
        button_question.click()
        panel_question = base_page.find_element_located(ScooterLocators.ACCORDION_PANEL_WANT_FEW_QUESTION)
        panel_question_text = panel_question.text
        assert 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.' in panel_question_text

    @allure.title('Тест вопроса о времени аренды')
    def test_faq_time_calculation_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site(Urls.HOME_PAGE_URL)
        button_question = base_page.find_element_located(ScooterLocators.ACCORDION_BUTTON_TIME_CALCULATION_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", button_question)
        button_question_text = button_question.text
        assert 'Как рассчитывается время аренды?' in button_question_text
        button_question.click()
        panel_question = base_page.find_element_located(ScooterLocators.ACCORDION_PANEL_TIME_CALCULATION_QUESTION)
        panel_question_text = panel_question.text
        assert 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.' in panel_question_text

    @allure.title('Тест вопроса о заказе день в день')
    def test_faq_urgent_order_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site(Urls.HOME_PAGE_URL)
        button_question = base_page.find_element_located(ScooterLocators.ACCORDION_BUTTON_URGENT_ORDER_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", button_question)
        button_question_text = button_question.text
        assert 'Можно ли заказать самокат прямо на сегодня?' in button_question_text
        button_question.click()
        panel_question = base_page.find_element_located(ScooterLocators.ACCORDION_PANEL_URGENT_ORDER_QUESTION)
        panel_question_text = panel_question.text
        assert 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.' in panel_question_text

    @allure.title('Тест вопроса о продлении и возврате')
    def test_faq_return_renew_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site(Urls.HOME_PAGE_URL)
        button_question = base_page.find_element_located(ScooterLocators.ACCORDION_BUTTON_RETURN_RENEW_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", button_question)
        button_question_text = button_question.text
        assert 'Можно ли продлить заказ или вернуть самокат раньше?' in button_question_text
        button_question.click()
        panel_question = base_page.find_element_located(ScooterLocators.ACCORDION_PANEL_RETURN_RENEW_QUESTION)
        panel_question_text = panel_question.text
        assert 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.' in panel_question_text

    @allure.title('Тест вопроса о зарядке')
    def test_faq_charge_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site(Urls.HOME_PAGE_URL)
        button_question = base_page.find_element_located(ScooterLocators.ACCORDION_BUTTON_CHARGE_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", button_question)
        button_question_text = button_question.text
        assert 'Вы привозите зарядку вместе с самокатом?' in button_question_text
        button_question.click()
        panel_question = base_page.find_element_located(ScooterLocators.ACCORDION_PANEL_CHARGE_QUESTION)
        panel_question_text = panel_question.text
        assert 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.' in panel_question_text

    @allure.title('Тест вопроса об отмене')
    def test_faq_cancel_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site(Urls.HOME_PAGE_URL)
        button_question = base_page.find_element_located(ScooterLocators.ACCORDION_BUTTON_CANCEL_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", button_question)
        button_question_text = button_question.text
        assert 'Можно ли отменить заказ?' in button_question_text
        button_question.click()
        panel_question = base_page.find_element_located(ScooterLocators.ACCORDION_PANEL_CANCEL_QUESTION)
        panel_question_text = panel_question.text
        assert 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.' in panel_question_text

    @allure.title('Тест вопроса о доставке за МКАД')
    def test_faq_far_delivery_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site(Urls.HOME_PAGE_URL)
        button_question = base_page.find_element_located(ScooterLocators.ACCORDION_BUTTON_FAR_DELIVERY_QUESTION)
        driver.execute_script("arguments[0].scrollIntoView();", button_question)
        button_question_text = button_question.text
        assert 'Я жизу за МКАДом, привезёте?' in button_question_text
        button_question.click()
        panel_question = base_page.find_element_located(ScooterLocators.ACCORDION_PANEL_FAR_DELIVERY_QUESTION)
        panel_question_text = panel_question.text
        assert 'Да, обязательно. Всем самокатов! И Москве, и Московской области.' in panel_question_text





