from behave import when, then, use_step_matcher
from selenium.webdriver.common.by import By
from src.pageObjects.constants.constants import Constants

use_step_matcher('re')


# region >>>WHEN<<<

@when(r'I click the "(.+)" button')
def step_impl(context, button_text):
    context.home_page.click_element(By.LINK_TEXT, button_text)


# region >>>THEN<<<

@then('I see the "Home Page" title')
def step_impl(context):
    assert Constants.HOME_PAGE_TEXT.value in context.home_page.driver.title


@then(r'the page with "(.+)" is opened')
def step_impl(context, url):
    expected_url = Constants.HOME_PAGE_URL.value + url
    assert context.home_page.driver.current_url == expected_url


@then('I see the essential home page elements')
def step_impl(context):
    assert context.home_page.are_home_elements_visible()
