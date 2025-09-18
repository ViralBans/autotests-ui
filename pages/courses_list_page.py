from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.courses_toolbar = CoursesListToolbarViewComponent(page)
        self.course_view = CourseViewComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')

    def check_navbar(self, username: str):
        self.navbar.check_visible(username=username)

    def check_sidebar(self):
        self.sidebar.check_visible()

    def check_visible_courses_toolbar(self):
        self.courses_toolbar.check_visible()

    def click_create_course_button(self):
        self.courses_toolbar.click_create_course_button()

    def check_visible_empty_view(self):
        self.empty_view.check_visible(title='There is no results', description='Results from the load test pipeline will be displayed here')

    def check_visible_course_card(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        self.course_view.check_visible(index=index, title=title, max_score=max_score, min_score=min_score, estimated_time=estimated_time)
