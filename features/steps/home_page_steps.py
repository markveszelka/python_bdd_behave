from behave import *
from src.pages.home_page import HomePage

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)


@given('I am on the home page')
def step_impl(context):
    logging.info("Navigating to home page.")
    context.home_page = HomePage(context.driver)
    context.home_page.driver.get("https://magento.softwaretestingboard.com")
    assert "Home Page" in context.home_page.driver.title


@when('I click the login button')
def step_impl(context):
    context.home_page.click_login_button()
