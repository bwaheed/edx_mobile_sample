
"""
    Course Dashboard screen Test Module
"""

from android.pages.android_login import AndroidLogin
from android.pages.android_main_dashboard import AndroidMainDashboard
from android.pages.android_new_landing import AndroidNewLanding
from android.pages.android_whats_new import AndroidWhatsNew
from android.pages.android_course_discovery import AndroidCourseDiscovery
from common import strings
from common.globals import Globals
from android.pages.android_my_courses_list import AndroidMyCoursesList
from android.pages.android_course_dashboard import AndroidCourseDashboard

class TestAndroidCourseDashboardScreen(object):
    """
    Test Course Dashboard Screen
    """

    def test_start_course_dashboard_smoke(self, login, set_capabilities, setup_logging):

        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidCourseDashboardScreen.__name__))

        global_contents = Globals(setup_logging)
        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        assert android_whats_new_page.navigate_features()
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

    def test_validate_ui_elements(self,set_capabilities, setup_logging):
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities,setup_logging)
        android_course_dashboard_page.load_course_dashboard_screen()
        assert android_course_dashboard_page.on_screen()==Globals.COURSE_DASHBOARD_ACTIVITY_NAME
        assert android_course_dashboard_page.get_course_detail_name()
        assert android_course_dashboard_page.get_share_icon()
        assert android_course_dashboard_page.get_back_icon()
        assert android_course_dashboard_page.get_vedio_tab()
        assert android_course_dashboard_page.get_discussion_tab()
        assert android_course_dashboard_page.get_important_dates_tab()
        assert android_course_dashboard_page.get_resourse_tab()
        assert android_course_dashboard_page.get_course_content_tab()

    def test_load_contents_smoke(self,set_capabilities, setup_logging):
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities,setup_logging)
        #load and click the elements
        android_course_dashboard_page.load_back_icon()
        android_course_dashboard_page.load_course_dashboard_screen()
        android_course_dashboard_page.load_course_content_tab()
        android_course_dashboard_page.load_vedio_tab()
        android_course_dashboard_page.load_discussion_tab()
        android_course_dashboard_page.load_important_dates_tab()
        android_course_dashboard_page.load_resourse_tab()
        # android_course_dashboard_page.load_course_content_tab()
    
    def test_course_content_tab(self,set_capabilities, setup_logging):
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities,setup_logging)
        android_course_dashboard_page.load_course_content_tab()
        assert android_course_dashboard_page.get_course_header_image().text == strings.BLANK_FIELD
        assert android_course_dashboard_page.get_last_accessed_bar().text == strings.BLANK_FIELD
        assert android_course_dashboard_page.get_last_accessed_button().text == strings.LAST_ACCESSED_BUTTON
        android_course_dashboard_page.load_course_content_list()
    
    def test_vedio_content_tab(self,set_capabilities, setup_logging):
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities,setup_logging)
        android_course_dashboard_page.load_vedio_tab()
        android_course_dashboard_page.load_course_content_list()

    
    def test_load_discussion_tab(self,set_capabilities, setup_logging):
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities,setup_logging)
        android_course_dashboard_page.load_discussion_tab()
        # android_course_dashboard_page.load_discussion_content_list()
    
    def test_load_important_dates_tab(self,set_capabilities, setup_logging):
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities,setup_logging)
        android_course_dashboard_page.load_important_dates_tab()
        # android_course_dashboard_page.load_back_icon()

        # android_course_dashboard_page.load_course_content_list()
    
    def test_load_resourse_tab(self,set_capabilities, setup_logging):
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities,setup_logging)
        android_course_dashboard_page.load_resourse_tab()
        android_course_dashboard_page.load_resources_content_list()

       
        
        

