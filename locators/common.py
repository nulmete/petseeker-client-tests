from selenium.webdriver.common.by import By


class CommonLocators:
    SNACKBAR = "//div[@id='notistack-snackbar'][contains(text(), '{}')]"
    CONFIRM_MODAL = (
        By.XPATH,
        "//button[@id='confirm'][contains(text(), 'Confirmar')]",
    )
    DISMISS_MODAL = (
        By.XPATH,
        "//button[@id='dismiss'][contains(text(), 'Cancelar')]",
    )
