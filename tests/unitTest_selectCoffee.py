import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        user = "instructor"
        pwd = "mavericks"

        # Login
        driver.get("http://127.0.0.1:8000/")
        driver.find_element(By.LINK_TEXT, "Login").click()
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        # Wait for login to complete (assuming it takes 5 seconds)
        time.sleep(5)

        driver.find_element(By.LINK_TEXT, "Coffees").click()
        time.sleep(5)

        driver.find_element(By.LINK_TEXT, "Back to HomePage").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
