
from pydantic_settings import BaseSettings
import dotenv


class Config(BaseSettings):
    browserstack_username: str
    browserstack_key: str
    browserstack_url: str = 'http://hub.browserstack.com/wd/hub'
    app_url: str = 'bs://sample.app'
    ios_app_url: str = "bs://bfc9cb387aa35409d0506f4fa345e2ab8fd20135"
    project_name: str = 'Mobile Tests Lesson 1'
    build_name: str = 'browserstack-build-1'
    session_name: str = 'BStack first_test'
    android_version: str = '9.0'
    android_device: str = 'Google Pixel 3'
    android_platform: str = 'android'
    ios_device: str = 'iPhone XS'
    ios_version: str = '13'
    ios_platform: str = 'ios'


config = Config(_env_file=dotenv.find_dotenv(), _env_file_encoding='utf-8')
