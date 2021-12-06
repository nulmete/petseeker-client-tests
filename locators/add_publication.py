from selenium.webdriver.common.by import By


class AddPublicationLocators:
    TITLE_INPUT = (By.CSS_SELECTOR, "input[id='title']")
    PET_NAME_INPUT = (By.CSS_SELECTOR, "input[id='pet_name']")
    PET_RACE_INPUT = (By.CSS_SELECTOR, "input[id='pet_race']")
    MAP = (By.CSS_SELECTOR, ".gm-style")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[id='description']")
    IMG_INPUT = (By.CSS_SELECTOR, "input[id='images']")
    SUBMIT_BTN = (By.XPATH, "//button[contains(text(), 'Crear')]")
