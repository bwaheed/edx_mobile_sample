# coding=utf-8
"""
    Login Test Module
"""
from android.pages.android_login import AndroidLogin
from android.pages.android_new_landing import AndroidNewLanding
from common import strings
from common.globals import Globals
from appium import webdriver
import os


class TestAndroidLogin(object):
    """
    Login screen's Test Case
    """

    def test_start_login_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Login screen is loaded successfully
        """
        try:
            setup_logging.info('-- Starting {} Test Case'.format(TestAndroidLogin.__name__))

            android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
            android_login_page = AndroidLogin(set_capabilities, setup_logging)

            assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
            assert android_login_page.on_screen() == Globals.LOGIN_ACTIVITY_NAME

            setup_logging.info('Login screen successfully loaded')
            android_login_page.wifi_toggle()
            android_login_page.location_toggle()

            # set_capabilities.driver.toggle_wifi()
        except:
            android_login_page = AndroidLogin(set_capabilities, setup_logging)
            android_global = Globals(object)
            test_case_name = 'test_start_login_smoke'
            android_global.screenshot(set_capabilities, test_case_name, setup_logging)
            android_login_page.wifi_toggle()
            android_login_page.location_toggle()

            # set_capabilities.driver.toggle_wifi()
            # assert 1 == 0
    
    # self.driver.toggle_wifi()

    def test_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on screen 
            "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
            Password edit-field, "Forgot your password?" option, "Sign In" button,
            "Or sing in with" label, "Facebook" button, "Google" button,
            "By signing in to this app, you agree to the" label,
            "edX Terms of Service and Honor Code" option
        Verify all screen contents have their default values
        """
        try:
            android_login_page = AndroidLogin(set_capabilities, setup_logging)

            assert android_login_page.get_title_textview().text == strings.LOGIN
            assert android_login_page.get_username_editfield().text == strings.BLANK_FIELD
            assert android_login_page.get_password_editfield().text == strings.BLANK_FIELD
            # assert android_login_page.get_password_editfield().text == strings.LOGIN_PASSWORD_WATER_MARK
            assert android_login_page.get_forgot_password_textview().text == strings.LOGIN_FORGOT_PASSWORD
            assert android_login_page.get_sign_in_button().text == strings.LOGIN
            login_with_email_divider = android_login_page.get_login_with_email_divider_textview().text
            assert login_with_email_divider == strings.LOGIN_ANDROID_WITH_EMAIL_DIVIDER
            assert android_login_page.get_facebook_textview().text == strings.FACEBOOK_OPTION
            assert android_login_page.get_google_textview().text == strings.GOOGLE_OPTION
            assert android_login_page.get_agreement_textview().text == strings.LOGIN_ANDROID_AGREEMENT
        except:
            android_login_page = AndroidLogin(set_capabilities, setup_logging)
            android_global = Globals(object)
            test_case_name = 'test_ui_elements'
            android_global.screenshot(set_capabilities, test_case_name, setup_logging)
            assert 1 == 0

    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping back icon from 'Sign In' screen navigate user
                    back to 'New Landing' screen.
                Verify that user is able to load EULA screen and get back to Login Screen
                Verify that user is able to load Terms screen and get back to Login Screen
                Verify that user is able to load Privacy screen and get back to Login Screen
        """
        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_login_page.back_and_forth_login()
        # assert android_login_page.load_eula_screen()
        # assert android_login_page.load_terms_screen()
        # assert android_login_page.load_privacy_screen()

    def test_forgot_password_alert(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping 'Forgot your password?' will  load 'Reset Password' alert
                Verify following contents are visible on 'Reset Password' alert, 
                Alert Title, Alert Message, Email edit field, Cancel & OK buttons
                Verify tapping 'Cancel' will close 'Reset Password' alert
        """
        try:
            android_login_page = AndroidLogin(set_capabilities, setup_logging)
            android_login_page.get_forgot_password_alert()

            assert android_login_page.get_forgot_password_alert_title().text == strings.LOGIN_RESET_PASSWORD_ALERT_TITLE
            # assert android_login_page.get_forgot_password_alert_msg().text == strings.LOGIN_RESET_PASSWORD_ALERT_MSG
            assert android_login_page.get_forgot_password_alert_ok_button().text == strings.LOGIN_RESET_PASSWORD_ALERT_OK
            forgot_password_alert_cancel_button = android_login_page.get_forgot_password_alert_cancel_button().text
            assert 1 == 0
            assert forgot_password_alert_cancel_button == strings.LOGIN_RESET_PASSWORD_ALERT_CANCEL

            assert android_login_page.close_forgot_password_alert()

        except:
            android_login_page = AndroidLogin(set_capabilities, setup_logging)
            android_global = Globals(object)
            test_case_name = 'test_forgot_password_alert'
            android_global.screenshot(set_capabilities, test_case_name, setup_logging)
            assert 1 == 0

    def test_login_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can login with valid Username and Password
        """

        global_contents = Globals(setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_login_page.login(
            global_contents.login_wrong_user_name,
            global_contents.login_wrong_password) is False

        login_output = android_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password)
        assert login_output == Globals.WHATS_NEW_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))
        setup_logging.info('-- Ending {} Test Case'.format(TestAndroidLogin.__name__))
