from page_object.base_page import BasePage
from constants import Urls


class FaqPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.panel_question_text = None
        self.button_question_text = None

    def faq_get_any_question(self, locator_button, locator_panel):
        self.driver.get(Urls.HOME_PAGE_URL)
        button_question = self.find_element_located(locator_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button_question)
        self.button_question_text = button_question.text
        button_question.click()
        panel_question = self.find_element_located(locator_panel)
        self.panel_question_text = panel_question.text



