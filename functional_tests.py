from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text, [row.text for row in rows])

  def test_can_start_a_list_and_retrieve_it_later(self):
    # get home page
    self.browser.get('http://localhost:8000')
    # check that titles says todo list
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # able to see area to input todo
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
    # able to type "fix keyboard layout"
    inputbox.send_keys('fix keyboard layout')
    # after commiting page updates with new todo
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)
    self.check_for_row_in_list_table('1: fix keyboard layout')

    # has the ability to add more todos
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('fix keyboard layout again')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    # updates again after second todo
    self.check_for_row_in_list_table('1: fix keyboard layout')
    self.check_for_row_in_list_table('2: fix keyboard layout again')

    # make data persiste across sessionsererer
    self.fail("Finish the test!")

if __name__ == '__main__':
  unittest.main(warnings='ignore')
