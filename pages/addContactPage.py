from locators.addContactLocator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddContactPage:
    def __init__(self, driver):
        self.driver = driver

    def click_chat_button(self):
        print("Click chat button")
        # chat_button = self.driver.find_element_by_xpath(get_chat_button_xpath())
        chat_button = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.XPATH, get_chat_button_xpath())))
        chat_button.click()

    def click_add_contact_button(self):
        print("Click add contact button")
        # add_contact_button = self.driver.find_element_by_id(get_add_contact_button_id())
        add_contact_button = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.ID, get_add_contact_button_id())))
        add_contact_button.click()

    def enter_user_search(self,name_contact):
        print("Enter user need add contact")
        # user_search = self.driver.find_element_by_xpath(get_search_button_mini_xpath())
        user_search = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.XPATH, get_search_button_mini_xpath())))
        user_search.send_keys(name_contact)

    def click_close_button(self):
        print("Click close button")
        # close_button = self.driver.find_element_by_xpath(get_close_button_xpath())
        close_button = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.XPATH, get_close_button_xpath())))
        close_button.click()

    def click_inbox_button(self):
        print("Click inbox button")
        # inbox_button = self.driver.find_element_by_xpath(get_inbox_button_xpath())
        inbox_button = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.XPATH, get_inbox_button_xpath())))
        inbox_button.click()

    def click_hello_start_button(self):
        print("Click hello start button")
        # hello_start_button = self.driver.find(By.CSS_SELECTOR,get_hello_start_button_css())
        hello_start_button = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, get_hello_start_button_css())))
        hello_start_button.click()

    def click_hi_button(self):
        print("Click hi button")
        # hi_button = self.driver.find_element_by_xpath(get_hi_button_xpath())
        hi_button = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.XPATH, get_hi_button_xpath())))
        hi_button.click()

    def get_name_contact_in_list_friend(self):
        print("get name contact in list friend")
        name_contact_in_list_fr = self.driver.find_element_by_xpath(get_contact_in_list_friend_xpath()).text
        return name_contact_in_list_fr

    def click_list_contact_button(self):
        print("Click list contact button")
        # list_contact_button = self.driver.find_element_by_id(get_list_contact_button_id())
        list_contact_button = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.ID, get_list_contact_button_id())))
        list_contact_button.click()

    def click_wait_message_button(self):
        print("Click wait message button")
        # wait_message = self.driver.find_element_by_xpath(get_wait_message_button_xpath())
        wait_message = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((get_wait_message_button_xpath())))
        wait_message.click()

    def click_agree_button(self):
        print("Click agree button")
        # agree_button = self.driver.find_element(By.CSS_SELECTOR,get_agree_button_css())
        agree_button = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, get_agree_button_css())))
        agree_button.click()

    def click_not_agree_button(self):
        print("Click not agree button")
        # not_agree_button = self.driver.find_element_by_xpath(get_not_agree_button_css())
        not_agree_button = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, get_not_agree_button_css())))
        not_agree_button.click()