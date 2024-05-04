import time
import os

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from seleniumbase import Driver

import undetected_chromedriver as uc

from dotenv import load_dotenv

class Scraper:
  print('Scraper class running')
  load_dotenv()

  def __init__(self):
    self.driver = self.setup_driver()

    self.logged_in = False

  # feels hardcoded but we don't have any other use cases to accomodate right now
  def setup_driver(self):
    driver = Driver(uc=True)
    # driver._web_element_cls = uc.UCWebElement

    return driver

  def log_in(self):
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    TARGET_SITE = os.getenv("TARGET_SITE")

    self.driver.uc_open(f"https://{TARGET_SITE}/login")

    # TODO - eliminate sleep calls
    time.sleep(5)

    self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
    time.sleep(2)
    self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    time.sleep(2.1654)
    # button = self.driver.find_element(By.CLASS_NAME, "btn.btn-md.btn-primary.btn-block.top3").click()
    self.driver.uc_click('button.btn.btn-md.btn-primary.btn-block.top3[type="submit"]')

    # TODO - check for success
    self.logged_in = True

    time.sleep(60)
    pass

  def get_event_details(self, event_str):
    if not self.logged_in:
        self.log_in()

    ps_main_container = self.driver.find_element(By.ID, "psMainContainer")

    club_link = ps_main_container.find_element(By.TAG_NAME, 'a')

    return Scraper.extract_nested_text(ps_main_container)

  def extract_nested_text(target_element):
    # Find all descendant elements containing text
    text_elements = target_element.find_elements(By.XPATH, ".//*/text()")

    # Extract the text values
    text_values = [element.strip() for element in text_elements if element.strip()]

    return text_values




def find_match_table(driver):
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

def get_events_from_club(club_name_str, driver):

  TARGET_SITE = os.getenv("TARGET_SITE")
  driver.get(f"https://{TARGET_SITE}/clubs/{club_name_str}/matches?filter=upcoming")

  TARGET_SITE = os.getenv("TARGET_SITE")
  print(f"====> TargetSite : {TARGET_SITE}")

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

  return event_names
  driver.sleep(7)