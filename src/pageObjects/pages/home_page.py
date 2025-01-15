from selenium.webdriver.common.by import By
from src.pageObjects.pages.base_page import BasePage


class HomePage(BasePage):
    NAVIGATION_MENU_LOCATOR = (By.ID, 'ui-id-2')
    PROMO_IMAGE_LOCATOR = (By.CLASS_NAME, 'blocks-promo')
    HOME_PAGE_TITLE_LOCATOR = (By.CLASS_NAME, 'base')
    HEADER_LOCATOR = lambda self, header_text: (By.XPATH, f'//span[@class="base" and text()="{header_text}"]')

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def are_home_elements_visible(self) -> bool:
        return all([
            self.is_element_visible(self.NAVIGATION_MENU_LOCATOR),
            self.is_element_visible(self.PROMO_IMAGE_LOCATOR),
            self.is_element_visible(self.HOME_PAGE_TITLE_LOCATOR)
        ])
