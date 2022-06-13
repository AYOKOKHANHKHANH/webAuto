from pages.loginPage import LoginPage
from pages.logoutPage import LogoutPage
from utils.driversManages import chrome_driver_init
import unittest
import time
from utils.infoLogin import get_info_login_anonymous
from selenium.common.exceptions import NoSuchElementException


class LoginTestInChrome(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = chrome_driver_init()
        info = get_info_login_anonymous()
        self.url = info[0]
        self.phone_number = info[1]
        self.opt = info[2]

    def test_login(self):
        self.driver.get(self.url)
        login = LoginPage(self.driver)
        login.click_login_with_anonymous_acc()
        login.enter_phone_number(self.phone_number)
        login.click_login_anonymous_start_btn()
        try:
            login.enter_opt(self.opt)
        except NoSuchElementException as no_element:
            print(no_element)
            pass

        time.sleep(3)
        if self.driver.current_url == self.url:
            print("Đăng nhập thành công")
            logout = LogoutPage(self.driver)
            logout.click_avatar()
            logout.click_logout()
            logout.click_ok()
        else:
            print("Đăng nhập không thành công")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
