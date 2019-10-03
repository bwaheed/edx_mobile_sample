from appium import webdriver
import pytest
# from appium import SauceTestCase, on_platforms
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from android.pages import android_elements
from android.pages.android_base_page import AndroidBasePage
from android.pages.android_course_dashboard import AndroidCourseDashboard
from android.pages.android_gestures_sauce import Androidgesture



from android.pages.android_login import AndroidLogin
from android.pages.android_main_dashboard import AndroidMainDashboard
from android.pages.android_new_landing import AndroidNewLanding
from android.pages.android_whats_new import AndroidWhatsNew
from android.pages.android_course_discovery import AndroidCourseDiscovery
from common import strings
from common.globals import Globals
from android.pages.android_my_courses_list import AndroidMyCoursesList
from android.pages.android_course_dashboard import AndroidCourseDashboard




from time import sleep

app = "http://appium.github.io/appium/assets/ApiDemos-debug.apk"


class TestAndroidGesturesSauceTests():

    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            # 'appPackage': 'com.example.android.contactmanager',
            'appActivity': '.ApiDemos',
            'platformName': 'Android',
            'platformVersion': '4.4.4',
            'deviceName': 'Android Emulator',
            'appPackage': 'io.appium.android.apis'
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value


    def test_drag_and_drop(self, driver):
        # first get to the right activity
        driver.start_activity("io.appium.android.apis", ".ApiDemos")

        start = self.driver.find_element_by_id("io.appium.android.apis:id/drag_dot_3")
        end = self.driver.find_element_by_id("io.appium.android.apis:id/drag_dot_2")

        action = TouchAction(self.driver)
        action.long_press(start).move_to(end).release().perform()

        sleep(.5)

        text = self.driver.find_element_by_id("io.appium.android.apis:id/drag_result_text").text
        self.assertEqual(text, "Dropped!")

    def test_graphic_tab(self, set_capabilities, setup_logging):
        driver.start_activity("io.appium.android.apis", ".ApiDemos")        
        android_android_gestures_sauce = Androidgesture(set_capabilities, setup_logging)
        android_android_gestures_sauce.load_global_gesture()


    def test_smiley_face(self, driver, set_capabilities, setup_logging):
        # just for the fun of it.
        # this doesn't really assert anything.
        # paint
        android_android_gestures_sauce = Androidgesture(set_capabilities, setup_logging)
        android_android_gestures_sauce.load_global_gesture()

        
        eye1 = TouchAction()
        eye1.press(x=150, y=100).release()

        eye2 = TouchAction()
        eye2.press(x=250, y=100).release()

        smile = TouchAction()
        smile.press(x=110, y=200) \
            .move_to(x=1, y=1) \
            .move_to(x=1, y=1) \
            .move_to(x=1, y=1) \
            .move_to(x=1, y=1) \
            .move_to(x=1, y=1) \
            .move_to(x=2, y=1) \
            .move_to(x=2, y=1) \
            .move_to(x=2, y=1) \
            .move_to(x=2, y=1) \
            .move_to(x=2, y=1) \
            .move_to(x=3, y=1) \
            .move_to(x=3, y=1) \
            .move_to(x=3, y=1) \
            .move_to(x=3, y=1) \
            .move_to(x=3, y=1) \
            .move_to(x=4, y=1) \
            .move_to(x=4, y=1) \
            .move_to(x=4, y=1) \
            .move_to(x=4, y=1) \
            .move_to(x=4, y=1) \
            .move_to(x=5, y=1) \
            .move_to(x=5, y=1) \
            .move_to(x=5, y=1) \
            .move_to(x=5, y=1) \
            .move_to(x=5, y=1) \
            .move_to(x=5, y=0) \
            .move_to(x=5, y=0) \
            .move_to(x=5, y=0) \
            .move_to(x=5, y=0) \
            .move_to(x=5, y=0) \
            .move_to(x=5, y=0) \
            .move_to(x=5, y=0) \
            .move_to(x=5, y=0) \
            .move_to(x=5, y=-1) \
            .move_to(x=5, y=-1) \
            .move_to(x=5, y=-1) \
            .move_to(x=5, y=-1) \
            .move_to(x=5, y=-1) \
            .move_to(x=4, y=-1) \
            .move_to(x=4, y=-1) \
            .move_to(x=4, y=-1) \
            .move_to(x=4, y=-1) \
            .move_to(x=4, y=-1) \
            .move_to(x=3, y=-1) \
            .move_to(x=3, y=-1) \
            .move_to(x=3, y=-1) \
            .move_to(x=3, y=-1) \
            .move_to(x=3, y=-1) \
            .move_to(x=2, y=-1) \
            .move_to(x=2, y=-1) \
            .move_to(x=2, y=-1) \
            .move_to(x=2, y=-1) \
            .move_to(x=2, y=-1) \
            .move_to(x=1, y=-1) \
            .move_to(x=1, y=-1) \
            .move_to(x=1, y=-1) \
            .move_to(x=1, y=-1) \
            .move_to(x=1, y=-1)
        smile.release()

        ma = MultiAction(driver)
        ma.add(eye1, eye2, smile)
        ma.perform()

        # so you can see it
        sleep(10)
