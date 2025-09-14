from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы элементов страницы
        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    #Метод для заполнения формы регистрации
    def fill_registration_form(self, email, username, password):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)  # Проверяем, что email введен корректно

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username) # Проверяем, что username введен корректно

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password) # Проверяем, что password введен корректно

    # Метод для нажатия на кнопку "Registration"
    def click_registration_button(self):
        self.registration_button.click()

    # Метод для нажатия на ссылку "Login"
    def click_login_link(self):
        self.login_link.click()