import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from actions import click_button_by_xpath


def privacy_policy(driver):
    click_button_by_xpath(driver, '//*[@id="block-8"]/ul/li[3]/a' )


