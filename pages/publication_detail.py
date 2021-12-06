from locators.publication_detail import PublicationDetailLocators
from selenium.webdriver.support.wait import WebDriverWait
from pages.page import BasePage


class PublicationDetailPage(BasePage):
    def get_title(self, text):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(
                PublicationDetailLocators.TITLE.format(str(text))
            )
        )

    def get_pub_type(self, text):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(
                PublicationDetailLocators.PUB_TYPE.format(str(text))
            )
        )

    def get_pet_name(self, text):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(
                PublicationDetailLocators.PET_NAME.format(str(text))
            )
        )

    def get_pet_race(self, text):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_xpath(
                PublicationDetailLocators.PET_RACE.format(str(text))
            )
        )

    def get_markers(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(
                *PublicationDetailLocators.MARKER
            )
        )

    def get_delete_btn(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *PublicationDetailLocators.DELETE_BTN
            )
        )

    def delete_publication(self):
        self.click_element(self.get_delete_btn())
        self.click_element(self.get_confirm_modal_btn())
