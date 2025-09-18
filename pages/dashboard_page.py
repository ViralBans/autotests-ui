from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.scores_chart_view = ChartViewComponent(page, identifier='scores', chart_type='scatter')
        self.courses_chart_view = ChartViewComponent(page, identifier='courses', chart_type='pie')
        self.students_chart_view = ChartViewComponent(page, identifier='students', chart_type='bar')
        self.activities_chart_view = ChartViewComponent(page, identifier='activities', chart_type='line')
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

    def check_visible_navbar(self, username: str):
        self.navbar.check_visible(username)

    def check_visible_sidebar(self):
        self.sidebar.check_visible()

    def check_visible_dashboard_title(self):
        self.dashboard_toolbar.check_visible()

    def check_visible_students_chart(self):
        self.students_chart_view.check_visible('Students')

    def check_visible_activities_chart(self):
        self.activities_chart_view.check_visible('Activities')

    def check_visible_courses_chart(self):
        self.courses_chart_view.check_visible('Courses')

    def check_visible_scores_chart(self):
        self.scores_chart_view.check_visible('Scores')
