import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()

        courses_list_page.check_visible_courses_toolbar()
        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.COURSES_CREATE)

        create_course_page.check_visible_course_toolbar(True)
        create_course_page.check_image_upload_widget(False)
        create_course_page.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.check_image_upload_widget(True)
        create_course_page.fill_course_form(title='Playwright', estimated_time='2 weeks', description='Playwright',
                                            max_score='100', min_score='10')
        create_course_page.check_visible_course_toolbar(False)
        create_course_page.click_create_course_button()
        courses_list_page.check_visible_course_card(index=0, title='Playwright', estimated_time='2 weeks',
                                                    max_score='100', min_score='10')

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.COURSES_CREATE)

        create_course_page.check_visible_course_toolbar(True)
        create_course_page.check_image_upload_widget(False)
        create_course_page.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.check_image_upload_widget(True)
        create_course_page.fill_course_form(title='Playwright', estimated_time='2 weeks', description='Playwright',
                                            max_score='100', min_score='10')
        create_course_page.check_visible_course_toolbar(False)
        create_course_page.click_create_course_button()

        courses_list_page.check_visible_course_card(index=0, title='Playwright', estimated_time='2 weeks',
                                                    max_score='100', min_score='10')
        courses_list_page.click_edit(index=0)

        create_course_page.fill_course_form(title='Playwright New', estimated_time='3 weeks', description='Playwright New Desc',
                                            max_score='150', min_score='20')
        create_course_page.click_create_course_button()

        courses_list_page.check_visible_course_card(index=0, title='Playwright New', estimated_time='3 weeks',
                                                    max_score='150', min_score='20')