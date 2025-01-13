from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def before_all(context):
    chrome_service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.quit()
