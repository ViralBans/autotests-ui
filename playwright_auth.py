from playwright.sync_api import sync_playwright, expect

from config import settings
from tools.routes import AppRoute

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill(settings.test_user.email)

    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill(settings.test_user.password)

    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')