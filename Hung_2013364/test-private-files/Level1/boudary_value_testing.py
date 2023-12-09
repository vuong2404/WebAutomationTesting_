# Generated by Selenium IDE
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from file_generator import create_file

class TestAddEntry(unittest.TestCase):
  def setup(self):
    self.current_dir = os.path.dirname(os.path.abspath(__file__))
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}   
    self.driver.maximize_window()
    self.driver.get("https://school.moodledemo.net/enrol/index.php?id=57")
    self.driver.find_element(By.ID, "username").send_keys("student") 
    self.driver.find_element(By.ID, "password").send_keys("moodle")
    self.driver.find_element(By.ID, "loginbtn").click()
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, ".avatar").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Private files").click()
    time.sleep(15)
  def teardown(self):
    self.driver.quit()
    
  def testcase1(self):
    self.upload_file("MIN.txt")

  def testcase2(self):
    self.upload_file("MIN-.txt")

  def testcase3(self):
    self.upload_file("NOM.txt")

  def testcase4(self):
    self.upload_file("MAX+.txt")

  def testcase5(self):
    self.upload_file("MAX.txt")
    
  def upload_file(self, file_name):
    self.setup()
    if len(self.driver.find_elements(By.XPATH, "//div[2]/a/div/div[3]"))>0:
      self.driver.find_element(By.XPATH, "//div[2]/a/div/div[3]").click()
      time.sleep(5)
      self.driver.find_element(By.XPATH, "//form/div/button[2]").click()
      time.sleep(5)
      self.driver.find_element(By.XPATH, "//button[contains(.,\'Yes\')]").click()
      time.sleep(5)
      self.driver.find_element(By.XPATH, "//span/input").click()
      time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".fa-file-o").click()
    time.sleep(15)
    file_path = os.path.join(self.current_dir, 'files', file_name)
    self.driver.find_element(By.XPATH, "//form/div/div/div/input").send_keys(file_path)
    time.sleep(5)
    
    upload_button = WebDriverWait(self.driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]"))
    )
    self.driver.execute_script("arguments[0].click();", upload_button)
    if file_name == 'MIN.txt' or file_name == 'MIN-.txt':
        time.sleep(5)
    else:
        time.sleep(100)
    self.driver.find_element(By.XPATH, "//span/input").click()
    print(f"Testcase for {file_name} passed\n")
    self.teardown()

if __name__ == "__main__":
    create_file('MIN.txt', 1, 'files')
    create_file('MIN-.txt', 2, 'files')
    create_file('NOM.txt', 52428800 , 'files')
    create_file('MAX+.txt', 104796159, 'files')
    create_file('MAX.txt', 104796160, 'files')
    unittest.main()
  
