import os
import unittest
import urllib.request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class LoginTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=options)
        self.driver.get("http://178.62.113.8/")
        self.logsURL = "http://104.248.248.147/log.txt"

    def test_typeToSearchBar(self):
        driver = self.driver
        searchText = 'blazer'
        searchFieldID = 'search'

        searchField = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(searchFieldID))

        searchField.clear()
        searchField.send_keys(searchText)
        searchField.submit()

        with urllib.request.urlopen(self.logsURL) as url:
            logs = url.read().decode('utf-8')
        assert '"event_type": "search"' in logs

    def test_goToAccessories(self):
        driver = self.driver
        linkName = 'ACCESSORIES'

        accessoriesTab = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_link_text(linkName))

        accessoriesTab.click()

        with urllib.request.urlopen(self.logsURL) as url:
            logs = url.read().decode('utf-8')
        assert '"runid": "test_run"' in logs

    def test_openProduct(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        productName = 'LAFAYETTE CONVERTIBLE DRESS'

        productField = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text(productName))

        productField.click()

        with urllib.request.urlopen(self.logsURL) as url:
            logs = url.read().decode('utf-8')
        assert '"event_type": "view_item"' in logs
        assert '"item_id": "425"' in logs

    def test_logIn_addProductToCart(self):
        driver = self.driver
        email = 'test@test.com'
        password = 'testtest'

        accountField = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text('ACCOUNT'))
        accountField.click()

        logInField = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text('Log In'))
        logInField.click()

        emailField = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('email'))
        emailField.send_keys(email)

        passwordField = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('pass'))
        passwordField.send_keys(password)

        logInButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('send2'))
        logInButton.click()

        with urllib.request.urlopen(self.logsURL) as url:
            logs = url.read().decode('utf-8')
        assert '"event_type": "add_to_cart"' in logs
        assert '"item_id": "421"' in logs
        assert '"item_id": "408"' in logs

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
