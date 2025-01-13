from src.pageObjects.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)