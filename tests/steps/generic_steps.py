from behave import *
from colorama import init

use_step_matcher('re')
init()


# region >>>GIVEN<<<

@given(r'I am on the "(.+)" page')
def step_impl(context, page):
    context.base_page.load_given_page(page)


# region >>>THEN<<<

@then(r'I see the "(.+)" header')
def step_impl(context, header):
    header_locator = context.home_page.HEADER_LOCATOR(header)
    header_element = context.driver.find_element(*header_locator)
    assert header_element.is_displayed(), f'Header "{header}" is not displayed'
