# coding=utf-8
"""
    Course Dashboard Page Module
"""

from android.pages import android_elements
from android.pages.android_base_page import AndroidBasePage

class AndroidCourseDashboard(AndroidBasePage):
    """
    Main Dashboard screen
    """

    def on_screen(self):
        """
        Load Main Dashboard screen

        Returns:
            str: Main Dashboard screen Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.COURSE_DASHBOARD_ACTIVITY_NAME
        )

    def get_my_courses_list_course_image(self):
        """
        Get Courses List

        Returns:
            webdriver element: Courses List Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.my_courses_list_course_image
        )

    def load_course_dashboard_screen(self):
        """
        Load Course Dashboard Screen
        """

        self.get_my_courses_list_course_image().click()

    def get_back_icon(self):
        """
        Get back icon
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Back_icon

        )
    def load_back_icon(self):
        self.get_back_icon().click()

    def get_course_name(self):
        """
        Get Course Name
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Course_name
        )

    def get_course_detail_name(self):
        """
        Get Course Detail Name
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Course_detail_name
        )
    def get_share_icon(self):
        """
        Get share icon
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.share_course
        )

    def get_course_content_tab(self):
        """
        Get Course Content Tab
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Course_content_tab
        )

    def load_course_content_tab(self):
        """
        Get Course Content Tab
        """
        self.get_course_content_tab().click()
    
    def get_vedio_tab(self):
        """
        Get Course Content Tab
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.vedio_tab
        )
    def load_vedio_tab(self):
        """
        Get Course Content Tab
        """
        self.get_vedio_tab().click()
    def get_discussion_tab(self):
        """
        Get Course Content Tab
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Discussion_tab
        )
    def load_discussion_tab(self):
        """
        Get Course Content Tab
        """
        self.get_discussion_tab().click()
    def get_important_dates_tab(self):
        """
        Get Course Content Tab
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Important_dates
        )
    def load_important_dates_tab(self):
        """
        Get Course Content Tab
        """
        self.get_important_dates_tab().click()
    def get_resourse_tab(self):
        """
        Get Course Content Tab
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Resources
        )
    def load_resourse_tab(self):
        """
        Get Course Content Tab
        """
        self.get_resourse_tab().click()
    
    def course_content_list(self):
        """
        list of all course section
        """
        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.course_content_list
        )
    
    def swipe_content(self):
        # self.driver.swipe(470, 1900, 470, 1000, 800)
        self.driver.swipe(470, 1250, 470, 1000, 3000)
        self.load_course_content_list()

    def get_next_vedio_button(self):
        """
        Get next vedio button
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.next_vedio_button
        )
    def get_previous_vedio_button(self):
        """
        Get previous vedio button
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.previous_vedio_button
        )
    
    def load_course_content_list(self):
        """
        Load course content list
        """
        if self.course_content_list():
            for item in self.course_content_list():
                item.click()
                if self.course_content_list():
                    for detail_item in self.course_content_list():
                        detail_item.click()
                        if self.get_next_vedio_button() and self.get_previous_vedio_button:
                            self.get_next_vedio_button().click()
                            self.get_previous_vedio_button().click()
                        self.get_back_icon().click()
                else:
                    self.get_back_icon().click()
                    # self.get_back_icon().click()
                self.get_back_icon().click()
            self.swipe_content()
        else:
            self.get_back_icon().click()

    def load_resources_content_list(self):
        """
        Load course content list
        """
        if self.course_content_list():
            for item in self.course_content_list():
                item.click()
                if self.course_content_list():
                    for detail_item in self.course_content_list():
                        detail_item.click()
                    
                        self.get_back_icon().click()
                else:
                    self.get_back_icon().click()
                    # self.get_back_icon().click()
            self.get_back_icon().click()
        else:
            self.get_back_icon().click()



    def discussion_content_list(self):
        """
        list of all discussion section
        """
        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.discussion_topic_name
        )
    def load_discussion_content_list(self):
        """
        Load discussion content list
        """
        for item in self.discussion_content_list():
            item.click()
            self.get_back_icon().click()
        # self.swipe_content()

    def get_course_header_image(self):
        """
        Get Course Header Image
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Course_header_image
        )
    def get_last_accessed_bar(self):
        """
        Get Last Accessed bar 
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Last_accessed_bar
        )
    def get_last_accessed_button(self):
        """
        Get last accessed buttton
        """
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.Last_accessed_view_button
        )

    # def get_course_tab_dashboard_activity():
    #     """
    #     Get course tab activities name 
    #     When user tap on any tab
    #     """
    #     return self.global_contents.wait_and_get_element(
    #         self.driver,
    #         android_elements.course_tab_da
    #     )
    
    




