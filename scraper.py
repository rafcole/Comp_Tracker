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
  USERNAME = os.getenv("USERNAME")
  PASSWORD = os.getenv("PASSWORD")
  TARGET_SITE = os.getenv("TARGET_SITE")

  def __init__(self):
    self.driver = self.setup_driver()

    self.logged_in = False

  # feels hardcoded but we don't have any other use cases to accomodate right now
  def setup_driver(self):
    driver = Driver(uc=True)
    # driver._web_element_cls = uc.UCWebElement

    return driver

  def log_in(self):
    try:
      self.driver.uc_open(f"https://{Scraper.TARGET_SITE}/login")
    except Exception as e:
      print("Could not find login page:", e)

    try:
      # TODO - eliminate sleep calls
      time.sleep(5)
      self.driver.find_element(By.NAME, "username").send_keys(Scraper.USERNAME)
      time.sleep(2)
      self.driver.find_element(By.NAME, "password").send_keys(Scraper.PASSWORD)
      time.sleep(2.1654)
    except Exception as e:
      print("Could not send text to username and password fields: ", e)

    try:
      # click login
      self.driver.uc_click('button.btn.btn-md.btn-primary.btn-block.top3[type="submit"]')

      # check for success
      self.driver.assert_text("Welcome back!", "#psMainContainer > div.col-xs-12 > div")
      self.driver.assert_element_present('/html/body/div[2]/div[3]/div/div[2]/ul[2]/li[1]/ul/li[8]/a')
      self.logged_in = True

      print("Login successful")
    except Exception as e:
      print(f"Log in failed : ", e)

    return self.logged_in

  def get_event_details(self, event_str):
    if not self.logged_in:
        self.log_in()

    self.driver.uc_open(f'http://{Scraper.TARGET_SITE}/{event_str}/register')

    ps_main_container = self.driver.find_element(By.ID, "psMainContainer")

    club_link = ps_main_container.find_element(By.TAG_NAME, 'a')

    return Scraper.extract_nested_text(ps_main_container)

  def extract_nested_text(target_element):
    print(target_element.text)
    print("Target element :", target_element)
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