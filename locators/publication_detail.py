from selenium.webdriver.common.by import By


class PublicationDetailLocators:
    TITLE = "//span[@id='title'][contains(text(), '{}')]"
    PUB_TYPE = "//span[@id='pub_type'][contains(text(), '{}')]"
    PET_NAME = "//p[@id='pet_name'][contains(text(), '{}')]"
    PET_RACE = "//p[@id='pet_race'][contains(text(), '{}')]"
    AUTHOR_NAME = "//p[@id='author_name'][contains(text(), '{}')]"
    PHONE_NUMBER = "//p[@id='phone_number'][contains(text(), '{}')]"
    MARKER = (
        By.CSS_SELECTOR,
        "img[src='https://maps.gstatic.com/mapfiles/transparent.png']",
    )
    DELETE_BTN = (
        By.XPATH,
        "//button[contains(text(), 'Finalizar publicación')]",
    )
