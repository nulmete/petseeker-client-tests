from locators.landing_page import LandingPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from pages.page import BasePage


class LandingPage(BasePage):
    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*LandingPageLocators.LOGIN_BTN)
        )

    def get_signup_button(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*LandingPageLocators.SIGNUP_BTN)
        )

    def get_auth0_email_input(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *LandingPageLocators.AUTH0_EMAIL_INPUT
            )
        )

    def get_auth0_password_input(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *LandingPageLocators.AUTH0_PASSWORD_INPUT
            )
        )

    def get_auth0_submit_button(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *LandingPageLocators.AUTH0_SUBMIT_BTN
            )
        )

    def login(self):
        self.click_element(self.get_login_button())
        self.set_input_text(
            "nicoulmete1@gmail.com", self.get_auth0_email_input()
        )
        self.set_input_text("Arenaza2135!", self.get_auth0_password_input())
        self.click_element(self.get_auth0_submit_button())
