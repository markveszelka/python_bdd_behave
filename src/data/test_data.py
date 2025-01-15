import random
import string


class LoginTestData:
    VALID_EMAIL = "mveszelka@test.com"
    VALID_PASSWORD = "Test1234"

    INVALID_EMAIL = ''.join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"
    INVALID_PASSWORD = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
