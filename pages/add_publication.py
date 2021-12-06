import os
from locators.add_publication import AddPublicationLocators
from selenium.webdriver.support.wait import WebDriverWait
from pages.page import BasePage


class AddPublicationPage(BasePage):
    def get_title(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *AddPublicationLocators.TITLE_INPUT
            )
        )

    def get_pet_name(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *AddPublicationLocators.PET_NAME_INPUT
            )
        )

    def get_pet_race(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *AddPublicationLocators.PET_RACE_INPUT
            )
        )

    def get_map(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*AddPublicationLocators.MAP)
        )

    def get_description(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *AddPublicationLocators.DESCRIPTION_INPUT
            )
        )

    def get_image_input(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *AddPublicationLocators.IMG_INPUT
            )
        )

    def get_submit(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(
                *AddPublicationLocators.SUBMIT_BTN
            )
        )

    def fill_inputs_valid(self):
        self.set_input_text("Titulo", self.get_title())
        self.set_input_text("Nombre", self.get_pet_name())
        self.set_input_text("Raza", self.get_pet_race())
        self.click_element(self.get_map())
        self.set_input_text("Notas adicionales", self.get_description())
        self.get_image_input().send_keys(os.getcwd() + "/Python.png")
        self.click_element(self.get_submit())
