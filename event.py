from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json

import re

class Event:
  # eventually need two initialization flows
  # one from raw page
  # one from rehydrated json or mongo obj
  def __init__(self, parent_element):
    self.parent_element = parent_element

  # finds the first link in the main container
  # as of 5/24 this is a link in the top right corner
  def club_name(self):
    club_url = self.parent_element.find_element(By.TAG_NAME, 'a').get_attribute('href')

    return re.search(r'\.com/clubs/(.*)', club_url).group(1)


  def status(self):
    # opens in n months/weeks/days
    # open
    # closed
    return self.parent_element.find_element(By.XPATH, '//*[contains(@class, "label-success") or contains(@class, "label-important")]').text

  def json(self):
    obj = {
      'club_name': self.club_name(),
      'start_time': 'empty',
      'status': self.status(),
      'registration_time': 'empty',
      'description': 'empty'
    }

    return json.dumps(obj)



