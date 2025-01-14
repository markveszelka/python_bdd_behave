from src.pageObjects.constants.constants import Constants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style, init

init()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by, value):
        self.driver.find_element(by, value).click()

    def is_text_visible(self, locator, text):
        try:
            _element = self.driver.find_element(*locator)
            if _element.is_displayed():
                return text in _element.text
            else:
                return False
        except Exception as e:
            print(f'Error occurred while checking text visibility: {e}')
            return False

    def load_given_page(self, page):
        if page.lower() == 'home':
            self.driver.get(Constants.HOME_PAGE_URL.value)
            WebDriverWait(self.driver, 10).until(EC.title_contains(Constants.HOME_PAGE_TEXT.value))
        elif page.lower() == 'login':
            self.driver.get(Constants.LOGIN_PAGE_URL.value)
            WebDriverWait(self.driver, 10).until(EC.title_contains(Constants.LOGIN_PAGE_TEXT.value))
        else:
            raise ValueError(f'{Fore.YELLOW}{Style.BRIGHT}Page "{page}" is not implemented yet{Style.RESET_ALL}')
