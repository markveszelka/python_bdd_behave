from selenium.webdriver.common.by import By
from src.pageObjects.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # TODO: refactor locators to constants, maybe class attributes?
    def are_login_elements_visible(self):
        try:
            _email_locator = (By.ID, 'email')
            _email_element = self.driver.find_element(*_email_locator)
            if not _email_element.is_displayed():
                return False

            _password_locator = (By.ID, 'pass')
            _password_element = self.driver.find_element(*_password_locator)
            if not _password_element.is_displayed():
                return False

            _sign_in_button_locator = (By.LINK_TEXT, 'Sign In')
            _sign_in_button_element = self.driver.find_element(*_sign_in_button_locator)
            if not _sign_in_button_element.is_displayed():
                return False

            return True

        except Exception as e:
            print(f'Error occurred while checking home page elements: {e}')
            return False

    # TODO: refactor locators to constants, maybe class attributes?
    def trigger_login(self, email, password):
        _sign_in_button_locator = (By.ID, 'send2')

        self.driver.find_element(By.ID, 'email').send_keys(email)
        self.driver.find_element(By.ID, 'pass').send_keys(password)
        self.driver.find_element(*_sign_in_button_locator).click()

    def is_invalid_credentials_error_message_visible(self):
        try:
            _error_message_locator = (
                By.XPATH, '//div[contains(@class, "message-error") and @data-ui-id="message-error"]')
            _error_message_element = self.driver.find_element(*_error_message_locator)

            _error_message_text_locator = (
                By.XPATH, '//div[@class="message-error error message" and @data-ui-id="message-error"]//div')
            _error_message_text = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'

            return (_error_message_element.is_displayed()
                    and self.is_text_visible(_error_message_text_locator,
                                             _error_message_text))

        except Exception as e:
            print(f'Error occurred while checking error message: {e}')
            return False

    def is_logged_in(self):
        try:
            _account_name_locator = (By.XPATH, '//span[@class="logged-in"]')
            _account_name_element = self.driver.find_element(*_account_name_locator)

            return _account_name_element.is_displayed()

        except Exception as e:
            print(f'Error occurred while checking account name: {e}')
            return False

    def is_email_and_password_error_visible(self):
        try:
            _email_error_locator = (By.ID, 'email-error')
            _email_error_element = self.driver.find_element(*_email_error_locator)

            _password_error_locator = (By.ID, 'pass-error')
            _password_error_element = self.driver.find_element(*_password_error_locator)

            return (_email_error_element.is_displayed()
                    and _password_error_element.is_displayed())

        except Exception as e:
            print(f'Error occurred while checking email and password error: {e}')
            return False

    def click_sign_in_button(self):
        _sign_in_button_locator = (By.ID, 'send2')
        self.driver.find_element(*_sign_in_button_locator).click()
