from pages.LoginPage.loginPage import LoginPage
from pages.LoginPage.logoutPage import LogoutPage
from utils.driversManages import chrome_driver_init
import unittest
import time
from utils.infoLogin import get_info_login_anonymous
from utils.driversManages import get_driver
from utils.infoLogin import get_url_web



class LoginAnonymousTest(unittest.TestCase):

    def setUp(self):
        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()
        self.url = get_url_web()
        self.driver.get(self.url)
        self.login_obj = LoginPage(self.driver)
        info = get_info_login_anonymous()
        self.url = info[0]
        self.phone_number = info[1]
        self.otp = info[2]

    def login_event(self, phone_number, otp, name = None):
        try:
            self.login_obj.click_login_with_anonymous_acc()
            self.login_obj.enter_phone_number(phone_number)
            self.login_obj.click_login_anonymous_start_btn()
            self.login_obj.enter_otp(otp)
            try:
                self.login_obj.click_recent_SMS()
                self.login_obj.re_enter_otp(otp)
            except Exception:
                self.login_obj.enter_name_Anony("ddsfdf")
                self.login_obj.click_continue_button_Anony()
        except Exception:
            print("Login Unsuccessfully")


    def logout_event(self):
        logout = LogoutPage(self.driver)
        try:
            try:
                logout.click_avatar()
            except Exception as err:
                print("Not avatar error", err)
                logout.click_avatar_not_img()

            logout.click_logout()
            logout.click_ok()
        except Exception as ex:
            print("Logout unsuccessfully", ex)




    def test_login_success(self):
        '''
            number_phone = True
            otp = True
            return: login successfully
        '''
        self.login_event(phone_number = self.phone_number,otp = self.otp)

        time.sleep(2)
        assert self.driver.current_url == self.url

        self.logout_event()

    def test_loginAnomy_phone_invalid(self):
        '''
            phone_number = False
            return: login unsuccessfully
        '''
        phone_number = '1234'
        otp = self.otp
        self.login_event(phone_number,otp)

        assert self.login_obj.click_login_anonymous_start_btn() == None


    def test_loginAnony_phone_empty(self):
        '''
            phone_number = Empty
            return: login unsuccessfully
        '''
        phone_number = ''
        otp = self.otp
        self.login_event(phone_number, otp)

        assert self.login_obj.click_login_anonymous_start_btn() == None

    def test_loginAnony_otp_False(self):
        '''
            otp = False
            return: login unsuccessfully
        '''
        phone_number = self.phone_number
        otp = '111111'
        self.login_event(phone_number,otp)

        assert self.driver.current_url != self.url

    def test_loginAnony_otp_empty(self):
        '''
            otp = Empty
            return: login unsuccessfully
        '''
        phone_number = self.phone_number
        otp = ''
        self.login_event(phone_number,otp)

        assert self.driver.current_url != self.url


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()