"""
TEST MAIN
"""
from Data import Data
from Locators import Locators



import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOrangeHRM():

    #Fixtures are defined using the @pytest.fixture decorator in Python.
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(Data.webdata().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    @pytest.mark.html
    def test_forgot_password_link_validation(self,boot):
        try:
            # Click the forgot password button and reset the password
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().forgotpasswordLocator).click()
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().usernameLocator).send_keys(
                Data.webdata().username)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().resetpasswordLocator).click()
            # Wait for the reset password success message or error message to be displayed
            if self.driver.find_element(by=By.XPATH,
                                        value=Locators.WebLocators().resetconformationlocator).is_displayed():
                print("Reset Password link sent successfully")

            else:
                print("Unable to reset the password")
        except NoSuchElementException as e:
            print("Element not found.")


    @pytest.mark.html
    def test_admin_page_header_validation(self,boot):
        try:
            #login to the OrangeHMR page
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().usernameLocator).send_keys(
                Data.webdata().username)
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().passwordLocator).send_keys(
                Data.webdata().password)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().buttonLocator).click()

           # Wait for the Admin page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(@href,'viewAdminModule')]"))
            ).click()
            # To find the title of the Webpage
            expected_title = "OrangeHRM"
            actual_title = self.driver.title
            if actual_title == expected_title:
                print("Title of the page is OrangeHRM")
            else:
                print("Unable to get the title")

            #Validate the below options are visible in the webpage
            admin_options = ["User Management", "Job", "Organization", "Qualifications",
                             "Nationalities", "Corporate Branding", "Configuration"]
            admin_options_obj = self.driver.find_elements(
                By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab-item")
            for option in admin_options_obj:
                option_value = option.text
                if option_value in admin_options:
                    print(option_value, " is present.")
                else:
                    print(option_value, " is not present.")

        except NoSuchElementException:
            print("Element not found.")
        except TimeoutException:
            print("Timeout occurred.")



    @pytest.mark.html
    def test_main_menu_validation(self,boot):
        try:
            # login to the Webpage
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().usernameLocator).send_keys(
                Data.webdata().username)
            self.driver.find_element(by=By.NAME, value=Locators.WebLocators().passwordLocator).send_keys(
                Data.webdata().password)
            self.driver.find_element(by=By.XPATH, value=Locators.WebLocators().buttonLocator).click()
            # Wait for the Admin page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(@href,'viewAdminModule')]"))
            )

            # Go to the Admin Page
            self.driver.find_element(
                By.XPATH, "//a[contains(@href,'viewAdminModule')]").click()

            # Wait for the admin menu options to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, ".oxd-text.oxd-text--span.oxd-main-menu-item--name"))
            )

            admin_menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info",
                                  "Performance", "Dashboard", "Directory", "Maintenance", "Claim", "Buzz"]
            admin_menu_options_obj = self.driver.find_elements(
                By.CSS_SELECTOR, ".oxd-text.oxd-text--span.oxd-main-menu-item--name")
            for option in admin_menu_options_obj:
                option_value = option.text
                if option_value in admin_menu_options:
                    print(option_value, " is present.")

                else:
                    print(option_value, " is not present.")
        except NoSuchElementException:
            print("Element not found.")
        except TimeoutException:
            print("Timeout occurred.")
