from locators.LoginLocator.loginLocator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_login_with_halo_acc(self):
        print('Login with haha lolo account')
        # login_halo_acc = self.driver.find_element_by_id(get_login_with_halo_btn_id())
        login_halo_acc = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_login_with_halo_btn_id())))
        login_halo_acc.click()

    def click_login_with_anonymous_acc(self):
        print('Login with anonymous account')
        # anonymous_btn = self.driver.find_element_by_id(get_anonymous_btn_id())
        anonymous_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_anonymous_btn_id())))
        anonymous_btn.click()

    def enter_username(self, username):
        print("Enter user name")
        username_input = self.driver.find_element_by_id(get_username_id())
        # username_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, get_username_id())))
        username_input.clear()
        username_input.send_keys(username)

    def enter_pwd(self, pwd):
        print("Enter password")
        pwd_input = self.driver.find_element_by_id(get_pwd_id())
        # pwd_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, get_pwd_id())))
        pwd_input.clear()
        pwd_input.send_keys(pwd)

    def click_login(self):
        print("Click login button")
        # login_btn = self.driver.find_element_by_xpath(get_login_btn_xpath())
        login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, get_login_btn_xpath())))
        login_btn.click()

    def click_continue(self):
        print("Click login continue")
        # login_continue_btn = self.driver.find_element_by_id(get_login_continue_btn_id())
        login_continue_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_login_continue_btn_id())))
        login_continue_btn.click()

    def enter_phone_number(self, phone_number):
        print("Enter phone number")
        # phone_number_input = self.driver.find_element_by_id(get_input_phone_number_id())
        phone_number_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_input_phone_number_id())))
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)

    def click_login_anonymous_start_btn(self):
        print("Start")
        # anonymous_start_btn = self.driver.find_element_by_id(get_anonymous_start_btn_id())
        anonymous_start_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_anonymous_start_btn_id())))
        anonymous_start_btn.click()

    def enter_otp(self, otp):
        print("Enter otp")
        # otp_input = self.driver.find_element_by_xpath(get_otp_input_xpath())
        otp_input = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, get_otp_input_xpath())))
        otp_input.clear()
        otp_input.send_keys(otp)

    def enter_pin(self, pin):
        print("Enter Pin")
        # pin_input = self.driver.find_element_by_xpath(get_pin_input_xpath())
        pin_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_pin_input_xpath())))
        pin_input.clear()
        pin_input.send_keys(pin)

    def click_not_account(self):
        print("Not me")
        # not_account = self.driver.find_element_by_xpath(get_not_account())
        not_account = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_not_account())))
        not_account.click()

    def get_noty_login_fail(self):
        print("Notification")
        # notify_el = self.driver.find_element_by_xpath(get_notify_login_fail_xpath())
        notify_el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_notify_login_fail_xpath())))
        return notify_el.text

    def get_helper_text_user_name(self):
        print("Get validate user name input")
        # helper_text = self.driver.find_element_by_id(get_accountId_helper_text_id())
        helper_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_accountId_helper_text_id())))
        return helper_text.text

    def get_helper_text_password(self):
        print("Get validate user name input")
        # helper_text = self.driver.find_element_by_id(get_password_helper_text_id())
        helper_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_password_helper_text_id())))
        return helper_text.text

    def click_accept_button(self):
        print("Click accept button")
        # accept_button = self.driver.find_element_by_id(get_accept_button_id())
        accept_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_accept_button_id())))
        accept_button.click()

    def re_enter_pin(self,pin):
        print("Re_enter pin")
        # re_pin = self.driver.find_element_by_xpath(get_pin_input_re_xpath())
        re_pin = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, get_pin_input_re_xpath())))
        re_pin.send_keys(pin)

    def click_save_button(self):
        print("Click save button")
        # save_button = self.driver.find_element_by_id(get_save_button_xpath())
        save_button = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, get_save_button_xpath())))
        save_button.click()

    def click_recent_SMS(self):
        print("Click recent SMS")
        # recend_SMS = self.driver.find_element_by_id(get_resend_SMS_button_id())
        recend_SMS = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_resend_SMS_button_id())))
        recend_SMS.click()

    def re_enter_otp(self,otp):
        print("Re enter otp")
        # re_enter = self.driver.find_element_by_xpath(get_re_otp_input_xpath())
        re_enter = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_re_otp_input_xpath())))
        re_enter.click()
        re_enter.send_keys(otp)

    def enter_name_Anony(self,name):
        print("Enter name Anony")
        # name_Anony = self.driver.find_element_by_id(get_enter_name_Anony_id())
        name_Anony = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_enter_name_Anony_id())))
        name_Anony.clear()
        name_Anony.send_keys(name)

    def click_continue_button_Anony(self):
        print("Click continue button")
        # continue_button = self.driver.find_element_by_id(get_continue_button_id())
        continue_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, get_continue_button_id()))
        continue_button.click()