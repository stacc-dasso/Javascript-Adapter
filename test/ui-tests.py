import unittest

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
        self.driver.get("http://178.62.113.8/")

    def test_typeToSearchBar(self):
        driver = self.driver
        searchText = 'blazer'
        searchFieldID = 'search'

        searchField = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(searchFieldID))

        searchField.clear()
        searchField.send_keys(searchText)
        searchField.submit()

    def test_goToAccessories(self):
        driver = self.driver
        linkName = 'ACCESSORIES'

        accessoriesTab = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_link_text(linkName))

        accessoriesTab.click()

    def test_openProduct(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        productName = 'LAFAYETTE CONVERTIBLE DRESS'

        productField = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text(productName))

        productField.click()

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

        manTab = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text('MEN'))
        manTab.click()

        shirtTab = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text('SHIRTS'))
        shirtTab.click()

        product = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text('PLAID COTTON SHIRT'))
        product.click()

        color = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('swatch17'))
        color.click()

        size = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text('S'))
        size.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
