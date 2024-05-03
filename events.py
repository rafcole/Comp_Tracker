import sys
import time
import re
import random
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from seleniumbase import Driver


from selenium_stealth import stealth

# import undetected_chromedriver as uc
from dotenv import load_dotenv
load_dotenv()

TARGET_SITE = os.getenv("TARGET_SITE")
print(f"====> TargetSite : {TARGET_SITE}")



arguments = sys.argv

if len(arguments) < 1:
   raise ValueError("No club name provided")

club_name = arguments[1]

# service = Service(executable_path="./chromedriver")
driver = Driver(uc=True)
# driver._web_element_cls = uc.UCWebElement

driver.get(f"https://{TARGET_SITE}/clubs/{club_name}/matches?filter=upcoming")


driver.sleep(10)



def find_match_table():
  try:
    return driver.find_element(By.CLASS_NAME, "table.table-striped")

  except NoSuchElementException:
    print("Could Not Find Results Table")

def get_table_rows(table):
  try:
     return table.find_elements(By.TAG_NAME, "tr")
  except NoSuchElementException:
     print("Empty Table")

def extract_event_URL_from_row(row):
   try:
      link = row.find_element(By.TAG_NAME, 'a')

      return link.get_attribute('href')
   except NoSuchElementException:
      print("No Link found in this row")

def extract_event_name(event_url):
   return re.search(r'(?<=\.com\/)(.*?)(?=\/register)', url).group(0)


match_table = find_match_table()
rows = get_table_rows(match_table)
match_urls = []
event_names = []

for row in rows:
   url = extract_event_URL_from_row(row)
   last_event = url
   event_name = extract_event_name(url)

   event_names.append(event_name)
   match_urls.append(url)

print(event_names)
driver.sleep(7)

try:
   # random_row_link = random.choice(rows).find_element(By.TAG_NAME, 'a')


   driver.get(random.choice(match_urls))

   # scroll_origin = ScrollOrigin.from_element(random_row_link)

   # ActionChains(driver)\
   #    .scroll_from_origin(scroll_origin, 0, 200)\
   #    .perform()

   # driver.sleep(1)
   # random_row_link.click()
except Exception as error:
   print("Failed click: ", error)

driver.sleep(200)


