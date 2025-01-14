from behave import fixture, use_fixture

from src.lib.drivers.chrome_driver_provider import ChromeDriver
from src.lib.helpers.allure_screen_shot_helper import ScreenshotHelper
from src.pageObjects.pages.base_page import BasePage
from src.pageObjects.pages.home_page import HomePage
from src.pageObjects.pages.login_page import LoginPage


@fixture
def browser_chrome(context):
    context.driver = ChromeDriver().get_driver()
    yield context.driver
    context.driver.quit()


def before_scenario(context, scenario):
    use_fixture(browser_chrome, context)

    context.base_page = BasePage(context.driver)
    context.home_page = HomePage(context.driver)
    context.login_page = LoginPage(context.driver)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        ScreenshotHelper.take_screenshot(context.driver, scenario.name)

    if context.driver:
        context.driver.quit()
