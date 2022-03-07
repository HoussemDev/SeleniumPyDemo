from selenium import webdriver
import time
import unittest
from POMProjectDemo.Pages.loginPage import LoginPage
from POMProjectDemo.Pages.HomePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/home/houssem/PycharmProjects/Selenium/POMProjectDemo/drivers"
                                                      "/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        homepage = HomePage(driver)

        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")
