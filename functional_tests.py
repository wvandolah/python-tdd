from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # get home page
    self.browser.get('http://localhost:8000')
    # check that titles says todo list
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').header_text
    self.assertIn('To-Do', header_text)

    # able to see area to input todo
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
    # able to type "fix keyboard layout"
    inputbox.send_keys('fix keyboard layout')
    # after commiting page updates with new todo
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(any(row.text == '1: fix keyboard layout' for row in rows))
    # has the ability to add more todos
    # updates again after second todo
    # make data persiste across sessionsererer
    self.fail("Finish the test!")

if __name__ == '__main__':
  unittest.main(warnings='ignore')
