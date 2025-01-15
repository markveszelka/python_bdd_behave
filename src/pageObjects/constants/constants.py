class Constants:
    BASE_URL = "https://magento.softwaretestingboard.com/"
    HOME_PAGE_URL = BASE_URL
    LOGIN_PAGE_URL = f"{BASE_URL}customer/account/login/"
    LOGIN_PAGE_URL_FRAGMENT = "customer/account/login/"

    HOME_PAGE_TEXT = "Home Page"
    LOGIN_PAGE_TEXT = "Customer Login"
    MY_ACCOUNT_PAGE_TEXT = "My Account"

    INVALID_CREDENTIALS_ERROR_MESSAGE = (
        "The account sign-in was incorrect or your account is disabled temporarily. "
        "Please wait and try again later."
    )
