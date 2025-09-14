from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Метод для открытия страницы
    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    # Метод для перезагрузки страницы
    def reload(self):
        self.page.reload(wait_until='networkidle')
