from enum import Enum
from typing import Self

from pathlib import Path
from pydantic import EmailStr, HttpUrl, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: Path


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: Path
    tracing_dir: Path
    browser_state_file: Path

    def get_base_url(self) -> str:
        return f"{self.app_url}/"

    @classmethod
    def initialize(cls) -> Self:  # Возвращает экземпляр класса Settings
        # Указываем пути
        videos_dir = Path("./videos")
        tracing_dir = Path("./tracing")
        browser_state_file = Path("./sessions/browser-state.json")

        # Создаем директории, если они не существуют
        videos_dir.mkdir(exist_ok=True)  # Если директория существует, то игнорируем ошибку
        tracing_dir.mkdir(exist_ok=True)
        # Создаем файл состояния браузера, если его нет
        browser_state_file.touch(exist_ok=True)  # Если файл существует, то игнорируем ошибку

        # Возвращаем модель с инициализированными значениями
        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            browser_state_file=browser_state_file
        )


settings = Settings.initialize()
