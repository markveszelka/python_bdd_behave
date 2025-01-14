from selenium.webdriver.common.by import By
from src.pageObjects.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # TODO: refactor locators to constants, maybe class attributes?
    def are_home_elements_visible(self):
        try:
            _navigation_menu_locator = (By.ID, 'ui-id-2')
            _navigation_menu_element = self.driver.find_element(*_navigation_menu_locator)
            if not _navigation_menu_element.is_displayed():
                return False

            _promo_image_locator = (By.CLASS_NAME, 'blocks-promo')
            _promo_image_element = self.driver.find_element(*_promo_image_locator)
            if not _promo_image_element.is_displayed():
                return False

            _home_page_title_locator = (By.CLASS_NAME, 'base')
            _home_page_title_element = self.driver.find_element(*_home_page_title_locator)
            if not _home_page_title_element.is_displayed():
                return False

            return True

        except Exception as e:
            print(f'Error occurred while checking home page elements: {e}')
            return False
