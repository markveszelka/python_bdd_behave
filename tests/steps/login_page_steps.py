import time
from behave import *
from colorama import init, Fore, Style
from src.pageObjects.constants.constants import Constants

use_step_matcher("re")
init()


# region >>>WHEN<<<

@when(r'I login with "(valid|invalid|empty)" credentials')
def step_impl(context, credentials_validity):
    if credentials_validity.lower() == "valid":
        _valid_email = "mveszelka@test.com"
        _valid_password = "Test1234"
        context.login_page.trigger_login(_valid_email, _valid_password)
    elif credentials_validity.lower() == "invalid":
        _invalid_email = "test@test.com"
        _invalid_password = "test"
        context.login_page.trigger_login(_invalid_email, _invalid_password)
    elif credentials_validity.lower() == "empty":
        time.sleep(
            1)  # TODO: wait for the page to be loaded, WebDriver wait for clickable element is not working, update it!
        context.login_page.click_sign_in_button()
    else:
        raise ValueError(
            f"{Fore.YELLOW}{Style.BRIGHT}Credentials '{credentials_validity}' is not implemented yet{Style.RESET_ALL}")


# region >>>THEN<<<

@then('I see the login page')
def step_impl(context):
    assert Constants.LOGIN_PAGE_TEXT.value in context.driver.title
    assert context.login_page.are_login_elements_visible()


@then('The URL of the login page is correct')
def step_impl(context):
    expected_url = Constants.HOME_PAGE_URL.value + Constants.LOGIN_PAGE_URL_FRAGMENT.value
    actual_url = context.driver.current_url
    assert expected_url == actual_url


@then('I see the invalid credentials error message')
def step_impl(context):
    assert context.login_page.is_invalid_credentials_error_message_visible()


@step('I see the login fields and button')
def step_impl(context):
    assert context.login_page.are_login_elements_visible()


@then('I am logged in to My Account page')
def step_impl(context):
    assert Constants.MY_ACCOUNT_PAGE_TEXT.value == context.driver.title
    assert context.login_page.is_logged_in()


@then('I see Email and Password errors are displayed')
def step_impl(context):
    assert context.login_page.is_email_and_password_error_visible()
