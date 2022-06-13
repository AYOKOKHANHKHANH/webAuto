from locators.addContactLocator import *


class AddContactPage:
    def __init__(self, driver):
        self.driver = driver

    def click_chat_button(self):
        print("Click chat button")
        chat_button = self.driver.find_element_by_xpath(get_chat_button_xpath())
        chat_button.click()

    def click_add_contact_button(self):
        print("Click add contact button")
        add_contact_button = self.driver.find_element_by_id(get_add_contact_button_id())
        add_contact_button.click()

    def enter_user_search(self,name_contact):
        print("Enter user need add contact")
        user_search = self.driver.find_element_by_xpath(get_search_button_mini_xpath())
        user_search.send_keys(name_contact)

    def click_close_button(self):
        print("Click close button")
        close_button = self.driver.find_element_by_xpath(get_close_button_xpath())
        close_button.click()

    def click_inbox_button(self):
        print("Click inbox button")
        inbox_button = self.driver.find_element_by_xpath(get_inbox_button_xpath())
        inbox_button.click()

    def click_hello_start_button(self):
        print("Click hello start button")
        hello_start_button = self.driver.find_element_by_xpath(get_hello_start_button_xpath())
        hello_start_button.click()

    def click_hi_button(self):
        print("Click hi button")
        hi_button = self.driver.find_element_by_xpath(get_hi_button_xpath())
        hi_button.click()

