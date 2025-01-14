from behave import given, then, use_step_matcher
from colorama import init
from selenium.webdriver.common.by import By

use_step_matcher('re')
init()


# region >>>GIVEN<<<

@given(r'I am on the "(.+)" page')
def step_impl(context, page):
    context.base_page.load_given_page(page)


# TODO: refactor locators to constants, maybe class attributes?
@then(r'I see the "(.+)" header')
def step_impl(context, header):
    header_element = context.driver.find_element(By.XPATH, f'//span[@class="base" and text()="{header}"]')
    assert header_element.is_displayed()
