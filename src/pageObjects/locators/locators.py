from selenium.webdriver.common.by import By
from enum import Enum

class Locators(Enum):
    SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign In")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "pass")

