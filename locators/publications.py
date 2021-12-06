from selenium.webdriver.common.by import By


class PublicationsPageLocators:
    BTN_ADD = (By.XPATH, "//button[contains(text(), 'Agregar')]")
    PUBLICATION = (By.ID, "publication")
