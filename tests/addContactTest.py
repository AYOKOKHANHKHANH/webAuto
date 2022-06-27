import pytest
import unittest
import time
from utils.infoLogin import get_url_web
from pages.loginPage import LoginPage
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

    def tearDown(self):
        self.driver.quit()

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
        self.login_event(username=self.user_name, pwd=self.pwd, pin=self.pin)
        # name_contact = self.name_contact
        add_contact = AddContactPage(self.driver)
        add_contact.click_chat_button()
        add_contact.click_add_contact_button()
        add_contact.enter_user_search("0904613192")
        add_contact.click_inbox_button()
        try:
            add_contact.click_hello_start_button()
        except:
            pass


    def test_friend_accept(self):
        username = "0904613192"
        pwd = "blackpinkinyourarea"
        pin = self.pin
        self.login_event(username=username, pwd=pwd, pin=pin)
        friend_accept = AddContactPage(self.driver)
        friend_accept.click_chat_button()
        try:
            friend_accept.click_wait_message_button()
            friend_accept.click_agree_button()
        except Exception as eror:
            print(eror)

    def test_list_friend(self):
        self.login_event(username=self.user_name, pwd=self.pwd, pin=self.pin)
        name_contact = self.name_contact
        list_friend = AddContactPage(self.driver)
        list_friend.click_list_contact_button()
        print(list_friend.get_name_contact_in_list_friend())
        if name_contact in list_friend.get_name_contact_in_list_friend():
            print("Found")
        else:
            print("Not Found")