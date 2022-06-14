import time
import pytest
import unittest
from config.envConfig import EnvConfig
from pages.loginPage import LoginPage
from pages.createGroupPage import CreateGroupPage
from utils.driversManages import chrome_driver_init
from utils.driversManages import get_driver
from utils.infoLogin import get_url_web


@pytest.mark.usefixtures("driver_class")
class CreateGroup(unittest.TestCase):
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
        self.name_group = envConfig.info.name_group

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

    def test_create_group(self):
        username = self.user_name
        pwd = self.pwd
        pin = self.pin
        name_contact = self.name_contact
        name_group = self.name_group
        self.login_event(username,pwd,pin)
        create_group = CreateGroupPage(self.driver)
        create_group.click_group_button()
        create_group.click_add_channel_button()
        create_group.enter_name_group(name_group)
        # create_group.click_close_button()
        create_group.click_ok_button()
        time.sleep(1)
        create_group.click_close_button()
        # create_group.click_option_button()
        # time.sleep(1)
        # create_group.click_del_group_button()
        # create_group.click_ok_button()

    def test_del_group(self):
        self.test_create_group()
        del_group = CreateGroupPage(self.driver)
        del_group.click_option_button()
        time.sleep(1)
        del_group.click_del_group_button()
        del_group.click_ok_button()