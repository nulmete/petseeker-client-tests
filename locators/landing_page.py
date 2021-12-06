from selenium.webdriver.common.by import By


class LandingPageLocators:
    LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Log In')]")
    SIGNUP_BTN = (By.XPATH, "//button[contains(text(), 'Sign Up')]")
    AUTH0_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    AUTH0_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    AUTH0_SUBMIT_BTN = (
        By.XPATH,
        "//button[contains(text(), 'Continue')]",
    )
