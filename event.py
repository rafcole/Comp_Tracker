from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Event:
  # eventually need two initialization flows
  # one from raw page
  # one from rehydrated json or mongo obj
  def __init__(self, parent_element):
    self.parent_element = parent_element

  # finds the first link in the main container
  # as of 5/24 this is a link in the top right corner
  def club_name(self):
    return self.parent_element.find_element(By.TAG_NAME, 'a')


  def event_status(self):
    # opens in n months/weeks/days
    # open
    # closed
    top_right_status_text = self.parent_element.find_element(By.CLASS, 'label label-important')

