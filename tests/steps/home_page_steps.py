from behave import *
from src.pageObjects.constants.constants import Constants

use_step_matcher('re')


# region >>>WHEN<<<

@when(r'I click the "(.+)" button')
def step_impl(context, button_text):
    context.home_page.click_element_by_text(button_text)


# region >>>THEN<<<

@then('I see the "Home Page" title')
def step_impl(context):
    assert Constants.HOME_PAGE_TEXT in context.home_page.driver.title, \
        f"Expected title '{Constants.HOME_PAGE_TEXT}' not found in page title."


@then(r'the page with "(.+)" is opened')
def step_impl(context, url):
    expected_url = Constants.HOME_PAGE_URL + url
    assert context.home_page.driver.current_url == expected_url, \
        f"Expected URL '{expected_url}' but found '{context.home_page.driver.current_url}'."


@then('I see the essential home page elements')
def step_impl(context):
    assert context.home_page.are_home_elements_visible(), "Essential home page elements are not visible."
