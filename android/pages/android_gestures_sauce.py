from android.pages import android_elements
from android.pages.android_base_page import AndroidBasePage
from common.globals import Globals
from android.pages import android_elements
from android.pages.android_base_page import AndroidBasePage
from android.pages.android_new_landing import AndroidNewLanding


class Androidgesture(AndroidBasePage):
    
    def global_gesture(self):
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.graphic_tab[5]
        )
    def load_global_gesture(self):
        self.global_gesture().click()


# elf.driver.find_elements_by_class_name(
#             android_elements.android_native_button
#         )[self.global_contents.second_existence].click()



        # return self.global_contents.wait_and_get_element(
        #     self.driver,
        #     android_elements.login_edx_logo
        # )