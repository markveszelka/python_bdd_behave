import time
from behave import *
from colorama import init, Fore, Style
from src.data.test_data import LoginTestData
from src.pageObjects.constants.constants import *

use_step_matcher("re")
init()


# region >>>WHEN<<<

@when(r'I login with "(valid|invalid|empty)" credentials')
def step_impl(context, credentials_validity):
    if credentials_validity.lower() == "valid":
        context.login_page.trigger_login(LoginTestData.VALID_EMAIL, LoginTestData.VALID_PASSWORD)
    elif credentials_validity.lower() == "invalid":
        context.login_page.trigger_login(LoginTestData.INVALID_EMAIL, LoginTestData.INVALID_PASSWORD)
    elif credentials_validity.lower() == "empty":
        time.sleep(1)  # TODO: flakiness workaround, until better solution is found. WebDriverWait is not working.
        context.login_page.click_sign_in_button()
    else:
        raise ValueError(
            f"{Fore.YELLOW}{Style.BRIGHT}Credentials '{credentials_validity}' is not implemented yet{Style.RESET_ALL}")


# region >>>THEN<<<

@then('I see the login page')
def step_impl(context):
    assert Texts.LOGIN_PAGE_TEXT in context.driver.title, "Login page title is incorrect."
    assert context.login_page.are_login_elements_visible(), "Login page elements are not visible."


@then('The URL of the login page is correct')
def step_impl(context):
    expected_url = URLs.HOME_PAGE_URL + URLs.LOGIN_PAGE_URL_FRAGMENT
    actual_url = context.driver.current_url
    assert expected_url == actual_url, f"Expected URL '{expected_url}' but found '{actual_url}'."


@then('I see the invalid credentials error message')
def step_impl(context):
    assert context.login_page.is_invalid_credentials_error_message_visible(), \
        "Invalid credentials error message is not visible."


@then('I see the login fields and button')
def step_impl(context):
    assert context.login_page.are_login_elements_visible(), "Login fields and button are not visible."


@then('I am logged in to My Account page')
def step_impl(context):
    assert Texts.MY_ACCOUNT_PAGE_TEXT == context.driver.title, "My Account page title is incorrect."
    assert context.login_page.is_logged_in(), "User is not logged in."


@then('I see Email and Password errors are displayed')
def step_impl(context):
    assert context.login_page.is_email_and_password_error_visible(), "My Account page title is incorrect."
