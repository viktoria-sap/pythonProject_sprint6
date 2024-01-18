from selenium.webdriver.common.by import By


class ScooterLocators:
    ACCORDION_BUTTON_HOW_MUCH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-0']")
    ACCORDION_BUTTON_WANT_FEW_QUESTION = (By.XPATH, "//div[@id='accordion__heading-1']")
    ACCORDION_BUTTON_TIME_CALCULATION_QUESTION = (By.XPATH, "//div[@id='accordion__heading-2']")
    ACCORDION_BUTTON_URGENT_ORDER_QUESTION = (By.XPATH, "//div[@id='accordion__heading-3']")
    ACCORDION_BUTTON_RETURN_RENEW_QUESTION = (By.XPATH, "//div[@id='accordion__heading-4']")
    ACCORDION_BUTTON_CHARGE_QUESTION = (By.XPATH, "//div[@id='accordion__heading-5']")
    ACCORDION_BUTTON_CANCEL_QUESTION = (By.XPATH, "//div[@id='accordion__heading-6']")
    ACCORDION_BUTTON_FAR_DELIVERY_QUESTION = (By.XPATH, "//div[@id='accordion__heading-7']")

    ACCORDION_PANEL_HOW_MUCH_QUESTION = (By.XPATH, "//div[@id='accordion__panel-0']")
    ACCORDION_PANEL_WANT_FEW_QUESTION = (By.XPATH, "//div[@id='accordion__panel-1']")
    ACCORDION_PANEL_TIME_CALCULATION_QUESTION = (By.XPATH, "//div[@id='accordion__panel-2']")
    ACCORDION_PANEL_URGENT_ORDER_QUESTION = (By.XPATH, "//div[@id='accordion__panel-3']")
    ACCORDION_PANEL_RETURN_RENEW_QUESTION = (By.XPATH, "//div[@id='accordion__panel-4']")
    ACCORDION_PANEL_CHARGE_QUESTION = (By.XPATH, "//div[@id='accordion__panel-5']")
    ACCORDION_PANEL_CANCEL_QUESTION = (By.XPATH, "//div[@id='accordion__panel-6']")
    ACCORDION_PANEL_FAR_DELIVERY_QUESTION = (By.XPATH, "//div[@id='accordion__panel-7']")

    ORDER_BUTTON_UPPER = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_LOWER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    VIEW_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    CANCEL_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']")
    LOGO_SCOOTER_BUTTON = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX_BUTTON = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    HOME_HEADER = (By.XPATH, "//div[@class='Home_Header__iJKdX']")

    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SECOND_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    WHEN_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_INPUT = (By.XPATH, "//div[@class='Dropdown-control']")
    SECOND_OPTION_PERIOD_INPUT = (By.XPATH, "//div[text()='двое суток']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@class='select-search__input']")
    FIRST_OPTION_METRO_STATION_FIELD = (By.XPATH, "//div[text()='Бульвар Рокоссовского']")
    SUCCESSFUL_TEXT = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    ORDER_HEADER = (By.XPATH, "//div[@class='Order_Header__BZXOb']")

