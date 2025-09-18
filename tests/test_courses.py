import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()

    courses_list_page.check_visible_courses_toolbar()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    create_course_page.check_visible_course_toolbar(True)
    create_course_page.check_image_upload_widget(False)
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_image_upload_widget(True)
    create_course_page.fill_course_form(title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10')
    create_course_page.check_visible_course_toolbar(False)
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_course_card(index=0, title='Playwright', estimated_time='2 weeks', max_score='100', min_score='10')
