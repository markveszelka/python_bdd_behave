from selenium.webdriver.common.by import By
from src.pageObjects.constants.constants import Constants
from src.pageObjects.pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT_LOCATOR = (By.ID, 'email')
    PASSWORD_INPUT_LOCATOR = (By.ID, 'pass')
    SIGN_IN_BUTTON_LOCATOR = (By.ID, 'send2')
    ERROR_MESSAGE_LOCATOR = (
        By.XPATH, '//div[contains(@class, "message-error") and @data-ui-id="message-error"]'
    )
    ERROR_MESSAGE_TEXT_LOCATOR = (
        By.XPATH, '//div[@class="message-error error message" and @data-ui-id="message-error"]//div'
    )
    ACCOUNT_NAME_LOCATOR = (By.XPATH, '//span[@class="logged-in"]')
    EMAIL_ERROR_LOCATOR = (By.ID, 'email-error')
    PASSWORD_ERROR_LOCATOR = (By.ID, 'pass-error')

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def are_login_elements_visible(self) -> bool:
        return all([
            self.is_element_visible(self.EMAIL_INPUT_LOCATOR),
            self.is_element_visible(self.PASSWORD_INPUT_LOCATOR),
            self.is_element_visible(self.SIGN_IN_BUTTON_LOCATOR)
        ])

    def trigger_login(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT_LOCATOR).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR).send_keys(password)
        self.click_element(*self.SIGN_IN_BUTTON_LOCATOR)

    def is_invalid_credentials_error_message_visible(self) -> bool:
        try:
            error_visible = self.is_element_visible(self.ERROR_MESSAGE_LOCATOR)
            text_visible = self.is_text_visible(self.ERROR_MESSAGE_TEXT_LOCATOR,
                                                Constants.INVALID_CREDENTIALS_ERROR_MESSAGE)
            return error_visible and text_visible
        except Exception as e:
            print(f"Error checking invalid credentials message visibility: {e}")
            return False

    def is_logged_in(self) -> bool:
        return self.is_element_visible(self.ACCOUNT_NAME_LOCATOR)

    def is_email_and_password_error_visible(self):
        return all([
            self.is_element_visible(self.EMAIL_ERROR_LOCATOR),
            self.is_element_visible(self.PASSWORD_ERROR_LOCATOR)
        ])

    def click_sign_in_button(self):
        self.click_element(*self.SIGN_IN_BUTTON_LOCATOR)
