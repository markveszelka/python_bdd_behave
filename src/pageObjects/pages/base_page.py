from src.data.time_outs import TimeOut
from src.pageObjects.constants.constants import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from colorama import Fore, Style, init

init()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by, value):
        self.driver.find_element(by, value).click()

    def click_element_by_text(self, button_text: str):
        self.click_element(By.LINK_TEXT, button_text)

    def is_text_visible(self, locator, text) -> bool:
        try:
            _element = self.driver.find_element(*locator)
            if _element.is_displayed():
                return text in _element.text
            else:
                return False
        except Exception as e:
            print(f'Error occurred while checking text visibility: {e}')
            return False

    def is_element_visible(self, locator) -> bool:
        try:
            element: WebElement = self.driver.find_element(*locator)
            return element.is_displayed()
        except Exception as e:
            print(f'Error occurred while checking element visibility: {e}')
            return False

    def load_given_page(self, page):
        print("LOAD GIVEN PAGE")
        if page.lower() == 'home':
            self.driver.get(URLs.HOME_PAGE_URL)
            WebDriverWait(self.driver, TimeOut.MEDIUM.value).until(EC.title_contains(Texts.HOME_PAGE_TEXT))
        elif page.lower() == 'login':
            print(URLs.LOGIN_PAGE_URL)
            self.driver.get(URLs.LOGIN_PAGE_URL)
            WebDriverWait(self.driver, TimeOut.MEDIUM.value).until(EC.title_contains(Texts.LOGIN_PAGE_TEXT))
        else:
            raise ValueError(f'{Fore.YELLOW}{Style.BRIGHT}Page "{page}" is not implemented yet{Style.RESET_ALL}')
