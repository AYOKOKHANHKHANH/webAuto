import pytest
import unittest
import time
from utils.infoLogin import get_url_web
from pages.loginPage import LoginPage
from pages.logoutPage import LogoutPage
from utils.driversManages import get_driver
from config.envConfig import EnvConfig
from utils.driversManages import chrome_driver_init


@pytest.mark.usefixtures("driver_class")
class LoginTest(unittest.TestCase):

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

                # logout
                self.logout_event()

        except Exception as err:
            print("Login unsuccessfully", err)

    def logout_event(self):
        logout = LogoutPage(self.driver)
        try:
            try:
                logout.click_avatar()
            except Exception as err:
                print("Not avatar error", err)
                time.sleep(1)
                logout.click_avatar_not_img()

            logout.click_logout()
            logout.click_ok()
        except Exception as ex:
            print("Logout unsuccessfully", ex)

    def test_login_with_acc_and_pwd_correct(self):
        """
            user_name = True
            pwd = True
            :return login successfully
        """
        username = self.user_name
        pwd = self.pwd
        pin = self.pin

        self.login_event(username=username, pwd=pwd, pin=pin)

        # wait login
        time.sleep(1)

        # Expect login successfully
        assert self.driver.current_url == self.url + 'welcome'

    def test_login_with_acc_and_pwd_empty(self):
        """
            user_name = null
            pwd = null
            :return login unsuccessfully
        """
        username = ""
        pwd = ""

        self.login_event(username=username, pwd=pwd)
        # wait login
        time.sleep(1)

        # Expect login unsuccessfully
        assert self.driver.current_url != self.url

    def test_login_with_acc_true_pwd_empty(self):
        """
            user_name = True
            pwd = null
            :return login unsuccessfully
        """
        username = self.user_name
        pwd = ""

        self.login_event(username=username, pwd=pwd)

        # wait login
        time.sleep(1)

        # Expect login unsuccessfully
        assert self.driver.current_url != self.url

    def test_login_with_acc_empty(self):
        """
            user_name = Null
            pwd = True
            :return login unsuccessfully
        """
        username = ""
        pwd = self.pwd

        self.login_event(username=username, pwd=pwd)

        # wait login
        time.sleep(1)

        # Expect login unsuccessfully
        assert self.driver.current_url != self.url

    def test_login_with_acc_true_pwd_false(self):
        """
            user_name = True
            pwd = False
            :return login unsuccessfully
        """
        username = self.user_name
        pwd = "abcdeaa132"

        self.login_event(username=username, pwd=pwd)

        # wait login
        time.sleep(1)

        # Expect login unsuccessfully
        assert self.driver.current_url != self.url

    def test_login_with_acc_false_pwd_true(self):
        """
            user_name = False
            pwd = True
            :return login unsuccessfully
        """
        username = "0000088899"
        pwd = self.pwd

        self.login_event(username=username, pwd=pwd)

        # wait login
        time.sleep(1)

        # Expect login unsuccessfully
        assert self.driver.current_url != self.url


if __name__ == "__main__":
    unittest.main()
