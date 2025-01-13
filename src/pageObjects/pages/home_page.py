from src.pageObjects.locators.locators import Locators
from src.pageObjects.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_login_button(self):
        sign_in_button_locator = Locators.SIGN_IN_BUTTON.value
        self.driver.find_element(*sign_in_button_locator).click()
