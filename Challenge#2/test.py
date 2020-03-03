from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest


class Test(unittest.TestCase):
  def test_1(self):
    try:
      driver = webdriver.Chrome('./chromedriver80')
      # Get the test website
      driver.get("https://www.gobear.com/ph?x_session_type=UAT")

      driver.implicitly_wait(15)
      # Go to the travel card
      insuranceTab = driver.find_element_by_xpath('//a[contains(@href, "#Insurance")]')
      travelTab = driver.find_element_by_xpath('//a[contains(@href, "#Travel")]')

      insuranceTab.click()
      travelTab.click()

      # submitBtn = driver.find_element_by_name('product-form-submit');
      wait = WebDriverWait(driver, 30)
      submitBtn = wait.until(EC.element_to_be_clickable((By.NAME, 'product-form-submit')))
      submitBtn.click()
      resultList = driver.find_elements_by_class_name('card-full')

      # Check number of result
      self.assertTrue(len(resultList) >= 3,"Less than 3")
      rem = len(resultList)

      #Check filter 
      driver.find_element_by_xpath('//div[contains(@data-gb-name, "filter-bar")]').click()
      driver.find_element_by_xpath('//div[contains(@data-filter-name, "Promos Only")]').click()
      check = rem == len(resultList)
      self.assertTrue(check,"Filters not working")
      rem = len(resultList)

      driver.find_element_by_xpath('//div[contains(@data-gb-name, "sort-bar")]').click()
      driver.find_element_by_xpath('//div[contains(@data-sort-by, "premium")]').click()
      check = rem == len(resultList)
      self.assertTrue(check ,"Sorts not working")
      rem = len(resultList)
      
      driver.find_element_by_xpath('//div[contains(@data-gb-name, "edit-detail-bar")]').click()
      driver.find_element_by_xpath('//div[contains(@data-gb-trip-types, "annual")]').click()
      check = rem == len(resultList)
      self.assertTrue(check,"Details not working")
    finally:
      # Close the test website
      driver.close()



if __name__ == "__main__":
	unittest.main()