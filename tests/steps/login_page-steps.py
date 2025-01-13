from behave import *
from selenium.webdriver.support import expected_conditions as EC
from src.pageObjects.locators.locators import Locators

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)


@then('I should see the login page')
def step_impl(context):
    context.home_page.wait_until(EC.url_contains("customer/account/login/"))
    logging.info("Login page URL is correct.")
    assert "Customer Login" in context.driver.title

    logging.info("Checking email input presence...")
    email_input = context.home_page.wait_until(EC.presence_of_element_located(Locators.EMAIL_INPUT.value))
    assert email_input.is_displayed()

    logging.info("Checking password input presence...")
    password_input = context.home_page.wait_until(EC.presence_of_element_located(Locators.PASSWORD_INPUT.value))
    assert password_input.is_displayed()
