from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory import PageFactory


class BasePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def click(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.send_keys(text)

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_until(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition)

    def wait_for_element_visible(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))
