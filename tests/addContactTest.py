import pytest
import unittest
import time
from utils.infoLogin import get_url_web
from pages.loginPage import LoginPage
from pages.logoutPage import LogoutPage
from utils.driversManages import get_driver
from config.envConfig import EnvConfig
from utils.driversManages import chrome_driver_init
from pages.addContactPage import AddContactPage


# from tests.loginTest import LoginTest

@pytest.mark.usefixtures("driver_class")
class AddContact(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()
        self.url = get_url_web()
        self.driver.get(self.url)
        self.login_obj = LoginPage(self.driver)

        envConfig: EnvConfig = EnvConfig.getInstance()
        self.user_name = envConfig.info.user_name
        self.pwd = envConfig.info.pwd
        self.pin = envConfig.info.pin
        self.name_contact = envConfig.info.name_contact

    # def tearDown(self):
    #     self.driver.quit()

    def login_event(self, username, pwd, pin=None):
        try:
            self.login_obj.click_login_with_halo_acc()

            # Wait load page
            time.sleep(1)

            self.login_obj.enter_username(username)
            self.login_obj.enter_pwd(pwd)
            self.login_obj.click_login()

            if pin is not None:
                self.login_obj.click_continue()
                self.login_obj.enter_pin(pin)
                self.login_obj.click_accept_button()

                time.sleep(1)
                assert self.driver.current_url == self.url


        except Exception as err:
            print("Login unsuccessfully", err)

    def test_add_contact(self):
        username = self.user_name
        pwd = self.pwd
        pin = self.pin
        name_contact = self.name_contact
        self.login_event(username=username, pwd=pwd, pin=pin)
        time.sleep(2)
        add_contact = AddContactPage(self.driver)
        add_contact.click_chat_button()
        add_contact.click_add_contact_button()
        add_contact.enter_user_search(name_contact)
        add_contact.click_inbox_button()
        add_contact.click_hello_start_button()


