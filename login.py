import sys
import time
import re
import random
import logging
import os
# logging.basicConfig(level=10)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from selenium_stealth import stealth


from selenium.common.exceptions import NoSuchElementException

from dotenv import load_dotenv
load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TARGET_SITE = os.getenv("TARGET_SITE")

import undetected_chromedriver as uc
driver = uc.Chrome()
driver._web_element_cls = uc.UCWebElement


driver.get(f"https://{TARGET_SITE}/ewpsa-2024-10-action-2-gun/register")

# allow redirect
time.sleep(10)


driver.find_element(By.NAME, "username").send_keys(USERNAME)

time.sleep(7)

driver.find_element(By.NAME, "password").send_keys(PASSWORD)

time.sleep(2.1654)

button = driver.find_element(By.CLASS_NAME, "btn.btn-md.btn-primary.btn-block.top3").click()

time.sleep(300)



