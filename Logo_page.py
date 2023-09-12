import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def logo_page(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'custom-logo'))).click()
