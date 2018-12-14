from selenium import webdriver
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
    self.fail('Finish the test!')

    # able to see area to input todo
    # able to type "fix keyboard layout"
    # after commiting page updates with new todo
    # has the ability to add more todos
    # updates again after second todo
    # make data persiste across sessionsererer

if __name__ == '__main__':
  unittest.main(warnings='ignore')
