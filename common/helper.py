from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

import time
import namegenerator

delay_to_load_page = 10
username = 'Admin'
password = 'admin123'
name = namegenerator.gen()


class TestGrades:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

    def login(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//input[@name="username"]'))).send_keys(username)
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def add(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[text()="Admin"]'))).click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[contains(text(),"Job")]'))).click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Pay Grades")]').click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Add")]'))).click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//input[@placeholder]'))).send_keys(name)
        self.driver.find_element(By.XPATH, "//button[@type='Save']").click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[contains(text(),"--Select--")]'))).click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"UAH - Ukraine Hryvnia")]').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder]').send_keys(1000)
        self.driver.find_element(By.XPATH, '//input[@placeholder]').send_keys(10000)
        self.driver.find_element(By.XPATH, "//button[@type='Save']").click()

    def check_row(self):
        xpath_found_row = '//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "Ukraine Hryvnia")]'
        found_row = WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, xpath_found_row)))

        found_row.find_element(By.XPATH, '//div[contains(., "Ukraine Hryvnia")]')
        found_row.find_element(By.XPATH, '//div[contains(., "1000")]')
        found_row.find_element(By.XPATH, '//div[contains(., "10000")]')

    def remove_and_check(self):
        xpath_delete = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{name}"' \
                       ', "Ukraine Hryvnia")]//i[@class="oxd-icon bi-trash"]'
        found_row = self.driver.find_element(By.XPATH, xpath_delete)
        found_row.find_element(By.XPATH, '//i[@class="oxd-icon bi-trash"]').click()
        self.driver.find_element(By.XPATH, '//button[contains(.,"Yes, Delete")]').click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, xpath_delete)
            assert 'Element not removed'
        except NoSuchElementException:
            pass

        self.driver.close()







