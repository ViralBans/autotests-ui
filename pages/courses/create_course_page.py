from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.course_toolbar = CreateCourseToolbarViewComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.course_form = CreateCourseFormComponent(page)
        self.exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.exercise_form = CreateCourseExerciseFormComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')

    def check_visible_course_toolbar(self, is_create_course_disabled: bool):
        self.course_toolbar.check_visible(is_create_course_disabled)

    def click_create_course_button(self):
        self.course_toolbar.click_create_course_button()

    def check_image_upload_widget(self, is_image_uploaded: bool):
        self.image_upload_widget.check_visible(is_image_uploaded=is_image_uploaded)

    def upload_preview_image(self, file: str):
        self.image_upload_widget.upload_preview_image(file)

    def remove_preview_image(self):
        self.image_upload_widget.click_remove_image_button()

    def check_visible_course_form(self, title: str, estimated_time: str, description: str, max_score: str,
                                  min_score: str):
        self.course_form.check_visible(title=title, estimated_time=estimated_time, description=description,
                                       max_score=max_score, min_score=min_score)

    def fill_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.course_form.fill(title=title, estimated_time=estimated_time, description=description, max_score=max_score,
                              min_score=min_score)

    def check_visible_exercise_toolbar(self):
        self.exercise_toolbar.check_visible()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(title='There is no exercises',
                                                description='Click on "Create exercise" button to create new exercise')

    def click_create_exercise_button(self):
        self.exercise_toolbar.click_create_exercise_button()

    def check_visible_exercise_form(self, index: int, title: str, description: str):
        self.exercise_form.check_visible(index=index, title=title, description=description)

    def fill_exercise_form(self, index: int, title: str, description: str):
        self.exercise_form.check_visible(index=index, title=title, description=description)
