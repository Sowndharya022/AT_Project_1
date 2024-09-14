#pages/pim_page.py
from datetime import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class PIMPage(BasePage):
    PIM_MENU = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
    ADD_BUTTON = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@name='firstName']")
    MIDDLE_NAME_INPUT = (By.XPATH, "//input[@name='middleName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@name='lastName']")

    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    EDIT_BUTTON = (
        By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]")
    DELETE_BUTTON = (
        By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]")

    nationality_option = (By.XPATH,
                          "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]")
    NATIONALITY_DROPDOWN = (By.XPATH,
                            "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i")
    MARITAL_STATUS_DROPDOWN = (By.XPATH,
                               "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i")

    marital_status_single = (By.XPATH,
                             "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]")
    DOB_INPUT = (By.XPATH,
                 "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/i")

    dob_year_input_button = (By.XPATH,
                             "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i")
    dob_year = (By.XPATH,
                "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[31]")

    dob_month_input_button = (By.XPATH,
                              "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i")

    dob_month = (By.XPATH,
                 "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[1]")

    dob_date = (By.XPATH,
                "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[3]/div[22]/div")

    GENDER_RADIO_FEMALE = (By.XPATH,
                           "//form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span")

    employee_list = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]")
    yes_delete = (By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]")

    def go_to_pim(self):
        self.click_element(self.PIM_MENU)

    def add_employee(self, first_name, middle_name, last_name):
        self.click_element(self.ADD_BUTTON)
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.MIDDLE_NAME_INPUT, middle_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.click_element(self.SAVE_BUTTON)

    def add_personal_details(self):
        self.click_element(self.NATIONALITY_DROPDOWN)
        self.click_element(self.nationality_option)

        self.click_element(self.MARITAL_STATUS_DROPDOWN)
        self.click_element(self.marital_status_single)

        self.click_element(self.DOB_INPUT)
        self.click_element(self.dob_year_input_button)
        self.click_element(self.dob_year)
        self.click_element(self.dob_month_input_button)
        self.click_element(self.dob_month)
        self.click_element(self.dob_date)

        self.click_element(self.GENDER_RADIO_FEMALE)
        self.click_element(self.SAVE_BUTTON)

    def click_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            print(f"Timeout while waiting for element {locator} to be clickable.")
            self.driver.save_screenshot('screenshot.png')
        except Exception as e:
            print(f"An error occurred: {e}")
            self.driver.save_screenshot('screenshot.png')

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 2).until(EC.visibility_of(element))

    def js_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def edit_employee(self, first_name, middle_name, last_name):
        self.scroll_to_element(self.EDIT_BUTTON)
        try:
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(self.EDIT_BUTTON)
            )
            self.js_click(self.EDIT_BUTTON)
            self.enter_text(self.FIRST_NAME_INPUT, first_name)
            self.enter_text(self.MIDDLE_NAME_INPUT, middle_name)
            self.enter_text(self.LAST_NAME_INPUT, last_name)
            self.js_click(self.SAVE_BUTTON)
        except Exception as e:
            print(f"An error occurred during editing: {e}")
            self.driver.save_screenshot('edit_employee_error.png')

    def delete_employee(self):
        self.scroll_to_element(self.DELETE_BUTTON)
        try:
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(self.DELETE_BUTTON)
            )
            self.js_click(self.DELETE_BUTTON)
            self.js_click(self.yes_delete)

        except Exception as e:
            print(f"An error occurred during deletion: {e}")
            self.driver.save_screenshot('delete_employee_error.png')
