import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def click_button_by_xpath(driver, xpath):
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    button.click()
