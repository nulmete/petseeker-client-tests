from locators.publications import PublicationsPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from pages.page import BasePage


class PublicationsPage(BasePage):
    def get_add_button(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *PublicationsPageLocators.BTN_ADD
            )
        )

    def get_publications(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(
                *PublicationsPageLocators.PUBLICATION
            )
        )

    def click_add_button(self):
        self.click_element(self.get_add_button())
