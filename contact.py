import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def contact_us_message_valid(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'menu-item-25'))).click()
    driver.find_element(By.NAME, 'fcb44c85').send_keys('vlad')
    driver.find_element(By.NAME, '0112ce16').send_keys('blad')
    driver.find_element(By.NAME, '012af4e3').send_keys('bladvlad@gmail.com')
    driver.find_element(By.NAME, 'fd8a921a').send_keys('stop touch me please')
    driver.find_element(By.CLASS_NAME, 'uagb-forms-main-submit-button.wp-block-button__link').click()

